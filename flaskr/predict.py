from fastai.learner import load_learner
from fastai.vision.core import PILImage
from pathlib import Path

model_path = Path('models', 'model.pkl')
test_image_path = Path('assets', 'doyel.jpg')

learner = load_learner(model_path)


def predict_bird(img):
    pred, pred_idx, probs = learner.predict(PILImage.create(img))

    pred_value = f'Prediction: {pred}; Probability: {probs[pred_idx]:.04f}'

    # print('Loaded learner')
    # print(learner.dls.vocab)
    return pred_value


if __name__ == '__main__':
    pred = predict_bird(test_image_path)
    print(pred)
