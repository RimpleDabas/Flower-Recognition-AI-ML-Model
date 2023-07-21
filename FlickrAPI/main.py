from flickr import get_urls
from downloader import download_images
import os
import time

#all_flowers = ['rose' , ' orchid' , ' bougainvillea' , ' hibiscus' , 'sunflower']
all_flowers = ['tulip' , 'hydrangea', 'dahlia', 'foxglove', 'daffodil']
images_per_flower = 200

def download():
    for flower in all_flowers:

        print('Getting urls for', flower)
        urls = get_urls(flower, images_per_flower)
        
        print('Downloading images for', flower)
        path = os.path.join('data', flower)

        download_images(urls, path)

if __name__=='__main__':

    start_time = time.time()

    download()

    print('Took', round(time.time() - start_time, 2), 'seconds')