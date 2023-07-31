from flask import Flask, render_template, request
import numpy as np
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import cv2

app = Flask(__name__)

# Loading the model
model = load_model('model_79.h5')
#flowers = {'0': 'Bougainvilliea', '1': 'Daffodil', '2': 'Dahlia', '3': 'foxglove','4':'Hibiscus','5':'Hydrangea','6':'Orchid','7': 'Rose','8':'Sunflower','9': 'Tulip'}
flowers = ['Bougainvilliea', 'Daffodil', 'Dahlia',  'foxglove','Hibiscus','Hydrangea','Orchid', 'Rose','Sunflower', 'Tulip']
@app.route("/")
def main():
    return render_template("index.html")

def processImg(IMG_PATH):
    # Read image
    model = load_model("model_79.h5")
    # Preprocess image
    image = cv2.imread(IMG_PATH)
    image = cv2.resize(image, (150, 150))
    image = image.astype("float") / 255.0
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    res = model.predict(image)
    label = np.argmax(res)
    print("Label", label)
    labelName = flowers[label]
    print("Label name:", labelName)
    return labelName


# Initializing flask application
app = Flask(__name__)
@app.route("/")
def template_test():
    return render_template('template.html', label='', imagesource='Picture5.jpg')

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        import time
        start_time = time.time()
        file = request.files['file']
        file.save(file_path)
        result = processImg(file_path)
        label = np.argmax(result)
        print("Label", label)
        labelName = flowers[label]
        print("Label name:", labelName)
        return render_template('template.html', label=label, imagesource='../uploads/' + filename)



if __name__ == "__main__":
    app.run(debug=True)
