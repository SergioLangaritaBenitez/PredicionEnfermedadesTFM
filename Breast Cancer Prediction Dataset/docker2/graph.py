import pandas as pd
import matplotlib.pyplot as plt
import os
import argparse
import json


parser = argparse.ArgumentParser()
parser.add_argument('--input','--data')
input_arg=parser.parse_args()

if os.path.exists(input_arg.input):
    text = open(input_arg.input, "r").read()
    #print(type(text))
    data=json.loads(text)
    #print(data)
    df = pd.read_csv('/opt/Breast_cancer_data.csv')
    plt.plot(df.mean_radius[df.diagnosis==1], df.mean_texture[df.diagnosis==1], 'o',color="red")
    plt.plot(df.mean_radius[df.diagnosis==0], df.mean_texture[df.diagnosis==0], 'o',color="green")
    plt.plot(data["mean_radius"], data["mean_texture"], 'o',color="black")

    plt.xlabel('mean radius')
    plt.ylabel('mean texture')
    plt.savefig('picture1.png')
    plt.clf()

    plt.plot(df.mean_radius[df.diagnosis==1], df.mean_smoothness[df.diagnosis==1], 'o',color="red")
    plt.plot(df.mean_radius[df.diagnosis==0], df.mean_smoothness[df.diagnosis==0], 'o',color="green")
    plt.plot(data["mean_radius"], data["mean_smoothness"], 'o',color="black")
    plt.xlabel('mean radius')
    plt.ylabel('mean smoothness')
    
    plt.savefig('picture2.png')

    plt.clf()
    plt.plot(df.mean_texture[df.diagnosis==1], df.mean_smoothness[df.diagnosis==1], 'o',color="red")
    plt.plot(df.mean_texture[df.diagnosis==0], df.mean_smoothness[df.diagnosis==0], 'o',color="green")
    plt.plot(data["mean_texture"], data["mean_smoothness"], 'o',color="black")
    plt.xlabel('mean mean_texture')
    plt.ylabel('mean smoothness')
    plt.savefig('picture3.png')
