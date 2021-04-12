#------------------------------------------------------------------------------#
#     Import Libraries                                                         #
#------------------------------------------------------------------------------#

import keras
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import time
import numpy as np
import random
import pandas as pd
import math

#------------------------------------------------------------------------------#
#     Read in CSV table                                                        #
#------------------------------------------------------------------------------#

df = pd.read_csv('/content/drive/MyDrive/ColabStuff/ET Landing/bounding_boxes.csv')
BBFrame = df[['Frame']].values
BBCordX = df[['TopLeftCornerX']].values
BBCordY = df[['TopLeftCornerY']].values
BBLength = df[['Length']].values
BBHeight = df[['Height']].values

#------------------------------------------------------------------------------#
#     Define Image Processing Functions                                        #
#------------------------------------------------------------------------------#
def box(x, y, w, h, img):
  image = np.asarray(img).copy()
  x = int(x)
  y = int(y)
  w = int(w)
  h = int(h)
  for i in range(x, x+w, 1):
    for j in range(0, 5, 1):
      image[y+j-1][i] = (255, 0, 0)
  for i in range(x, x+w, 1):
    for j in range(0, 5, 1):
      image[y+h-j-1][i] = (255, 0, 0)
  for i in range(y, y+h, 1):
    for j in range(0, 5, 1):
      image[i][x+j-1] = (255, 0, 0)
  for i in range(y, y+h, 1):
    for j in range(0, 5, 1):
      image[i][x+w-j-1] = (255, 0, 0)
  return image

def boxGreen(x, y, w, h, img):
  image = np.asarray(img).copy()
  x = int(x)
  y = int(y)
  w = int(w)
  h = int(h)
  for i in range(x, x+w, 1):
    for j in range(0, 2, 1):
      image[y+j-1][i] = (0, 255, 0)
  for i in range(x, x+w, 1):
    for j in range(0, 2, 1):
      image[y+h-j-1][i] = (0, 255, 0)
  for i in range(y, y+h, 1):
    for j in range(0, 2, 1):
      image[i][x+j-1] = (0, 255, 0)
  for i in range(y, y+h, 1):
    for j in range(0, 2, 1):
      image[i][x+w-j-1] = (0, 255, 0)
  return image

def boxYellow(x, y, w, h, img):
  image = np.asarray(img).copy()
  x = int(x)
  y = int(y)
  w = int(w)
  h = int(h)
  for i in range(x, x+w, 1):
    for j in range(0, 5, 1):
      image[y+j-1][i] = (255, 255, 0)
  for i in range(x, x+w, 1):
    for j in range(0, 5, 1):
      image[y+h-j-1][i] = (255, 255, 0)
  for i in range(y, y+h, 1):
    for j in range(0, 5, 1):
      image[i][x+j-1] = (255, 255, 0)
  for i in range(y, y+h, 1):
    for j in range(0, 5, 1):
      image[i][x+w-j-1] = (255, 255, 0)
  return image

def crossHeir(x, y, w, h, img):
  image = np.asarray(img).copy()
  x = int(x)
  y = int(y)
  w = int(w)
  h = int(h)
  for i in range(y-int(h/2), y+int(h/2), 1):
    for j in range(x-2, x+2, 1):
      image[i][j] = (255, 255, 0)
  for i in range(x-int(w/2), x+int(w/2), 1):
    for j in range(y-2, y+2, 1):
      image[j][i] = (255, 255, 0)
  return image

def snip(x, y, w, h, image):
  x = int(x)
  y = int(y)
  w = int(w)
  h = int(h)
  snippet = []
  for i in range(y, y+h-1, 1):
    snippet.append(image[i][x:x+w])
  return np.asarray(snippet)

def pathImage(num):
  path = "/content/drive/MyDrive/ColabStuff/ET Landing/render/render"
  numLen = len(str(num));
  zeroNum = 4-numLen;
  zeroPrefix = ""
  for j in range(0, zeroNum, 1):
    zeroPrefix += "0"
  path = path + zeroPrefix + str(num) + ".png"
  return path

#------------------------------------------------------------------------------#
#  Put reshaped positive trains into variable                                  #
#------------------------------------------------------------------------------#
positive_train = []

for i in range(0, 5000, 1):
  curImg = np.asarray((Image.open(pathImage(BBFrame[i][0])))).copy()
  snippet = Image.fromarray(snip(BBCordX[i], BBCordY[i], BBLength[i], BBHeight[i], curImg)).resize((55,43))
  positive_train.append(snippet)
  print(i)
 
#------------------------------------------------------------------------------#
#  Put reshaped negative trains into variable                                  #
#------------------------------------------------------------------------------#

def isRock(x, y, num):
  path = "/content/drive/MyDrive/ColabStuff/ET Landing/images/clean/clean"
  numLen = len(str(num));
  zeroNum = 4-numLen;
  zeroPrefix = ""
  for j in range(0, zeroNum, 1):
    zeroPrefix += "0"
  path = path + zeroPrefix + str(num) + ".png"
  heatmap = np.asarray(Image.open(path))
  totalRock = 0
  for i in range(x, x+55, 1):
    for j in range(y, y+44, 1):
      if(heatmap[j][i][2] == 255 or heatmap[j][i][1] == 255):
        totalRock += 1
      if(totalRock == 40):
        return False
  return True

negative_train = []

for i in range(0, 5000, 1):
  print(i)
  randX = random.randint(0, 650)
  randY = random.randint(0, 400)
  if(isRock(randX, randY, BBFrame[i][0])):
    curImg = np.asarray((Image.open(pathImage(BBFrame[i][0])))).copy()
    snippet = Image.fromarray(snip(randX, randY, 55, 44, curImg))
    negative_train.append(snippet)
  else:
    randX = random.randint(0, 650)
    randY = random.randint(0, 400)
    if(isRock(randX, randY, BBFrame[i][0])):
      curImg = np.asarray((Image.open(pathImage(BBFrame[i][0])))).copy()
      snippet = Image.fromarray(snip(randX, randY, 55, 44, curImg))
      negative_train.append(snippet)
  print(i)
  
train_images = []
train_outputs = []

positiveNum = 0
negativeNum = 0

for i in range(0, len(negative_train) + len(positive_train)-1, 1):
  pick = random.randint(0,1)

  if(negativeNum < len(negative_train) and positiveNum < len(positive_train)):
    if(pick == 0):
      train_images.append(np.asarray(negative_train[negativeNum]))
      train_outputs.append(0)
      negativeNum += 1
    if(pick == 1):
      train_images.append(np.asarray(positive_train[positiveNum]))
      train_outputs.append(1)
      positiveNum += 1
  if(negativeNum >= len(negative_train) and positiveNum < len(positive_train)):
    train_images.append(np.asarray(positive_train[positiveNum]))
    train_outputs.append(1)
    positiveNum += 1
  if(negativeNum < len(negative_train) and positiveNum >= len(positive_train)):
    train_images.append(np.asarray(negative_train[negativeNum]))
    train_outputs.append(0)
    negativeNum += 1
  if(negativeNum >= len(negative_train) and positiveNum >= len(positive_train)):
    break;
      
train_images = np.asarray(train_images)
train_outputs = np.asarray(train_outputs)

model = keras.models.Sequential()
model.add(keras.layers.Conv2D(64,(1,1),activation='relu',input_shape=(55,43,3)))
model.add(keras.layers.Conv2D(32,(3,3),activation='relu'))
model.add(keras.layers.Conv2D(32,(3,3),activation='relu'))
model.add(keras.layers.Dense(32,activation='relu'))
model.add(keras.layers.Conv2D(32,(3,3),activation='relu'))
model.add(keras.layers.Conv2D(32,(3,3),activation='relu'))
model.add(keras.layers.Dense(32,activation='relu'))
model.add(keras.layers.MaxPooling2D((2,2)))
model.add(keras.layers.MaxPooling2D((2,2)))
model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(32,activation='relu'))
model.add(keras.layers.Dense(16,activation='relu'))
model.add(keras.layers.Dense(1,activation='sigmoid'))

model.compile(loss="mean_squared_error",optimizer=keras.optimizers.Adam())
model.fit(train_images, train_outputs, batch_size=100, epochs=20)

image = np.asarray(Image.open("/content/drive/MyDrive/ColabStuff/ET Landing/render/render0004.png")).copy()
boxArray = []
for y in range(0, image.shape[0]-100, 20):
  for x in range(0, image.shape[1]-100, 20):
    snippet = []
    snippet.append(np.asarray(Image.fromarray(snip(x, y, 100, 100, image)).resize((55, 43))))
    snippet = np.asarray(snippet)
    curConf = model.predict(snippet)[0][0]
    if(curConf >= 0.90):
      boxArray.append([x, y, 5, 5])
      print(curConf)

for y in range(0, image.shape[0]-50, 20):
  for x in range(0, image.shape[1]-100, 20):
    snippet = []
    snippet.append(np.asarray(Image.fromarray(snip(x, y, 100, 50, image)).resize((55, 43))))
    snippet = np.asarray(snippet)
    curConf = model.predict(snippet)[0][0]
    if(curConf >= 0.90):
      boxArray.append([x+50, y+25, 5, 5])
      print(curConf)

for y in range(0, image.shape[0]-100, 20):
  for x in range(0, image.shape[1]-100, 20):
    snippet = []
    snippet.append(np.asarray(Image.fromarray(snip(x, y, 100, 100, image)).resize((55, 43))))
    snippet = np.asarray(snippet)
    curConf = model.predict(snippet)[0][0]
    if(curConf >= 0.90):
      boxArray.append([x+50, y+50, 5, 5])
      print(curConf)

for y in range(0, image.shape[0]-100, 20):
  for x in range(0, image.shape[1]-50, 20):
    snippet = []
    snippet.append(np.asarray(Image.fromarray(snip(x, y, 50, 100, image)).resize((55, 43))))
    snippet = np.asarray(snippet)
    curConf = model.predict(snippet)[0][0]
    if(curConf >= 0.90):
      boxArray.append([x+25, y+50, 5, 5])
      print(curConf)

for y in range(0, image.shape[0]-50, 20):
  for x in range(0, image.shape[1]-50, 20):
    snippet = []
    snippet.append(np.asarray(Image.fromarray(snip(x, y, 50, 50, image)).resize((55, 43))))
    snippet = np.asarray(snippet)
    curConf = model.predict(snippet)[0][0]
    if(curConf >= 0.90):
      boxArray.append([x+25, y+25, 5, 5])
      print(curConf)

for i in boxArray:
  image = box(i[0], i[1], i[2], i[3], image).copy();
plt.imshow(image)

rocketRadius = 100

selectDistance = 1000
selectX = 0
selectY = 0
for y in range(0, len(image), 20):
  for x in range(0, len(image[0]), 20):
    minDistance = 1000
    for i in boxArray:
      y1 = i[1]
      x1 = i[0]
      distance = math.sqrt((y-y1) * (y-y1) + (x-x1) * (x-x1))
      if(distance < minDistance):
        minDistance = distance
    if(minDistance+20 > rocketRadius):
      image = boxGreen(x, y, 20, 20, image).copy()
      midDistance = math.sqrt((len(image)/2-y) * (len(image)/2-y) + (len(image[0])/2-x) * (len(image[0])/2-x))
      if(midDistance < selectDistance):
        selectDistance = midDistance
        selectX = x
        selectY = y
        print(selectX, selectY, selectDistance)

image = crossHeir(len(image[0])/2, len(image)/2, 50, 50, image).copy()

minDistance = 1000
minInd = 0
counter = 0
for i in boxArray:
  y1 = i[1]
  x1 = i[0]
  distance = math.sqrt((len(image[1])/2-y1) * (len(image[1])/2-y1) + (len(image[0])/2-x1) * (len(image[0])/2-x1))
  if(distance < minDistance):
    minDistance = distance
    minInd = counter
  counter += 1

image = boxYellow(selectX, selectY, 20, 20, image).copy()
plt.imshow(image)
