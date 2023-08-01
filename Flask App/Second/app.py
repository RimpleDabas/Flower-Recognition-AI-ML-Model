from flask import Flask, render_template, request
import numpy as np
from keras.preprocessing.image import img_to_array
from keras.models import load_model
#from keras.preprocessing import image
import cv2
app = Flask(__name__)

# Loading the model
model = load_model('final-model-256.h5')
flowers = {'0': 'Bougainvilliea', '1': 'Daffodil', '2': 'Dahlia', '3': 'Foxglove','4':'Hibiscus','5':'Hydrangea','6':'Orchid','7': 'Rose','8':'Sunflower','9': 'Tulip'}

@app.route("/")
def main():
    return render_template("index.html")

# Initializing flask application
app = Flask(__name__)
@app.route("/")
def about():
    return render_template('index.html')

@app.route('/submit', methods=['GET','POST']) # submit route here is linked to html
def upload_file():
    if request.method == 'POST':
        file = request.files['my_image']
        Image_path= "./static/" + file.filename	
        file.save(Image_path)
        #print(Image_path)
        img = cv2.imread(Image_path, cv2.IMREAD_COLOR)
        img = cv2.resize(img, (256, 256))
        image = img_to_array(img)
        image = np.expand_dims(image,axis=0)
        #print(result)
        label = str(np.argmax(model.predict(image),axis=1)[0])
        print(label)
    return render_template('index.html', prediction = flowers[label], img_path = Image_path) # prediction and img_path linked to html

if __name__ == "__main__":
    app.run(debug=True)
