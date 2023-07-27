# Flower-Recognition Model
In this project our aim is to train Convolutional Neural Network(CNN) for flower recognizion and built a flask based app for it. 
## Data collection
The data for testing and training our model were collected from three sources
 - Web scraping from Google Images
 - API requests from Flickr 
 - API request from Pixabay

## Data Cleaning 
This step involved getting rid of junk images such as drawings, flowers tagged in wrong categories etc. This was done manually.We collected data flowerwise in folders to use them as labels for our machine learning. The combined data is located [here](https://github.com/joshi-swetam/Flower-Recognition-AI-ML-Model/tree/main/Combined%20flowers)

## Model Training and testing

As part of preprocessing step we rescaled, resized and labeled our data.We used tensorflow and Keras for training our model.We stared with different combinations of Convolutional, pooling, flatten and dense layers to train our models. The files for which are located here. . We tried building layers with different optimizers and activations functions. Augmentation and dropout were done as needed. We also tried transfer leaning models but they were computaionally more expensive and time consuming. The best accuracy we could reach was   and model for the same can be located here.

We quantified our model using confusion matrix and classification report.After saving the model we made predictions using prediction dataset. 

## Flask App
We then made flask based app to upload the image and make predictions. The files for the same can be located here

## Limitations
 - Our dataset was limited. We had approx 300 images per category. Having more images would have allowed for better accuracy.
 - Training models was time consuming and that limited us for conducting more trails.
 - We did not try pre processing steps such as edge detection and enhancement which could have allowed us to get better accuracy.


