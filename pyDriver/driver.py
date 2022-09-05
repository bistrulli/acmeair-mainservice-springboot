'''
Created on 19 ago 2022

@author: emilio
'''

import json
import numpy as np
import time


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
    #estraggo un progilo random da visualizzare e aggiornare in base a quelli disponibili
    data = {"login":"uid0@email.com",
            "password":"password"}
    
    st=time.time()
    r = s.post(url="http://localhost:80/auth/login",data=data)
    print("login time %f"%(time.time()-st))
    
    #view profile
    st=time.time()
    r=s.get(url="http://localhost/customer/byid/%s"%(data["login"]),data={})
    print("view profile time %f"%(time.time()-st))
    userData=json.loads(r.text);
    
    #update profile
    number="".join(map(str,np.random.randint(low=0,high=9,size=9)))
    userData["phoneNumber"]=number
    userData["password"]=data["password"];
    st=time.time()
    r=s.post(url="http://localhost/customer/byid/%s"%(data["login"]),headers={"Content-Type": "application/json; charset=utf-8"},
             json=userData)
    print("update profile time %f"%(time.time()-st))
    userData=json.loads(r.text);
    
    #view profile
    st=time.time()
    r=s.get(url="http://localhost/customer/byid/%s"%(data["login"]),data={})
    print("view profile time %f"%(time.time()-st))
    userData=json.loads(r.text);
    
    if(not userData["phoneNumber"]==number):
        raise ValueError("number not saved successfully")
    
    #studio meglio il comportamento inteno e preparo l'applicazione per essere eseguita nel mio framework. Posso sostituire il mio proxy 
    #con ha proxy?
    
    
    
    
        
