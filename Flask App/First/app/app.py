# Importing required libs
from flask import Flask, render_template, request
from model import preprocess_img, predict_result

# Instantiating flask app
app = Flask(__name__)

dict = {}
dict['0'] = 'bougainvillea'
dict['1'] = 'daffodil'
dict['2'] = 'dahlia'
dict['3'] = 'foxglove'
dict['4'] = 'hibiscus'
dict['5'] = 'hydrangea'
dict['6'] = 'orchid'
dict['7'] = 'rose'
dict['8'] = 'sunflower'
dict['9'] = 'tulip'

# Home route
@app.route("/")
def main():
    return render_template("index.html")


# Prediction route
@app.route('/prediction', methods=['POST'])
def predict_image_file():
    try:
        if request.method == 'POST':
            request.files['file'].save("./predict/predict.jpg")
            img_data = preprocess_img()
            pred_digits = predict_result(img_data)
            label_digit = str(pred_digits[0])
            return render_template("result.html", predictions=dict[label_digit].capitalize())

    except Exception:
        error = "File cannot be processed."
        return render_template("result.html", err=error)


# Driver code
if __name__ == "__main__":
    app.run(debug=True)