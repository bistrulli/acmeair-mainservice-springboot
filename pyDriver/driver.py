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
    
    # {'tripFlights': [{'numPages': 1, 
    #                   'flightsOptions': [{'_id': 'fe3b5205-3119-4ed6-85ef-d96ec13f21d1', 
    #                   'firstClassBaseCost': 500, 'economyClassBaseCost': 200, 
    #                   'numFirstClassSeats': 10, 'numEconomyClassSeats': 200, 
    #                   'airplaneTypeId': 'B747', 'flightSegmentId': 'AA319', 
    #                   'scheduledDepartureTime': 'Tue Sep 13 00:00:00 CEST 2022', 
    #                   'scheduledArrivalTime': 'Tue Sep 13 01:29:00 CEST 2022', 
    #                   'flightSegment': {'_id': 'AA319', 'originPort': 'FCO', 'destPort': 'LHR', 'miles': 892}}], 
    #                   'currentPage': 0, 'hasMoreOptions': False, 'pageSize': 10}
                      
    # book flight
    bookData = {
              userid: userData["_id"],
              toFlightId: flightData['flightsOptions'][0]["_id"]],
              toFlightSegId: flightData['flightsOptions'][0]["flightSegmentId"]],
              retFlightId: "66560514 - b3d7 - 4f61 - 9386 - fea62c6c5613",
              retFlightSegId: "AA188",
              oneWayFlight: False
        }
    
    print(bookData)
    
    # cancel booking
    
    s.close()
        
