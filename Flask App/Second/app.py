from flask import Flask, render_template, request
import numpy as np
from keras.preprocessing.image import img_to_array
from keras.models import load_model
from keras.preprocessing import image

app = Flask(__name__)

# Loading the model
model = load_model('model_79.h5')
flowers = {'0': 'Bougainvilliea', '1': 'Daffodil', '2': 'Dahlia', '3': 'Foxglove','4':'Hibiscus','5':'Hydrangea','6':'Orchid','7': 'Rose','8':'Sunflower','9': 'Tulip'}

@app.route("/")
def main():
    return render_template("index.html")

# Initializing flask application
app = Flask(__name__)
@app.route("/")
def about():
    return render_template('index.html')

@app.route('/submit', methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['my_image']
        Image_path= "./static/" + file.filename	
        file.save(Image_path)
        i = image.load_img(Image_path,target_size = (150,150))
        i = image.img_to_array(i)/255.0
        result = model.predict(np.expand_dims(i,0))
        answer = np.argmax(result,axis=1)[0]
        label = str(answer)
    return render_template('index.html', prediction = flowers[label], img_path = Image_path)

if __name__ == "__main__":
    app.run(debug=True)
