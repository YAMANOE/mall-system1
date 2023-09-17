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
        return f"your name is {self.name},your email is {self.email}"
    
carriers=[" Data scientist"," Software developer"," Loading and unloading corge"," accounting and finance"," Arrange the goods"," electrician","sanitation worker"]   
chronic_diseases=['1- Heart disease','2- Cancer','3- Stroke','4- Diabetes','5- Kidney disease']
class Jobs()  : 
    def __init__(self,name,email,age,adress,height,weight,carrier,phonenumber,chronicdiseases):
        self.name=name
        self.email=email
        self.age=int(age)
        self.adress=adress
        self.height=height
        self.weight=float(weight)
        self.carrier=carrier
        self.phonenumber=phonenumber
        self.chronicdiseases=chronicdiseases
        if self.weight <40 or self.weight >140:
            print('Sorry, you do not meet the conditions')
        if self.age>60 :
            print('Sorry, you do not meet the conditions')  
    def __str__(self):
        return f' name : {self.name}, age : {self.age}, email : {self.email}, adress : {self.adress}, height is : {self.height} , weight :{self.weight}, careier :{self.carrier} , phone number : {self.phonenumber},chronic diseases: {self.chronicdiseases}'        

class Employees():
    def __init__(self,sectionwork,fulltime,parttime):
        self.sectionwork=sectionwork
        self.fulltime=fulltime
        self.parttime=parttime    
    def __str__(self):
        return f' sectionwork : {self.sectionwork}, full time : {self.fulltime},part time : {self.parttime }'
     
Investmentcorporate={'name':"",'email':""}
lowercost=['5m','6m','7m','8m','9m']
largestcost=['10m','11m','12m','13m','14m','15m']
class Investment :
    def __init__(self,namecompany,emailcompany,cost):
        self.namecompany=namecompany
        self.emailcompany=emailcompany
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
# class              

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< main code :  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>


c=1
v=2

total=0
print("Do you have an account with us?")
choose=input("please choose yes or no  : ")
newaccounts={"name":"","email":"","password":""}
employees={"name":"",'email':"","age":"",'adress':"",'height':"","weight":"","carrier":"","phonenumber":"","chronicdiseases":"","sectionwork":"","fulltime":"","parttime":""}
if choose=="no":
    name=input("enter your name : ")
    while c<v:
        email=input("enter your email : ")
        for i in range(len(email)):
            if email[i]!='@':
                print('wrong input .')
                c+=1
                v+=1
        break                       
    print('Your password must consist of at least eight characters . ')    
    password=input('enter your password : ')
    for i in range(len(password)):
        total+=1
        if total<8:
            print('wrong input .')
            break
        newacc=NewAccount(name,email,password)  
        print("<<<<<<  complate account  >>>>>>") 
    for i in range(10):     
        print("What services do you want?")
        print('1-Job search')
        print('2-Investment')
        print('3-Purchase Goods')
        print('4-employee')
        schoos2=int(input('Type the service number you want : '))
        if schoos2==1 :
             name=input("enter your name : ")
             email=input("enter your email : ")
             age=input('enter your age : ')
             adress=input('enter your adress : ')
             height=input('enter your height  : ')
             weight=input('enter your weight : ')
             print(carriers) 
             carrier=input('Write your specialty as it appears in front of you : ')
             phonenumber=input('enter your phonenumber : ')
             chronicdiseases=input('Do you have any serious chronic diseases? Answer yes or no :')
             if chronicdiseases=='yes' or chronicdiseases=='Yes':
                 print(chronic_diseases)
                 choose5=input('Do you have any of these diseases?,enter yes or no : ')
                 if choose5=='yes':
                     print('We are sorry')
                     continue    
             print('We look forward to seeing you soon .')            
             staff1=Jobs(name,email,age,adress,height,weight,carrier,phonenumber,chronicdiseases)
             print(staff1)
             for i in employees:
                if i=='name':
                    employees[i]=name
                if i=='email':
                    employees[i]=email
                if i=='password' :
                    employees[i]=password
                if i=='age':
                    employees[i]==age
                if i=='adress':
                    employees[i]=adress
                if i=="height":
                    employees[i]=height
                if i=="weight":
                    employees[i]=weight
                if i=="carrier":
                    employees[i]==carrier
                if i=="phonenumber":
                    employees[i]=phonenumber
                if i=="chronicdiseases":
                    employees[i]=chronicdiseases    
             if schoos2==4:
                sectionwork=input('enter the sectinwork : ')
                fulltime=input('full time input yes or no :')
                parttime=input(' part time input yes or no :')
                if fulltime=="yes":
                     print('Monthly Salary is 500 JD')
                else :
                     print('She works part-time and will take up to an hour 2JD')
                for i in employees:
                    if i=="sectionwork":
                        employees[i]=sectionwork
                    if i =="fulltime" :
                        employees[i]==fulltime
                    if i=='part time':
                        employees[i]==parttime 
                    print(employees)          
        if schoos2==2:
             companyname=input('write company name  : ')
             emailcompany=input('write company email : ')
             cost=int(input('enter your cost : '))
             investment=Investment(companyname,emailcompany,cost)
             print(investment)
        if schoos2==3:
             print('This system supports the gross domestic product by purchasing vegetables and fruits from citizens .')
             name=input('entar your name : ')
             phonenumber=input('enter your phone number :')
             producttype=input('enter product type : ')
             productweight=int(input('enter product weight : '))
             PurchaseGoods1=PurchaseGoods(name,phonenumber,producttype,productweight)
             print(PurchaseGoods1)
    





