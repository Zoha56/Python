from unittest import result
def converts(emp_list):
    result=[]
    for employee in emp_list:
       try:
           items=employee.split(',')
           emp_dic={}
           for item in items:
                 key,value=item.split(':')
                 key = key.strip()
                 value = value.strip()
                 if key in ('salary','bonus'):
                      value=int(value)
                 emp_dic[key]=value
           result.append(emp_dic)
       except ValueError as e:
           print(f"Error found in {'record'}:Invalid format({e}) ")
       except KeyError as e:
           print(f"Error found in {'record'}:Missing key({e}) ")
       except Exception as e:
           print(f"Unexpected Error  in {'record'}:({e}) ")
    return result
def payroll(result):
    Total=0
    for i in result:
        Total+=i['salary']+i['bonus']
    return Total
def highest(result):
    Total=0
    high=0
    Name=None
    for employee in result:
        Total=employee['salary']+employee['bonus']
        if Total>high:
            high=Total
            Name=employee['name']
    return high,Name
def HR(result):
    Name=set()
    for employee in result:
        if employee['department']=='HR':
            Name.add(employee['name'])
    return Name
def highbonus(result):
    Name=list()
    for employee in result:
        if employee['bonus']>1500:
            Name.append(employee['name'])
    return Name
def filter_out(result):
     high= list(filter(lambda emp:emp['salary']+emp['bonus']>60000, result))
     return high
def sorted_emp(result):
    list1=sorted(result , key=lambda emp:len(emp['department']))
    return list1

emp_list=["employee_id:101,name:John,department:HR,salary:50000,bonus:10000","employee_id:102,name:Alex,department:Sales,salary:40000,bonus:4000",
          "employee_id:103,name:Smith,department:HR,salary:50000,bonus:20000"]
ans=converts(emp_list)
print(ans)
print(payroll(ans))
print(highest(ans))
print(HR(ans))
print(highbonus(ans))
print(filter_out(ans))
print(sorted_emp(ans))

