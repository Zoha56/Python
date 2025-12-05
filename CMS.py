from asyncio import Handle


students_data = [ 
"id:101,name:Ali,dept:CS,attendance:88,marks:[80,75,90],feedback:Excellent", 
"id:102,name:Sara,dept:IT,attendance:72,marks:[60,65,58],feedback:Helpful", 
"id:103,name:Hamza,dept:CS,attendance:95,marks:[90,92,88],feedback:Very Good", 
"id:104,name:Maryam,dept:Math,attendance:67,marks:[55,60,50],feedback:Average", 
"id:105,name:Usman,dept:IT,attendance:85,marks:[70,68,72],feedback:Helpful" 
]
def convert(students_data):
   try:
    result=[]
    for data in students_data:
        students={}
        student=data.split(',')
        for item in student:
            if ':' not in item:  # skip malformed items
                continue
            key,value=item.split(':',1)
            key=key.strip()
            value=value.strip()
            if key=="id" or key=="attendance":
               value=int(value)
            elif key == "marks":
                value = value.strip('[]')
                value = [int(v.strip()) for v in value.split(',')]
            students[key]=value
        result.append(students)
   except Exception as e:
       print(f"Error in record ",e)
   return result
      
converted=convert(students_data)
for student in converted:
    print(student)
def average_attendance(converted):
    average={}
    department_count={}
    attendance_sum={}
    for student in converted:
        dep=student.get('dept')
        attend=student.get('attendance')
        if dep is None or attend is None:
            continue
        if not dep in attendance_sum:
            attendance_sum[dep]=attend
            department_count[dep]=1
        else:
            attendance_sum[dep]+=attend
            department_count[dep]+=1
    for dep in attendance_sum:
        average[dep]=attendance_sum[dep]/department_count[dep]
    return average
print(average_attendance(converted))
def low_attendance(converted):
    names=[]
    for student in converted:
        attendance=student.get('attendance')
        if attendance<75:
            names.append(student['name'])
    return names
print(low_attendance(converted))