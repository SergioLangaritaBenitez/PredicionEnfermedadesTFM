import gradio as gr
import base64
import requests
#from minio import Minio
import os
import zipfile
import json 
import oscar_python
import boto3
import uuid

class gradiooscar:
    def __init__(self, endpoint, user, password,ssl):
        self.endpoint=endpoint
        self.user=user
        self.password=password
        self.ssl=ssl
        x=self.basicRequest("/system/config")
        
        if x.status_code == 200:
            self.login=True
            response=json.loads(x.text)
            client=response["minio_provider"]
            #print(client)
            #print(client["endpoint"].split("//")[1])
            #print(client["access_key"])
            #print(client["secret_key"])
            self.minio=boto3.client('s3',
                            endpoint_url=client["endpoint"],
                            #region_name=c["region"],
                            verify=client['verify'],
                            aws_access_key_id=client["access_key"],
                            aws_secret_access_key=client["secret_key"])
        else:
            self.login=False

    def getLogin(self):
        return self.login

    def basicRequest(self,path):
        url=self.endpoint+path
        as_bytes=bytes(self.user+":"+self.password,"utf-8")
        userAndPass = base64.b64encode(as_bytes).decode("utf-8")
        headers = {"Authorization": "Basic "+ userAndPass}
        x = requests.get(url, headers=headers , verify=self.ssl)
        return x


    def get_token(self,servicename):
        x=self.basicRequest("/system/services")
        result=json.loads(x.text)
        for service in result:
            if service["name"] == servicename:
                return service["token"]
        return None 


    def callAsync(self,data,bucket,input,output):
        id=str(uuid.uuid4())
        self.minio.upload_file(data, bucket, input+"/"+id)
        waiter = self.minio.get_waiter('object_exists')
        waiter.wait(Bucket=bucket, Key = output+"/"+id+".txt")

        self.minio.download_file(bucket,output+'/'+id+".txt", id+".txt")
        f=open(id+".txt", "r") 
        result=f.read()
        os.remove(id+".txt")
        return result

    def call2Async(self,data,bucket,input,output,ext):
        id=str(uuid.uuid4())
        self.minio.upload_file(data, bucket, input+"/"+id)

        waiter = self.minio.get_waiter('object_exists')

        waiter.wait(Bucket=bucket, Key = output[0]+"/"+id+ext[0])
        self.minio.download_file(bucket,output[0]+'/'+id+ext[0], id+ext[0])
        
        with zipfile.ZipFile(id+ext[0], 'r') as zip_ref:
            zip_ref.extractall(".")
        os.remove(id+ext[0])

        waiter.wait(Bucket=bucket, Key = output[1]+"/"+id+ext[1])
        self.minio.download_file(bucket,output[1]+'/'+id+ext[1], id+ext[1])
        f=open(id+ext[1], "r") 
        result=f.read()
        os.remove(id+ext[1])

        return result


    def bearerRequest(self,servicename,data):
        token=self.get_token(servicename)
        url=self.endpoint+"/run/"+servicename
        headers = {"Authorization": "Bearer "+str(token)}
        x = requests.post(url, headers=headers, data = data, verify=self.ssl)
        return x
