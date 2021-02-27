import keras
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import time
import numpy as np
import random

imgArr = []
imgAns = []

def pathAirplane(num):
  path = "/content/drive/MyDrive/ColabStuff/natural_images/airplane/"
  numLen = len(str(num));
  zeroNum = 4-numLen;
  zeroPrefix = ""
  for j in range(0, zeroNum, 1):
    zeroPrefix += "0"
  path = path + "airplane_" + zeroPrefix + str(num) + ".jpg"
  return path

def pathCar(num):
  path = "/content/drive/MyDrive/ColabStuff/natural_images/car/"
  numLen = len(str(num));
  zeroNum = 4-numLen;
  zeroPrefix = ""
  for j in range(0, zeroNum, 1):
    zeroPrefix += "0"
  path = path + "car_" + zeroPrefix + str(num) + ".jpg"
  return path

def pathCat(num):
  path = "/content/drive/MyDrive/ColabStuff/natural_images/cat/"
  numLen = len(str(num));
  zeroNum = 4-numLen;
  zeroPrefix = ""
  for j in range(0, zeroNum, 1):
    zeroPrefix += "0"
  path = path + "cat_" + zeroPrefix + str(num) + ".jpg"
  return path

def pathDog(num):
  path = "/content/drive/MyDrive/ColabStuff/natural_images/dog/"
  numLen = len(str(num));
  zeroNum = 4-numLen;
  zeroPrefix = ""
  for j in range(0, zeroNum, 1):
    zeroPrefix += "0"
  path = path + "dog_" + zeroPrefix + str(num) + ".jpg"
  return path

def pathFlower(num):
  path = "/content/drive/MyDrive/ColabStuff/natural_images/flower/"
  numLen = len(str(num));
  zeroNum = 4-numLen;
  zeroPrefix = ""
  for j in range(0, zeroNum, 1):
    zeroPrefix += "0"
  path = path + "flower_" + zeroPrefix + str(num) + ".jpg"
  return path

def pathFruit(num):
  path = "/content/drive/MyDrive/ColabStuff/natural_images/fruit/"
  numLen = len(str(num));
  zeroNum = 4-numLen;
  zeroPrefix = ""
  for j in range(0, zeroNum, 1):
    zeroPrefix += "0"
  path = path + "fruit_" + zeroPrefix + str(num) + ".jpg"
  return path

def pathMotorbike(num):
  path = "/content/drive/MyDrive/ColabStuff/natural_images/motorbike/"
  numLen = len(str(num));
  zeroNum = 4-numLen;
  zeroPrefix = ""
  for j in range(0, zeroNum, 1):
    zeroPrefix += "0"
  path = path + "motorbike_" + zeroPrefix + str(num) + ".jpg"
  return path

def pathPerson(num):
  path = "/content/drive/MyDrive/ColabStuff/natural_images/person/"
  numLen = len(str(num));
  zeroNum = 4-numLen;
  zeroPrefix = ""
  for j in range(0, zeroNum, 1):
    zeroPrefix += "0"
  path = path + "person_" + zeroPrefix + str(num) + ".jpg"
  return path


for i in range(0, 700, 1):
  print(i)
  imgArr.append(np.asarray(Image.open(pathAirplane(i)).resize((150,150), Image.ANTIALIAS)).copy())
  imgAns.append(np.asarray([1, 0, 0, 0, 0, 0, 0, 0]))
  imgArr.append(np.asarray(Image.open(pathCar(i)).resize((150,150), Image.ANTIALIAS)).copy())
  imgAns.append(np.asarray([0, 1, 0, 0, 0, 0, 0, 0]))
  imgArr.append(np.asarray(Image.open(pathCat(i)).resize((150,150), Image.ANTIALIAS)).copy())
  imgAns.append(np.asarray([0, 0, 1, 0, 0, 0, 0, 0]))
  imgArr.append(np.asarray(Image.open(pathDog(i)).resize((150,150), Image.ANTIALIAS)).copy())
  imgAns.append(np.asarray([0, 0, 0, 1, 0, 0, 0, 0]))
  imgArr.append(np.asarray(Image.open(pathFlower(i)).resize((150,150), Image.ANTIALIAS)).copy())
  imgAns.append(np.asarray([0, 0, 0, 0, 1, 0, 0, 0]))
  imgArr.append(np.asarray(Image.open(pathFruit(i)).resize((150,150), Image.ANTIALIAS)).copy())
  imgAns.append(np.asarray([0, 0, 0, 0, 0, 1, 0, 0]))
  imgArr.append(np.asarray(Image.open(pathMotorbike(i)).resize((150,150), Image.ANTIALIAS)).copy())
  imgAns.append(np.asarray([0, 0, 0, 0, 0, 0, 1, 0]))
  imgArr.append(np.asarray(Image.open(pathPerson(i)).resize((150,150), Image.ANTIALIAS)).copy())
  imgAns.append(np.asarray([0, 0, 0, 0, 0, 0, 0, 1]))
  
imgArr = np.asarray(imgArr)
imgAns = np.asarray(imgAns)

print(type(imgArr))
print(type(imgAns))

model = keras.models.Sequential()
model.add(keras.layers.Conv2D(32,(3,3),activation='relu',input_shape=(150,150,3)))
model.add(keras.layers.MaxPooling2D((2,2)))
model.add(keras.layers.Conv2D(64,(3,3),activation='relu'))
model.add(keras.layers.MaxPooling2D((2,2)))
model.add(keras.layers.Conv2D(128,(3,3),activation='relu'))
model.add(keras.layers.MaxPooling2D((2,2)))
model.add(keras.layers.Conv2D(128,(3,3),activation='relu'))
model.add(keras.layers.MaxPooling2D((2,2)))
model.add(keras.layers.Flatten())
model.add(keras.layers.Dropout(0.5))
model.add(keras.layers.Dense(512,activation='relu'))
model.add(keras.layers.Dense(8,activation='softmax'))


model.compile(loss="categorical_crossentropy",optimizer=keras.optimizers.Adam(),metrics=['acc'])
model.fit(imgArr, imgAns, batch_size=5, epochs=64)

model = keras.models.load_model('/content/drive/MyDrive/ColabStuff')

def predict(img):
  image = img.copy()
  plt.imshow(image)
  test_data = np.asarray([image])
  confidence = np.array(model.predict(test_data, batch_size=1))
  max = 0
  maxInd = 0
  outSay = ["AIRPLANE", "CAR", "CAT", "DOG", "FLOWER", "FRUIT", "MOTORBIKE", "HUMAN"]
  for i in range(0, 8, 1):
    if(confidence[0][i] > max):
      max = confidence[0][i]
      maxInd = i
  return confidence[0]

def box(x, y, w, h, img):
  image = img.copy()
  for i in range(x, x+w, 1):
    for j in range(0, 5, 1):
      image[y+j][i] = (255, 0, 0)
  for i in range(x, x+w, 1):
    for j in range(0, 5, 1):
      image[y+h-j][i] = (255, 0, 0)
  for i in range(y, y+h, 1):
    for j in range(0, 5, 1):
      image[i][x+j] = (255, 0, 0)
  for i in range(y, y+h, 1):
    for j in range(0, 5, 1):
      image[i][x+w-j] = (255, 0, 0)
  return image

def snip(x, y, img):
  snippet = []
  for i in range(y, y+150, 1):
    snippet.append(img[i][x:x+150])
  
  return np.asarray(snippet)

image = np.asarray(Image.open("/image/you/want/to/process").copy())
boxArray = []
for y in range(0, image.shape[0]-150, 20):
  for x in range(0, image.shape[1]-150, 20):
    print(x, y)
    curConf = predict(snip(x, y, image))
    if(curConf[7] >= 0.80):
      print("==============================================")
      print("X= " + str(x) + " Y= " + str(y))
      print("Airplane  = " + str(curConf[0]))
      print("Car       = " + str(curConf[1]))
      print("Cat       = " + str(curConf[2]))
      print("Dog       = " + str(curConf[3]))
      print("Flower    = " + str(curConf[4]))
      print("Fruit     = " + str(curConf[5]))
      print("Motorbike = " + str(curConf[6]))
      print("Person    = " + str(curConf[7]))
      print("==============================================")
      boxArray.append([x, y])

for i in boxArray:
  image = box(i[0], i[1], 150, 150, image).copy();
plt.imshow(image)
