# What are Those?! Sneaker Classifier 

By Jeffrey Li

Last Updated: March 1, 2024

## Project Summary

In this project, I wanted to answer a popular question that first gained traction in 2015 from a viral Vine video: What are Those?! Often times, a sick pair of kicks in the wild catches our eye, but we have no idea what brand or model they are. I propose this program that can provide users with the correct name and model of sneakers, given an image. 

The project pipeline involves six major steps: (1) gathering raw data through web-scraping images of sneakers on Google Image, (2) manually cleaning image data to ensure quality and consistency, (3) processing images and creating training and validation sets, (4) developing a convolutional neural network (CNN) architecture for multiclass classification tasks, (5) training and validating the model on sneaker images, and (6) optimizing the model through hyperparameter tuning and changes in architectural design. 

From the qualitative assessment, the model appears to generalize well, capable of distinguishing footwear of different color ways. Through incorporating architectural changes, including implementing batch normalization prior to RELU activation, and introducing augmentation techniques during the training process, I improved validation accuracy from 67% to 86%. 

Currently, more work is being done to extract images of footwear from other brands, such as adidas, New Balance, and Nike, to diversify and continually update the image repository. Some short term goals include: (1) looking into and experimenting with pretrained models and (2) designing and executing a web or mobile interface for the model. 

## Content

- **create_dataset.py:** creates image datasets in your local directory
    - Each type of sneaker model will have its own directory named after the SKU.
    - Each image in the SKU directory will be numbered.
    - The images are then divided into training and testing files. The default is 70:30 split.  

- **dataloader.py:** creates a separate dataloader for the training or testing image datasets using the [torch.utils.data.DataLoader](https://pytorch.org/docs/stable/data.html) class

- **image-scraping-driver.py:** image-scraping Selenium driver for Google Images 
    - You will need to download the correct [ChromeDriver](https://chromedriver.chromium.org/downloads) for your version of Google Chrome for this driver to work. 
    - Resources/References:
        - [Automating Google Chrome to Scrape Images with Selenium and Python](https://www.youtube.com/watch?v=7KhuEsq-I8o)
        - [A Beginner’s Guide to Image Scraping with Python and Selenium](https://medium.com/@nithishreddy0627/a-beginners-guide-to-image-scraping-with-python-and-selenium-38ec419be5ff)

- **model-training-assessment.ipynb:** contains training and validation loops and qualitative and quantiative assessments 

- **model.py:** contains the architecture of CNN 

## Model Architecture

| Layer  | Operation                                 | Input Size          | Output Size         |
|--------|-------------------------------------------|---------------------|---------------------|
| Conv1  | Conv2d(3, 32, kernel_size=3, stride=1, pad=1)| (224, 224, 3)       | (224, 224, 32)      |
| BN1    | BatchNorm2d(32)                            | (224, 224, 32)      | (224, 224, 32)      |
| ReLU   | ReLU()                                     | (224, 224, 32)      | (224, 224, 32)      |
| Pool1  | MaxPool2d(kernel_size=2, stride=2)         | (224, 224, 32)      | (112, 112, 32)      |
| Conv2  | Conv2d(32, 64, kernel_size=3, stride=1, pad=1)| (112, 112, 32)     | (112, 112, 64)      |
| BN2    | BatchNorm2d(64)                            | (112, 112, 64)      | (112, 112, 64)      |
| ReLU   | ReLU()                                     | (112, 112, 64)      | (112, 112, 64)      |
| Pool2  | MaxPool2d(kernel_size=2, stride=2)         | (112, 112, 64)      | (56, 56, 64)        |
| Conv3  | Conv2d(64, 128, kernel_size=3, stride=1, pad=1)| (56, 56, 64)       | (56, 56, 128)       |
| BN3    | BatchNorm2d(128)                           | (56, 56, 128)       | (56, 56, 128)       |
| ReLU   | ReLU()                                     | (56, 56, 128)       | (56, 56, 128)       |
| Pool3  | MaxPool2d(kernel_size=2, stride=2)         | (56, 56, 128)       | (28, 28, 128)       |
| Flatten| Flatten()                                  | (28, 28, 128)       | 100352              |
| FC1    | Linear(100352, 256)                       | 100352              | 256                 |
| ReLU   | ReLU()                                     | 256                 | 256                 |
| FC2    | Linear(256, 10)                           | 256                 | 10                  |


## Sample Images 

| Image| SKU | Model |
|----------|----------|------------------------------|
| ![Image 1](/assests/img/sample/555088-105.jpg) | 555088-105 | Jordan 1 Retro High Dark Mocha |
| ![Image 2](/assests/img/sample/555088-126.jpg) | 555088-126 | Jordan 1 Retro High Light Smoke Grey |
| ![Image 3](/assests/img/sample/555088-500.jpg) | 555088-500 | Jordan 1 Retro High Court Purple White |
| ![Image 4](/assests/img/sample/555088-711.jpg) | 555088-711 | Jordan 1 Retro High OG Taxi
| ![Image 5](/assests/img/sample/DC1788-100.jpg) | DC1788-100 | Jordan 1 Retro High CO.JP Midnight Navy (2020) |
| ![Image 6](/assests/img/sample/DD9335-641.jpg) | DD9335-641 | Jordan 1 Retro High OG Atmosphere (Women's) |
| ![Image 7](/assests/img/sample/DO7097-100.jpg) | DO7097-100 | Jordan 1 Retro High OG A Ma Maniére |
| ![Image 8](/assests/img/sample/DZ5485-031.jpg) | DZ5485-031 | Jordan 1 Retro High OG Lucky Green |
| ![Image 9](/assests/img/sample/DZ5485-400.jpg) | DZ5485-400 | Jordan 1 Retro High OG UNC Toe |
| ![Image 10](/assests/img/sample/DZ5485-612.jpg) | DZ5485-612 | Jordan 1 Retro High OG Chicago Lost and Found |

## Results

![augmentation](/assests/img/augmentation.PNG)

Training image samples following augmentation 

![augmentation](/assests/img/acc_curve.PNG)

Validation accuracy curves for three experiments:
- Experiment 1 (67.4%): only RELU activation and MaxPool layer following convolutional layer
- Experiment 2 (78.1%): introduced Batch Normalization prior to each RELU activation layer
- Experiment 3 (86.0%): introduced data augmentation techniques for training set, namely Normalization, RandomRotation, and RandomHorizontalFlip 

![augmentation](/assests/img/loss_curve.PNG)

![augmentation](/assests/img/confusion_matrix.PNG)
