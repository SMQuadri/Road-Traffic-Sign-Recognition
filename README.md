# Road-Traffic-Sign-Recognition

## Overview :
Traffic sign recognition is the process of automatically identifying which class the respective sign belongs to. The earlier Computer Vision techniques required lots of hard work in data processing and it took a lot of time to manually extract the features of the image. Instead, today deep learning techniques have become more popular for performing computer vision or image processing tasks. The goal of this project is to build a traffic sign recognition system for autonomous vehicles.
![trafficSR](https://user-images.githubusercontent.com/55687431/86936099-2da20900-c15b-11ea-991a-508e9b86ecc1.jpg)



## Dataset :
German Traffic Sign Recognition Dataset (GTSRB) is an image classification dataset.
The images used in this dataset are those of traffic signs. The images are classified into 43 different classes. The training set contains 39209 labeled images and the test set contains 12630 images.


## Environments used :
-> Anaconda Navigator (jupyter notebook and spyder)

-> PyCharm


## Libraries used :
-> pandas

-> numpy

-> matplotlib

-> sklearn

-> pillow

-> os

-> keras (with tensorflow backend)

-> tkinter (for deployment of the model)


## Steps to build the project :
1) Setup the project and virtual environment.
2) Install the required dependencies and the libraries in your virtual environment.
3) Import the installed libraries.
4) Interpret the data & fetch the path of the required directory using the os library.
5) Resize the images.
6) Store the traffic sign images from the 'Train' dataset and their respective labels in the form of numpy arrays.
7) Perform the train_test_split() on the 'Train' dataset. 
8) Convert the labelled data (i.e; the class labels of their respective images) into its one-hot vector using to_categorical(). This function can be imported from the library 'utils' present in 'keras'.
9) Create a Sequential() model and pass a list of its layer instances to create a CNN model architechture.
10) Add a convolution layer to the input image and assign appropriate parameters to it.
11) Then pool the convo layer created above using MaxPool() to reduce the dimensions of the image pattern window generated.
12) Add a dropout layer to this set to prevent model overfitting during training process.
13) Now add one more convolution layer which takes the output of the previous layer as its input. We are doing this in order to extract all possible (even minute) features from the image. Here, as this layer is more far from the direct image we can increase the size of 'filters' and decrease the 'kernel_size' in the parameters.
14) Simliar to the above layer instance, pool the convolution layer in step (13) using MaxPool.
15) Also, add a dropout layer to it.
16) Now, add a Flatten layer to convert the feature matrix into a its vector representation.
17) Implement the last layer of the CNN model i.e; the Dense layer (Fully Connected layer).
18) Apply softmax application in only the last layer (i.e; dense layer) as we are implementing a multi classification problem.
19) Complie this model created by setting the optimizer as 'Adam', the loss as 'categorical_crossentropy' & the metric to be used as 'accuracy'.
20) After the building of the model architechture, now train the model using model.fit()
21) Now, visualize the results by plotting graphs between acc and val_acc & loss and val_loss.
22) The next step is to implement the model architechture over the 'test.csv' dataset. This dataset contains the path of the image in the 'test' folder.
23) Save the results of the prediction over the 'test.csv' dataset in a heirarchical data file (i.e; hdf5 format).
24) The last step is to deploy the model. You can either do this by creating a flask application which renders an HTML template (OR) by creating a python file which contains a tkinter program & then deploy it on your local host.


## Model Evaluation :
The model achieved 97.09% accuracy on the validation set (random 20% subset of the training dataset) & 96.37% on the 'test.csv' dataset.



# Repository Contents :
1) Datasets Folder: Contains the link of the kaggle kernel from where the datasets can be downloaded.
2) Demo Images folder : Contains screenshots of output demo of my project.
3) Project Demonstration.zip : This zip folder contains a video demonstrating the project output. To view it you need to download the zip folder.
4) Road Traffic Sign Recognition.ipynb : This notebook contains the model architechture and the code for predicting the new data.
5) interface.py : This python file contains the tkinter program for deployment of the project on local host to provide a GUI to the user.
6) model_RTSR.h5 : This heirarchical data file contains the stored predicitions for the 'test.csv' dataset which is further used to load the model in 'interface.py'
