'''
Created on 19 ago 2022

@author: emilio
'''

import json
import numpy as np
import time
import datetime

from Users.clientThread import clientThread
import requests

if __name__ == '__main__':
    # istanzio il workload
    # nuser=1
    # users=[]
    # for i in range(nuser):
    #     users.append(clientThread())
    
    s = requests.Session() 
    
    # come primo workload eseguo login/view_profile/update_profile
    # come workload finale eseguo un untete che con una certa probabilita 
        # login
        # modifica il suo profilo
        # cerca un volo esistente 
            # con prob p1
                # fa il booking di quel volo (Devo cancellare il booking? forse si per coerenza)
            # con prob 1-p1
            # torna alla ricerca
    
    # login
    # data to be sent to api
    # estraggo un progilo random da visualizzare e aggiornare in base a quelli disponibili
    data = {"login":"uid0@email.com",
            "password":"password"}
    
    st = time.time()
    r = s.post(url="http://localhost:80/auth/login", data=data)
    # print("login time %f"%(time.time()-st))
    print(r.text)
    
    # view profile
    st = time.time()
    r = s.get(url="http://localhost/customer/byid/%s" % (data["login"]), data={})
    print('view profile resp', r.text)
    # print("view profile time %f"%(time.time()-st))
    userData = json.loads(r.text);
    
    # update profile
    number = "".join(map(str, np.random.randint(low=0, high=9, size=9)))
    userData["phoneNumber"] = number
    userData["password"] = data["password"];
    st = time.time()
    r = s.post(url="http://localhost/customer/byid/%s" % (data["login"]), headers={"Content-Type": "application/json;"},
             json=userData)
    print("update profile resp", r.text)
    
    # print("update profile time %f"%(time.time()-st))
    userData = json.loads(r.text);
    
    # view profile
    st = time.time()
    r = s.get(url="http://localhost/customer/byid/%s" % (data["login"]), data={})
    # print("view profile time %f"%(time.time()-st))
    userData = json.loads(r.text);
    print("view2 progile", userData)
    
    if(not userData["phoneNumber"] == number):
        raise ValueError("number not saved successfully")
    
    # query flight
    queryData = {"fromAirport": "FCO",
                "toAirport": "LHR",
                "fromDate": "Tue Sep 13 2022 00:00:00 GMT+0200 (Ora legale dell’Europa centrale)",
                "returnDate": "Tue Sep 13 2022 00:00:00 GMT+0200 (Ora legale dell’Europa centrale)",
                "oneWay": False}
    r = s.post(url="http://localhost/flight/queryflights", data=queryData)

    flightData = json.loads(r.text);
    print(flightData)
    
    toFlight=flightData["tripFlights"][0]["flightsOptions"][0]
    retFlight=flightData["tripFlights"][1]["flightsOptions"][0]
                          
    # book flight
    bookData = {
              "userid": userData["_id"],
              "toFlightId": toFlight["_id"],
              "toFlightSegId": toFlight["flightSegmentId"],
              "retFlightId": retFlight["_id"],
              "retFlightSegId": retFlight["flightSegmentId"],
              "oneWayFlight": False
        }
    
    print(bookData)
    
    # cancel booking
    
    s.close()
        
