from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from keras.preprocessing import image
from tensorflow.keras.preprocessing.image import img_to_array
import numpy as np 
import cv2

app = Flask(__name__)

model = load_model('final-model-256.h5')
@app.route("/")

def predict_label(img_path):
	image = cv2.imread(img_path, cv2.IMREAD_COLOR)
	image = cv2.resize(image, (256, 256))
	image = img_to_array(image)
	image = np.expand_dims(image,axis=0)
	answer = np.argmax(model.predict(image),axis=1)[0]
	if  answer == 0:
		print("Label: Bougainvillea")
	elif answer == 1:
		print("Label: Daffodil")
	elif answer == 2:
		print("Label: Dahlia")
	elif answer == 3:
		print("Label : Foxglove")
	elif answer == 4: 
		print("Label : Hibiscus")
	elif answer == 5:
		print("Label: Hydrangea")
	elif answer == 6: 
		print("Label : Orchid")
	elif answer == 7:
	    print("Label: Rose")
	elif answer == 8 :
		print("Label: Sunflower")    
	elif answer == 9:
	    print("Label: Tulip")
	return answer    


# routes
@app.route("/", methods=['GET', 'POST'])
def main():
	return render_template("index.html")


@app.route("/submit", methods = ['GET', 'POST'])
def get_output():
	if request.method == 'POST':
		img = request.files['my_image']
		img_path = "static/" + img.filename	
		img.save(img_path)
		p = predict_label(img_path)
	return render_template("index.html", prediction = p, img_path = img_path)

if __name__ =='__main__':
	#app.debug = True
	app.run(debug = True)