import gradio as gr
import base64
import os
import zipfile
from gradio_oscar import gradiooscar
from oscar_python.client import Client


baseurl=os.environ['oscar_endpoint']
ssl= False   
pre ="/opt/"
port=int(os.environ['port'])

def authorization(login, password):
    global gro 
    global client
    client = Client("cluster-id",baseurl, login, password, False)
    gro = gradiooscar(baseurl,login,password,ssl)
    return gro.getLogin()

def parseResult(result):
    firstsplit=result.split("\n")
    dictionary={}
    for n in range(0,4):
        secondsplit=firstsplit[n].split(":")
        dictionary[secondsplit[0]]=secondsplit[1]
    #print(str(result).split("\n")  )
    label=firstsplit[5].split(":")[1]
    return dictionary,label


def radiografiaAsync(image):
    response=gro.callAsync(image,"chestray","input","output")
    return parseResult(response)




def rmiAsync(image):
    response=gro.callAsync(image,"alzheimer","input","output")

    return parseResult(response)


def bcdAsync(mean_radius,mean_texture,mean_smoothness):
    data='{"mean_radius": ['+mean_radius+'],\n\t\t"mean_texture": ['+mean_texture+'],\n\t\t"mean_primeter": [186.9],\n\t\t"mean_area": [2501.0],\n\t\t"mean_smoothness": ['+mean_smoothness+']}'
    f = open("myfile.txt", "w") 
    f.write(data)
    f.close()
    result=gro.call2Async("myfile.txt","bcp","input",["output/grap","output/model"],[".zip",".txt"])
    os.remove("myfile.txt")
    return result,"picture1.png","picture2.png","picture3.png"





with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            img1 = gr.Image(type="filepath")
            inbtw1 = gr.Button("Process X-Ray image" )
            #inbtw2 = gr.Button("Process X-Ray image Sync")
        examples=gr.Examples([pre+"NORMAL.jpeg",pre+"COVID19.jpeg",pre+"Pneumonia.jpeg",pre+"Tuberculosis.png"], img1) 
        label1=gr.Label(num_top_classes=4)
        textbox1=gr.Textbox(label="Prediction")
        inbtw1.click(fn=radiografiaAsync,
                inputs=img1,
                outputs=[label1,textbox1])
        #inbtw2.click(fn=radiografiaSync,
        #        inputs=img1,
        #        outputs=[label1,textbox1])
    with gr.Row():
        with gr.Column():
            img2 = gr.Image(type="filepath",)
            inbtalz1 = gr.Button("Detection of Alzheimer")
            #inbtalz2 = gr.Button("Detection of Alzheimer Sync")
        examples2=gr.Examples([pre+"mild_2.jpg",pre+"moderate_19.jpg",pre+"non_73.jpg",pre+"verymild_216.jpg"], img2)
        label2=gr.Label(num_top_classes=4)
        textbox2=gr.Textbox(label="Prediction")
        inbtalz1.click(fn=rmiAsync,
                inputs=img2,
                outputs=[label2,textbox2])
        #inbtalz2.click(fn=rmiSync,
        #        inputs=img2,
        #        outputs=[label2,textbox2])


    with gr.Row():
        with gr.Column():
            mean_radius = gr.Textbox(label="Mean Radius")
            mean_texture = gr.Textbox(label="Mean Texture")
            mean_smoothness = gr.Textbox(label="Mean Smoothness")
            inbtw3 = gr.Button("Breast Cancer Detection")
        textbox3=gr.Textbox(label="Prediction")
    with gr.Row():
        img1 = gr.Image(type="filepath")
        img2 = gr.Image(type="filepath")
        img3 = gr.Image(type="filepath")

        inbtw3.click(fn=bcdAsync,
                inputs= [mean_radius,mean_texture,mean_smoothness],
                outputs=[textbox3,img1,img2,img3])            
demo.launch(server_name="0.0.0.0",server_port=port,auth=authorization)
