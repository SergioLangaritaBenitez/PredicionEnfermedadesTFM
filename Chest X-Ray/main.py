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
 	train_label=None
 	for image, label in tfds.as_numpy(train_ds):
 		x_train = image
 	x_train = x_train.astype('float32') / 255.0
 	return x_train



def evaluate(model,image):
	prediction_raw=model.predict(image,batch_size=2)
	prediction=prediction_raw.argmax(axis=1)
	probabilities="COVID-19: " + str(prediction_raw[0][0])+"\n"
	probabilities+="NORMAL: " + str(prediction_raw[0][1])+"\n"
	probabilities+="PNEUMONIA: " + str(prediction_raw[0][2])+"\n"
	probabilities+="TUBERCULOSIS: " + str(prediction_raw[0][3])+"\n"
	result=prediction[0]
	if(prediction[0]==0):
		result="COVID-19"
	elif(prediction[0]==1):
		result="NORMAL"
	elif(prediction[0]==2):
		result="PNEUMONIA"
	elif(prediction[0]==3):
		result="TUBERCULOSIS"
	ret=probabilities+"\nPrediction:"+result+"\n"
	return ret
	
model = keras.models.load_model('cnnmodel')
image5=imagetofile('/opt/image')



result=evaluate(model,image5)
f = open(str(sys.argv[1])+".txt", "w")
f.write(result)
f.close()
