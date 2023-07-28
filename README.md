# Flower-Recognition Model

----Insert dashboard image here-----

In this project our aim is to train Convolutional Neural Network(CNN) for flower recognizion and built a flask based app for it. We currently have model for the following ten flowers .
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
![image](/Images/Picture1.jpg)

As classification report depicts the accuracy of our model is 79% although the precision differs for flowers. It performs well with sunflowers and foxglove but not so well in predicting flowers.

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

