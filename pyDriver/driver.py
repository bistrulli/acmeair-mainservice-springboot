'''
Created on 19 ago 2022

@author: emilio
'''

import json

from Users.clientThread import clientThread
import requests

if __name__ == '__main__':
    # istanzio il workload
    # nuser=1
    # users=[]
    # for i in range(nuser):
    #     users.append(clientThread())
    
    
    s = requests.Session() 
    
    #come primo workload eseguo login/view_profile/update_profile
    #come workload finale eseguo un untete che con una certa probabilita 
        #modifica il suo profilo
        #cerca un volo
        #con un altra probailita 
            #fa il booking di quel volo (fatto il booking abbandona il sito. Devo cancellare il booking? forse si per coerenza)
            #esegue una nuova ricerca
    
    
    #login
    # data to be sent to api
    data = {"login":"uid0@email.com",
            "password":"password"}
    r = s.post(url="http://localhost:80/auth/login",data=data)
    print(r.text)
    
    #view profile
    r=s.get(url="http://localhost/customer/byid/%s"%(data["login"]),data={})
    userData=json.loads(r.text);
    print(userData)
    userData["phoneNumber"]="086326284"
    
    #update profile
    userData["password"]=data["password"];
    r=s.post(url="http://localhost/customer/byid/%s"%(data["login"]),headers={"Content-Type": "application/json; charset=utf-8"},
             json=userData)
    print(r.status_code)
    
    
        
