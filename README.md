# Flower-Recognition Model
![image](/Images/Dashboard_1.png)
In this project we aimed to train Convolutional Neural Network(CNN) for flower recognizion and built a flask based app for it. Our app allows users to upload an image and predictions.We currently have model for the following ten flowers.
 - Bougainvillea 
 - Daffodil
 - Dahlia
 - Foxglove
 - Hibiscus
 - Hydrangea
 - Orchid
 - Rose
 - Sunflower
 - Tulip

App predicts the flower as shown below
![gif](/Images/Dashboard.gif)

It further allows the user to give an input and allows to upload another image.
![](/Images/Dashboard_4.png)
## Data collection
The data for testing and training our model was collected from three sources
 - Web scraping from Google Images
 - API requests from Flickr 
 - API request from Pixabay
Codes for these files are in the folders based on their names. 

## Data Cleaning 
This step involved getting rid of junk images such as drawings, flowers tagged in wrong categories etc. This was done manually. After cleaning we arranged flowers folderwise so as to use them for labeling in the preprocessing steps. The combined data is located [here](https://github.com/joshi-swetam/Flower-Recognition-AI-ML-Model/tree/main/Combined%20flowers)


## Model Training and testing

As part of preprocessing step we rescaled, resized and labeled our data.We then converted our images and labels as .npy files for ease of storing and using them in models. The files can be located [here](https://github.com/joshi-swetam/Flower-Recognition-AI-ML-Model/tree/main/Models/dataset). We used tensorflow and Keras for training our model. We stared with different combinations of Convolutional and pooling layers for feature extractions.The clasiffication layers were combinations of flatten ,dense and dropout layers. We tried building layers with different optimizers and activations functions. We also tried transfer leaning models but they were computaionally more expensive and time consuming. The best accuracy we could reach was 79 percent.All our ipynb files and .h5 saved models can be referred [here](https://github.com/joshi-swetam/Flower-Recognition-AI-ML-Model/tree/main/Models)

We quantified our model using confusion matrix and classification report.After saving the model we made predictions using prediction dataset.
![image](/Images/Picture_79.png)

As classification report depicts the accuracy of our model is 79% although the precision differs for flowers. It performs well with sunflowers and bougainvillea but not so well in predicting hyrangea and rose. Another thing we noticed that significant number of daffodils were being classified as sunflowers.
If we look at the confusion matrix and classification report for the 76% accuracy below it performs well in predicting rose as well as Daffodils in comparison to the model with 79% accuracy. 
![Image](/Images/Picture_76.png)

## Flask App
We then made flask based app to upload the image and make predictions. The files for the same can be located [here](https://github.com/joshi-swetam/Flower-Recognition-AI-ML-Model/tree/main/Flask%20App)

## Limitations
 - Our dataset was limited. We had approx 300 images per category. Having more images would have allowed for better accuracy.
 - Training models was time consuming and that limited us for conducting more trails.
 - We did not try pre processing steps such as edge detection and enhancement which could have allowed us to get better accuracy.

 ## References
- https://medium.com/@draj0718/convolutional-neural-networks-cnn-architectures-explained-716fb197b243
- https://medium.com/@adrianmrit/creating-simple-image-datasets-with-flickr-api-2f19c164d82f
- https://pixabay.com/api/docs/#api_search_images
- https://medium.com/@ferrygunawan/create-flower-image-classification-with-tensorflow-keras-and-flask-4fd6efd4c5ac
