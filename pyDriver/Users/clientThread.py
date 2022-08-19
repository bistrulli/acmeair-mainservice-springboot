import requests as req
import numpy as np
import time
from threading import Thread
from pymongo import MongoClient
import pymongo



class clientThread(Thread):
    
    i=0
    toStop=False
    id=None
    mongoClient=None
    
    ttime=None
    delays=[]
    
    def __init__(self,ttime=1000.0):
        Thread.__init__(self)
        self.ttime=ttime
        self.id=clientThread.i
        clientThread.i+=1
        self.mongoClient=MongoClient("mongodb://localhost:27017/")
        
    
    def run(self):
        ms1Obj=self.mongoClient["sys"]["ms"].find_one({"name":"ms1"})
        ms2Obj=self.mongoClient["sys"]["ms"].find_one({"name":"ms2"})
        
        
        while(not clientThread.toStop):
            try:
                st = time.time_ns() // 1_000_000 
                
                d = np.random.exponential(scale=self.ttime)
    
                time.sleep(d/1000.0)
                
                resp=req.get('http://localhost:%d/'%(ms1Obj["prxPort"]))
                if(resp.status_code!=200):
                    raise ValueError("Error while connecting to %s with code %d and message %s"%(ms1Obj["name"],resp.status_code,resp.text))
                
                resp=req.get('http://localhost:%d/'%(ms2Obj["prxPort"]))
                if(resp.status_code!=200):
                    raise ValueError("Error while connecting to %s with code %d and message %s"%(ms2Obj["name"],resp.status_code,resp.text))
                
                # end= time.time_ns() // 1_000_000
                # self.mongoClient["client"]["rt"].insert_one({"st":st,"end":end})
            except:
                #print(self.id,"error")
                pass
    
    