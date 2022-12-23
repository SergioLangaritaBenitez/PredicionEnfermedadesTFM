#!/usr/bin/env python3.9.0
import json
import pickle
import pandas as pd
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--input','--data')
parser.add_argument('--output')
input_arg=parser.parse_args()
if os.path.exists(input_arg.input):
	path="/opt/"
	text = open(input_arg.input, "r").read()
	data=json.loads(text)
	with open(path+'Pickle_RL_Model.pkl', 'rb') as file:  
	    Pickled_LR_Model = pickle.load(file)
	    
	with open(path+'json_data.json') as json_file:
	    numbers = json.load(json_file)

	dftry = pd.DataFrame(data)
	dftry["mean_radius"]=dftry["mean_radius"]/numbers["mean_radius"]
	dftry["mean_texture"]=dftry["mean_texture"]/numbers["mean_texture"]


	aux=dftry[["mean_radius", "mean_texture","mean_smoothness"]]
	
	Ypredict = Pickled_LR_Model.predict(aux)  
	#print("Predicion: "+str(Ypredict))
	#return Ypredict
	if(Ypredict[0] >= 0.5):
		resultado="Positive"
	else:
		resultado="Negative"
	print(Ypredict)
	print(resultado)
	f = open(input_arg.output, "w")
	f.write(resultado)
	f.close()
