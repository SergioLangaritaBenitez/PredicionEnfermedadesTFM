#!/usr/bin/env python3
from tensorflow import keras
import tensorflow as tf
import tensorflow_datasets as tfds
import sys


def imagetofile(folder):
 	batch_size2 = 4
 	img_height = 128
 	img_width = 128
 	train_ds= tf.keras.utils.image_dataset_from_directory(folder, seed=123, shuffle=False, image_size=(img_height, img_width),batch_size=batch_size2) 
 	x_train =None 
 	for image, label in tfds.as_numpy(train_ds):
 		x_train = image
 	x_train = x_train.astype('float32') / 255.0
 	return x_train



def evaluate(model,image):
	prediction_raw=model.predict(image,batch_size=2)
	prediction=prediction_raw.argmax(axis=1)
	probabilities="Mild Demented: " + str(prediction_raw[0][0])+"\n"
	probabilities+="Moderate Demented: " + str(prediction_raw[0][1])+"\n"
	probabilities+="Non Demented: " + str(prediction_raw[0][2])+"\n"
	probabilities+="Very Mild Demented: " + str(prediction_raw[0][3])+"\n"
	result=prediction[0]
	if(prediction[0]==0):
		result="Mild Demented"
	elif(prediction[0]==1):
		result="Moderate Demented"
	elif(prediction[0]==2):
		result="Non Demented"
	elif(prediction[0]==3):
		result="Very Mild Demented" 
	ret=probabilities+"\nPrediction:"+result+"\n"
	return ret
	
	
model = keras.models.load_model('cnnmodel')
image5=imagetofile('/opt/image')
result=evaluate(model,image5)

f = open(str(sys.argv[1])+".txt", "w")
f.write(str(result))
f.close()
