# What are Those?! Sneaker Classifier 

By Jeffrey Li

Last Updated: March 1, 2024

## Project Summary

In this project, I wanted to answer the popular question that first gained traction in 2015 from a viral Vine video: What are Those?! Often times, a sick pair of kicks in the wild catches our eye, but we have no idea what brand or model they are. I propose a program that can provide users the correct name and model of sneakers provided an image. 

The project pipeline involves three major steps: (1) gathering raw image data through web-scraping images of sneakers on Google Image, (2) manually cleaning image data to ensure quality and consistency, (3) processing images and creating training and validation sets, (4) developing a convolutional neural network (CNN) architecture for multiclass classification tasks, (5) training and validating the model on sneaker images, and (6) optimizing the model through hyperparameter tuning and changes in architectural design. 

From our model assessment, the model appears to generalize well, distinguishing footwear of different colors. Through incorporating architectural changes, including implementing batch normalization prior to RELU activation, and introducing augmentation techniques during training, I improved validation accuracy from 67% to 86%. 

Currently, more work is being done to extract images of footwear from other brands, such as adidas, New Balance, and Nike, to diversify and continually update the image repository. Some short term goals include: (1) looking into and experimenting with pretrained models and (2) designing and executing a web or mobile interface for the model. 

