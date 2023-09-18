class NewAccount:
    def __init__(self,name,email,password ):
        self.name=name
        self.email=email
        self.__password=password
        for i in newaccounts:
            if i =="name":
                newaccounts[i]=name
            if i=="email":
                newaccounts[i]=email
            if i=="password":
                newaccounts[i]=password        
    def setpassword(self,newpass):
        self.__password=newpass  
    def getpassword(self):
        return self.__password
    def __str__(self):
        return f"your name is : {self.name},your email is : {self.email}, your password is : {self.getpassword()}"   
class Jobs()  : 
    def __init__(self,name,email,age,adress,height,weight,carrier,phonenumber,chronicdiseases,var1):
        self.name=name
        self.email=email
        self.age=age
        self.adress=adress
        self.height=height
        self.weight=float(weight)
        self.carrier=carrier
        self.phonenumber=phonenumber
        self.chronicdiseases=chronicdiseases
        self.var1=var1                    
        

        if self.weight <40 or self.weight >140:
            print('Sorry, you do not meet the conditions')
        if int(self.age)>60 :
            print('Sorry, you do not meet the conditions')  
    def __str__(self):
        return f' name : {self.name}, age : {self.age}, email : {self.email}, adress : {self.adress}, height is : {self.height} ,\
weight :{self.weight}, careier :{self.carrier} , phone number : {self.phonenumber}, chronic diseases: {self.chronicdiseases},Permanent type {self.var1} '        
    
Investmentcorporate={'name':"",'email':""}
lowercost=['5m','6m','7m','8m','9m']
largestcost=['10m','11m','12m','13m','14m','15m']
class Investment :
    def __init__(self,namecompany,Companyemail,cost):
        self.namecompany=namecompany
        self.emailcompany=Companyemail
        self.cost=cost
        for i in Investmentcorporate:
            if i =='name':
                Investmentcorporate['name']=self.namecompany
            if  i =='email':
                Investmentcorporate['email']=self.emailcompany       
        if self.cost<=90000:
            print('Spaces available for this investment : ')
            print(lowercost)
        if self.cost>=100000:
            print('Spaces available for this investment : ')
            print(largestcost) 
        print('Half the amount is paid every six months . ')  
    def __str__(self):
        return f'your company name is {self.namecompany}, company email is {self.emailcompany}, and cost is {self.cost}' 
    
class PurchaseGoods :
    
    def __init__(self,name,phonenumber,producttype,productweight):
        self.name=name
        self.phonenumber=phonenumber
        self.producttype=producttype
        self.productweight=productweight
        if self.productweight < 30000:
            print('Sorry, the quantity is small')   
        else:
            print('We will contact you soon') 
class Employees():
    def printInformation(x=0):
        for i in employees:
            print(i, " : " +employees[i])
        print('Do you want to modify any of the data? ') 
        change=input('yes or no : ')
        if change =='yes':
            for i in employees:
                print(i) 
            change2=input('what is the data do you need to change :  ') 
            if change2=='name':
                employees['name']=input('enter the new name : ')
            if change2=="email":
                employees['email']=input('enter the new email : ') 
            if change2=='age':
                employees['age'] =input('enter the new age : ')
            if change2=='adress':
                employees['adress']=input('enter the new adress : ')    
            if change2=='height':
                employees['height']=input('enter the new heigt : ') 
            if change2=='weight' :
                employees['weight']=input('enter the new weight : ')
            if change2=='phone number':
                employees['phone number']=input('enter the new phone number : ')
            else:
                print('You cannot modify this information')    
        print(employees)
                               
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< main code :  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Here we find all the list and dictionary used
suggestions=[]
carriers=["A- Data scientist","B- Software developer","C- Loading and unloading corge","D- accounting and finance","E- Arrange the goods","F- electrician","G- sanitation worker"]   
chronic_diseases=['1- Heart disease','2- Cancer','3- Stroke','4- Diabetes','5- Kidney disease']
newaccounts={"name":"","email":"","password":""}
employees={"name":"",'email':"","age":"",'adress':"",'height':"","weight":"",'carrier':"","phone number":"","chronicdiseases":"",'Permanent type':""}
# ------------------------------------------------------------------------------
print("Do you have an account with us?")
print()
choose=input("please choose yes or no  : ")
print()
if choose=="no":
    name=input("enter your name : ")
    var1=1                           #var1 and var2 They are two variables in order to verify the email
    var2=2
    while var1<var2:
        email=input("enter your email : ")
        for i in range(len(email)):
            if email[i]=="@":
                var1+=1 
                break                         
    print('Your password must consist of at least eight characters . ')
    total=0                         # it is variable to sum how many character in password
    var3=1                          #var3 and var4 They are two variables in order to verify the password
    var4=2
    while var3<var4:
        password=input('enter your password : ')   
        for i in range(len(password)):
            total+=1
        if total<8:
            print('wrong input .')
            var3+=1
            var4+=1
        else:
            var3+=1
            break
    newacc=NewAccount(name,email,password)
    print(newacc)  
print("<<<<<<<<<<<<<<<<<<<<<<<  complate account  >>>>>>>>>>>>>>>>>>>>>>>>>>") 
for i in range(10):     
    print("What services do you want?")
    print('1-Job search')
    print('2-Investment')
    print('3-Purchase Goods')
    print('4-employee')
    print('5-problems and suggestions')
    print('*'*60)
    schoos2=int(input('Type the service number you want : '))
    if schoos2==1 :
        name=input("enter your name : ")
        c=1                      # c and v They are two variables in order to verify the email
        v=2
        while c<v:
            email=input("enter your email : ")
            for i in range(len(email)):
                if email[i]=="@":
                    c+=1 
                    break
        age=input('enter your age : ')
        adress=input('enter your adress : ')
        height=input('enter your height  : ')
        weight=input('enter your weight : ')
        carrier =''
        for i in carriers:
            print(i)
        character=input('Enter your specialty code : ')
        if character=='A':
            carrier='Data scientist'
        elif character=='B':
            carrier='Software developer'
        elif   character=='C':
            carrier ='Loading and unloading corge'
        elif character=='D':
            carrier ='accounting and finance'
        elif character=='E':
            carrier ='Arrange the goods'
        elif character=='F':
            carrier ='electrician'
        elif character=='G':
            carrier ='sanitation worker'
        else:
           print('wrong input')
        print(carrier)   
        phonenumber=input('enter your phone number : ')
        print()
        chronicdiseases=input('Do you have any serious chronic diseases? Answer yes or no :')
        if chronicdiseases=='yes' or chronicdiseases=='Yes':
                print(chronic_diseases)
                for i  in chronic_diseases:
                    print(i)
                print('Do you have any of these diseases?')    
                choose5=input('enter yes or no : ')
                if choose5=='yes':
                    print('We are sorry')
                    break
        var1=" full time "                  #It is a variable to determine full-time or part-time
        fulltime=input('full time input yes or no :')
        if fulltime =='yes':
            print('Monthly Salary is 500 JD')
            var1='full time'
        else:
            print('She works part-time and will take up to an hour 2JD')
            var1='part time '           
        print('We look forward to seeing you soon .')            
        staff1=Jobs(name,email,age,adress,height,weight,carrier,phonenumber,chronicdiseases,var1)
        print(staff1)
        for i in employees:
            if i=='name':
                employees[i]=name
            elif i=='email':
                employees[i]=email
            elif i=='age':
                employees[i]=age
            elif i=='adress':
                employees[i]=adress
            elif i=="height":
                employees[i]=height
            elif i=="weight":
                employees[i]=weight
            elif i=="carrier":
                employees[i]=carrier
            elif i=="phone number":
                employees[i]=phonenumber
            elif i=="chronicdiseases":
                employees[i]=chronicdiseases
            elif i =="Permanent type" :
                employees[i]=var1  
        print('*'*60)       
    if schoos2==2:
        companyname=input('write company name  : ')
        c=1                                      #  c and v They are two variables in order to verify the email
        v=2
        while c<v:
            Companyemail=input('write company email : ')
            for i in range(len(email)):
                if email[i]=="@":
                    c+=1 
                    break
        cost=int(input('enter your cost : '))
        investment=Investment(companyname,Companyemail,cost)
        print(investment)
    if schoos2==3:
        print('This system supports the gross domestic product by purchasing vegetables and fruits from citizens .')
        name=input('entar your name : ')
        phonenumber=input('enter your phone number :')
        producttype=input('enter product type : ')
        productweight=int(input('enter product weight : '))
        PurchaseGoods1=PurchaseGoods(name,phonenumber,producttype,productweight)
        print(PurchaseGoods1)
        print('*'*60)  
    if schoos2==4:
        name=input('entar your name : ') 
        email=input('enter your email : ')
        password=input('enter your password : ')
        if newaccounts['name']==name:
            print('ture')
        if newaccounts['email']==email :
            staff2=Employees()
            staff2.printInformation()
        print('*'*60)               
    if schoos2==5:
           print('This system is for problems and suggestions')
           name=input('enetr your name : ')
           Suggestions1=input('enter your problems or suggestions ')
           suggestions.append(Suggestions1)
           print(suggestions)
           print('*'*60)

#<<<<<<<<<<<<<<<<<<<<the end >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>           



    





