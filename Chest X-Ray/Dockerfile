FROM python:3.9.0
COPY cnnmodel /opt/cnnmodel
RUN mkdir /opt/image
RUN mkdir /opt/image/class
COPY main.py /opt/main.py
RUN pip install --no-cache-dir tensorflow  tensorflow_datasets 
#tensorflow==12.8.2, numpy==1.23.1 , tensorflow_datasets==4.6.0, imageio==2.19.3
    
WORKDIR /opt
