import os
from flask import Flask,  app, request, Response, render_template, jsonify
from flaskr.predict import predict_bird
import flaskr.config as config
from flask_cors import CORS
from flaskr.utils import allowed_file

config_map = {
    'development': config.Development(),
    'production': config.Production(),
}

flask_env = os.environ.get("FLASK_ENV") or "development"
config_obj = config_map[flask_env.lower()]

app = Flask(__name__)
app.config.from_object(config_obj)
app.secret_key = "SECRET_KEY"
CORS(app)


@app.route('/image', methods=['POST'])
def upload_file():
    """
    This function handles image uploads and predicts what type of bird the image is

    """
    if request.method == 'POST':
        if 'file' not in request.files:
            print("No file part")
            return Response("{'message':'No file part found'}", status=400, mimetype='application/json')
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            print('No selected file')
            return Response("{'message':'No selected file'}", status=400, mimetype='application/json')
        if file and allowed_file(file.filename):

            pred, prob = predict_bird(file)
            pred_res = jsonify({'prediction': pred, 'probability': prob})
            return pred_res


if __name__ == '__main__':
    app.run(debug=True)
