FROM python:3.8
RUN pip install gradio minio oscar-python
COPY gradio_oscar.py /opt/gradio_oscar.py
COPY main.py /opt/main.py
COPY mild_2.jpg /opt/mild_2.jpg
COPY moderate_19.jpg /opt/moderate_19.jpg
COPY non_73.jpg /opt/non_73.jpg
COPY NORMAL.jpeg /opt/NORMAL.jpeg
COPY COVID19.jpeg /opt/COVID19.jpeg
COPY Pneumonia.jpeg /opt/Pneumonia.jpeg
COPY Tuberculosis.png /opt/Tuberculosis.png
COPY verymild_216.jpg /opt/verymild_216.jpg
ENTRYPOINT ["python3","/opt/main.py"]
