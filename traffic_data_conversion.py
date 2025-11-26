traffic_logs = [
"id:501,zone:A1,vehicle:Car,speed:62,time:08:30,violations:[None],status:Smooth",
"id:502,zone:A1,vehicle:Bike,speed:85,time:09:10,violations:[Helmet],status:Busy",
"id:503,zone:B2,vehicle:Bus,speed:45,time:17:25,violations:[None],status:Smooth",
"id:504,zone:C3,vehicle:Car,speed:110,time:14:15,violations:[Overspeed],status:Congested",
"id:505,zone:A1,vehicle:Truck,speed:40,time:18:50,violations:[None],status:Smooth",
]
def convert(traffic_logs):
    result=[]
    for data in traffic_logs:
        items=data.split(',')
        traffic={}
        for item in items:
            key,value=item.split(':',1) #split only at first
            key=key.strip() #to remove any extra spaces
            value=value.strip()
            if key=="id" or key=="speed":
                  value=int(value) #convert into integer for furture calculation
            elif key=="violations":
                value=value.strip("[]") #remove [] from start and end only
                value=value.split()#split values at blank spaces
                value=[v.strip().strip(',') for v in value]#
            traffic[key]=value
        result.append(traffic)
    return result
result=convert(traffic_logs)
print(result)
