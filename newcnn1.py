# coding: utf-8

# In[ ]:

from keras.layers import Conv2D, MaxPooling2D, AveragePooling2D


from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator

import numpy as np

#------------------------------
# sess = tf.Session()
# keras.backend.set_session(sess)
#------------------------------
#variables
num_classes =15
batch_size = 40
epochs = 150
#------------------------------

import os, cv2, keras

from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.engine.saving import load_model
# manipulate with numpy,load with panda
import numpy as np
# import pandas as pd

# data visualization
import cv2

# Data Import
def read_dataset(path):
    data_list = []
    label_list = []
    i=-1
    my_list = os.listdir(r'C:\Users\hp\PycharmProjects\FoodRecipieRecommendation\src\static\train')
    for pa in my_list:
        i=i+1
        print(pa,"==================")
        for root, dirs, files in os.walk(r'C:\Users\hp\PycharmProjects\FoodRecipieRecommendation\src\static\train\\' + pa):

         for f in files:
            file_path = os.path.join(r'C:\Users\hp\PycharmProjects\FoodRecipieRecommendation\src\static\train\\'+pa, f)
            img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
            res = cv2.resize(img, (48, 48), interpolation=cv2.INTER_CUBIC)
            data_list.append(res)
            label = i
            label_list.append(label)
            # label_list.remove("./training")
    return (np.asarray(data_list, dtype=np.float32), np.asarray(label_list))

def read_dataset1(path):
    data_list = []
    label_list = []

    file_path = os.path.join(path)
    img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    res = cv2.resize(img, (48, 48), interpolation=cv2.INTER_CUBIC)
    data_list.append(res)
    # label = dirPath.split('/')[-1]

            # label_list.remove("./training")
    return (np.asarray(data_list, dtype=np.float32))

# from sklearn.model_selection import train_test_split
# # load dataset
# x_dataset, y_dataset = read_dataset(r"")
# X_train, X_test, y_train, y_test = train_test_split(x_dataset, y_dataset, test_size=0.2, random_state=0)
#
# y_train1=[]
# for i in y_train:
#     emotion = keras.utils.to_categorical(i, num_classes)
#     print(i,emotion)
#     y_train1.append(emotion)
#
# y_train=y_train1
# x_train = np.array(X_train, 'float32')
# y_train = np.array(y_train, 'float32')
# x_test = np.array(X_test, 'float32')
# y_test = np.array(y_test, 'float32')
#
# x_train /= 255  # normalize inputs between [0, 1]
# x_test /= 255
#
# print("x_train.shape",x_train.shape)
# x_train = x_train.reshape(x_train.shape[0], 48, 48, 1)
# x_train = x_train.astype('float32')
# x_test = x_test.reshape(x_test.shape[0], 48, 48, 1)
# x_test = x_test.astype('float32')
#
# print(x_train.shape[0], 'train samples')
# print(x_test.shape[0], 'test samples')
# ------------------------------

# construct CNN structure
#
# model = Sequential()
#
# # 1st convolution layer
# model.add(Conv2D(64, (5, 5), activation='relu', input_shape=(48, 48, 1)))
# model.add(MaxPooling2D(pool_size=(5, 5), strides=(2, 2)))
#
# # 2nd convolution layer
# model.add(Conv2D(64, (3, 3), activation='relu'))
# model.add(Conv2D(64, (3, 3), activation='relu'))
# model.add(AveragePooling2D(pool_size=(3, 3), strides=(2, 2)))
#
# # 3rd convolution layer
# model.add(Conv2D(128, (3, 3), activation='relu'))
# model.add(Conv2D(128, (3, 3), activation='relu'))
# model.add(AveragePooling2D(pool_size=(3, 3), strides=(2, 2)))
#
# model.add(Flatten())
#
# # fully connected neural networks
# model.add(Dense(1024, activation='relu'))
# model.add(Dropout(0.2))
# model.add(Dense(1024, activation='relu'))
# model.add(Dropout(0.2))
#
# model.add(Dense(num_classes, activation='softmax'))
# # ------------------------------
# # batch process
#
# print(x_train.shape)
#
# gen = ImageDataGenerator()
# train_generator = gen.flow(x_train, y_train, batch_size=batch_size)
#
# # ------------------------------
#
# model.compile(loss='categorical_crossentropy'
#               , optimizer=keras.optimizers.Adam()
#               , metrics=['accuracy']
#               )
#
# # ------------------------------
#
# if not os.path.exists("model1.h5"):
#
#     model.fit_generator(train_generator, steps_per_epoch=batch_size, epochs=epochs)
#     model.save("model1.h5")  # train for randomly selected one
# else:
#     model = load_model("model1.h5")  # load weights
# from sklearn.metrics import confusion_matrix
# yp=model.predict_classes(x_test,verbose=0)
# cf=confusion_matrix(y_test,yp)
# print(cf)

#================================================segmentation========================================================

THRESH = 240
orig = cv2.imread(r"C:\Users\hp\PycharmProjects\FoodRecipieRecommendation\src\static\vrg.jpg")
img = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)

# Make the faint 1-pixel boundary bolder
rows, cols = img.shape
new_img = np.full_like(img, 255)    # pure white image
for y in range(rows):
    if not (y % 10):
        print ('Row = %d (%.2f%%)' % (y, 100.*y/rows))
    for x in range(cols):
        score  = 1 if y > 0 and img.item(y-1, x) < THRESH else 0
        score += 1 if x > 0 and img.item(y, x-1) < THRESH else 0
        score += 1 if y < rows-1 and img.item(y+1, x) < THRESH else 0
        score += 1 if x < cols-1 and img.item(y, x+1) < THRESH else 0
        if img.item(y, x) < THRESH or score >= 2:
            new_img[y, x] = 0       # black pixels show boundary

cv2.imwrite('thresh.png', new_img)

# Find all contours on the map
_th, contours, hierarchy = cv2.findContours(new_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
print( "Number of contours detected = %d" % len(contours))

# Fill second level regions on the map
coln = 0
colors = [
    [127, 0, 255],
    [255, 0, 127],
    [255, 127, 0],
    [127, 255, 0],
    [0, 127, 255],
    [0, 255, 127],
]
hierarchy = hierarchy[0]
for i in range(len(contours)):
    area = cv2.contourArea(contours[i])
    if hierarchy[i][3] == 1:
        print("=====================")
        print (i, area)
        coln = (coln + 1) % len(colors)
        cv2.drawContours(orig, contours, i, colors[coln], -1)

cv2.imwrite("colored_map.png", orig)

#=====================================================prediction=======================================================

def predict(fn):
    dataset=read_dataset1(fn)
    (mnist_row, mnist_col, mnist_color) = 48, 48, 1
    dataset = dataset.reshape(dataset.shape[0], mnist_row, mnist_col, mnist_color)
    dataset=dataset/255
    mo = load_model("model1.h5")

    # predict probabilities for test set

    yhat_classes = mo.predict_classes(dataset, verbose=0)
    return yhat_classes
#
#     print(yhat_classes)

print(predict(r"C:\Users\hp\PycharmProjects\FoodRecipieRecommendation\src\static\0008.jpg"))