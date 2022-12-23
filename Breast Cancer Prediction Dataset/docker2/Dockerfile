FROM ubuntu:20.04
COPY graph.py /opt/graph.py
COPY input.json /opt/input.json
COPY Breast_cancer_data.csv /opt/Breast_cancer_data.csv
RUN apt-get update
RUN apt-get install -y python3 python3-pip zip
RUN  pip3 install pandas==1.4.3 matplotlib==3.5.2
ENTRYPOINT ["python3","/opt/graph.py","--input","/opt/input.json"]
