#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tkinter as tk
from tkinter import filedialog
from tkinter import *

from PIL import ImageTk, Image
import numpy

# We need to load the trained model from the 'Road Traffic Sign Recognition.ipynb' as saved in the hdf5 file.
from keras.models import load_model
model = load_model('model_RTSR.h5')

# To label all the traffic signs with their respective class names, we are required to create a dictionary.
classes = { 1:'Speed limit (20km/h)',
            2:'Speed limit (30km/h)', 
            3:'Speed limit (50km/h)', 
            4:'Speed limit (60km/h)', 
            5:'Speed limit (70km/h)', 
            6:'Speed limit (80km/h)', 
            7:'End of speed limit (80km/h)', 
            8:'Speed limit (100km/h)', 
            9:'Speed limit (120km/h)', 
            10:'No passing', 
            11:'No passing veh over 3.5 tons', 
            12:'Right-of-way at intersection', 
            13:'Priority road', 
            14:'Yield', 
            15:'Stop', 
            16:'No vehicles', 
            17:'Veh > 3.5 tons prohibited', 
            18:'No entry', 
            19:'General caution', 
            20:'Dangerous curve left', 
            21:'Dangerous curve right', 
            22:'Double curve', 
            23:'Bumpy road', 
            24:'Slippery road', 
            25:'Road narrows on the right', 
            26:'Road work', 
            27:'Traffic signals', 
            28:'Pedestrians', 
            29:'Children crossing', 
            30:'Bicycles crossing', 
            31:'Beware of ice/snow',
            32:'Wild animals crossing', 
            33:'End speed + passing limits', 
            34:'Turn right ahead', 
            35:'Turn left ahead', 
            36:'Ahead only', 
            37:'Go straight or right', 
            38:'Go straight or left', 
            39:'Keep right', 
            40:'Keep left', 
            41:'Roundabout mandatory', 
            42:'End of no passing', 
            43:'End no passing veh > 3.5 tons' }


# Initialising the user interface.
top=tk.Tk()
top.geometry('1200x700')
top.title('Road Traffic Sign Recognition')
top.configure(background='#2F4F4F')
label=Label(top,background='#2F4F4F', font=('georgia',20,'bold'))
sign_image = Label(top)


# The function defined below is used to resize the image that is selected by the user.
# Also, it displays the respective class name of the selected image by using the stored predicted data in the hdf5 file created in the 'Road Traffic Sign Recognition.ipynb'
def classify(file_path):
    global label_packed
    image = Image.open(file_path)
    image = image.resize((30,30))
    image = numpy.expand_dims(image, axis=0)
    image = numpy.array(image)
    pred = model.predict_classes([image])[0]
    sign = classes[pred+1]
    print(sign)
    label.configure(foreground='#FFC0CB', text=sign) 
    
    
# A user interactive button is required which on trigger displays the sign.
def show_classify_button(file_path):
    classify_b=Button(top,text="Recognize the Sign ?",command=lambda: classify(file_path),padx=10,pady=10)
    classify_b.configure(background='#FEBD07', foreground='#2F4F4F',font=('georgia',15,'bold'))
    classify_b.place(relx=0.40,rely=0.38)
    
    
# After the user selects an image we need to upload the image on the interface.
def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=im)
        sign_image.image=im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass
    

# Now we need to create a user interactive button so that the user can select an image from the file path.
upload=Button(top,text="Select a traffic sign",command=upload_image,padx=10,pady=10)
upload.configure(background='#FEBD07', foreground='#2F4F4F',font=('georgia',15,'bold'))
upload.pack(side=BOTTOM,pady=50)
sign_image.pack(side=BOTTOM,expand=True)
label.pack(side=BOTTOM,expand=True)
heading = Label(top, text="Road Traffic Sign Recognition",pady=20, font=('georgia',30,'bold'))
heading.configure(background='#2F4F4F',foreground='#FFD700')
heading.pack()

# The entire code should be repeated on each instance triggered by the user. For that we use the mainloop()
top.mainloop()


# In[ ]:




