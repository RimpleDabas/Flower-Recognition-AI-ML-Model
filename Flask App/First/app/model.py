from keras.models import load_model
import numpy as np
import cv2

# Loading model
model = load_model("./model/final-model-256.h5")

def preprocess_img():
    img = cv2.imread("./predict/predict.jpg", cv2.IMREAD_COLOR)
    img = cv2.resize(img, (256, 256))
    
    return np.array(img)

# Predicting function
def predict_result(predict):
    pred = model.predict(np.expand_dims(predict, 0))
    return np.argmax(pred, axis=1)