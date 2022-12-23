FROM python:3.9.0
COPY cnnmodel /opt/cnnmodel
RUN mkdir /opt/image
RUN mkdir /opt/image/class
COPY main.py /opt/main.py
RUN python3 -m pip install  tensorflow==2.8.2 tensorflow_datasets==4.6.0
#tensorflow==2.8.2, numpy==1.23.1 , tensorflow_datasets==4.6.0, imageio==2.19.3
    
WORKDIR /opt
