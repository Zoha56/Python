def Student_dic(stu_list):
    result=[]
    for student in stu_list:
        try:
            student=student.split(',')
            stu_dic={}
            for stu in student:
                    key,value=stu.split(':')
                    key=key.sript()
                    value=value.sript()
                    if key in ('marks','attendance'):
                               value=int(value)
                    stu_dic[key]=value
            result.append(stu_dic)
        except ValueError as e: 
            print(f"Error occur in{'record'}:Invalid format({e})")
        except KeyError as e:
            print(f"Error occur in {'record'}:Invalid key({e})")
        except Exception as e:
            print(f"Unknown error ({e})")
      
    return result
def average(result):
    sum=0
    for student in result:
        sum+=student['marks']
    average=sum/len(result)
    return average
def highestmarks(result):
    Name=None
    highest=0
    for student in result:
        if student['marks']>highest:
            highest=student['marks']
            Name=student['name']
    return highest,Name
def above90(result):
    ans=set()
    for student in result:
        if student['marks']>90:
            ans.append(student['name'])
    return ans
def filter_student(result):
    list1=list(filter(lambda stu: stu['marks']>=50 , result))
    return list
def des_sort(result):
     list1=sorted(result , key=lambda stu: stu['marks'], reverse=True)
     return list1
def shoppingcart():
      cart=[]
      while True:
        n=int(input("enter 1 to add,2 to remove , 3 to update and 4 to calculate invoice"))
        if(n==1):
          cart_item={}
          cart_item["name"]=input("enter name of item")
          cart_item["price"]=int(input("enter price:"))
          cart_item["quantity"]=int(input("enter quantity:"))
          cart.append(cart_item)
        elif n==2:
            itemname=input("enter name of the item you want to remove")
            for i in cart:
                if i["name"]==itemname:
                    cart.remove(i)
            else:
                print("item is not in the list")
        elif n==3:
             itemname=input("enter name of the item you want to update")
             for i in cart:
                if i["name"]==itemname:
                     i["price"]=int(input("enter price:"))
                     i["quantity"]=int(input("enter quantity:"))
             else:
                 print("item is not in the list")
        elif n==4:
            print("your cart is ",cart)
            Total=sum(p['price']*p['quantity'] for p in cart)
            Expensive=max(cart , key=lambda item:item['price']*item['quantity'])
            print("Total bill is ",Total)
            print("Most Expensive item is",Expensive['price']*Expensive['quantity'])
            break
        else:
            print("invalid choice")
shoppingcart()
