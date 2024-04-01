import datetime
now =datetime.datetime.now()
print("current date and time:")
print(now.strftime("%y-%m-%d %H:%M:%S "))
fname=input("Input your first name :")
lname=input("input your second name : ")
print("Hello" +lname+ ""+ fname)
