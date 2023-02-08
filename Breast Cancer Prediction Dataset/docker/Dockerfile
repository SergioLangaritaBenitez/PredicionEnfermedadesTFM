FROM python:3.9
COPY json_data.json /opt/json_data.json
COPY Pickle_RL_Model.pkl /opt/Pickle_RL_Model.pkl
COPY main.py /opt/main.py
RUN apt-get update
RUN apt-get install -y python3 python3-pip
RUN pip3 install pandas==1.4.3 sklearn==0.0
ENTRYPOINT ["python3","/opt/main.py","--input","/opt/input.json","--output","/opt/result.txt"]
