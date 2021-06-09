from flask import Flask,  app, request, Response, render_template, jsonify
from predict import predict_bird
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = "SECRET_KEY"
CORS(app)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Create a URL route in our application for "/"


@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/

    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')


@app.route('/image', methods=['GET', 'POST'])
def upload_file():
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

            pred_value = predict_bird(file)
            pred_res = jsonify({'prediction': pred_value})
            print(pred_res)
            return pred_res


if __name__ == '__main__':
    app.run(debug=True)
