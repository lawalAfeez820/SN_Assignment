



import time
saver=[] #to save some value in the card_validation function
#luhn algorithm
""" card_validation function is to check if  the\
16 digit of  the atm card is correct    """
def card_validation(card_number):
    
    if len(card_number)==16 and card_number.isdigit():     
        
        for i in range(0,16,2):
           b=int((card_number)[i])*2
           if len(str(b))==2:
                  
               c=int(str(b)[0]) + int(str(b)[1])
               saver.append(c)
           else:
               saver.append(b)
        for i in range(1,15,2):
            saver.append(card_number[i])
            
        converter=[int(i) for i in saver]
        total=sum(converter)%10
        
        
        if (10-total)==int(card_number[-1]):
            return True
        else:
            return False
        
    else:
         return False



print("WELCOME TO K & K SUPERMARKET".center(60)    )   #name of the supermarket


"""  card _details is confirm the payment ,only the 16 digit of atm card
if entered wrongly it cause reccursion of this function.
so make sure the 16 digit is a correct atm digit(NO DEBIT TRANSACTION
WILL OCCUR IN YOUR ACCOUNT)"""
count=0
def card_details():
    
    card_type=["master card","verve"]
    the_type=input("ENTER YOUR CARD TYPE (master card or verve):   ")
    card_number=input("ENTER YOUR VALID 16-digit CARD NUMBER:  ")
    cvv=input("ENTER CVV(3-digit):  ")
    date=input("ENTER THE EXPIRY DATE OF YOUR CARD (in the form   mm/yy):  ")
    
    if (the_type.lower() in card_type) and\
    (len(cvv) ==3 and cvv.isdigit()) and card_validation(card_number) and len(date)==5:
        print("\n")
        print("please wait")
        time.sleep(5)
        print("\n")
        
        return "PAYMENT SUCCESSFUL"
    
    
    else:
         global count
         count+=1
         print("\n")
         print("please wait")
         time.sleep(5)
         print("\n")
         print("ONE(S0ME) OF THE ENTERED DETAILS IS NOT CORRECT")
         print("PLEASE MAKE SURE YOUR 16-DIGIT CARD NUMBER IS A VALID ONE")
         print("\n")
         time.sleep(2)
         if count<3:
             return card_details()
         else:
            return "TRY AGAIN LATER"
    
    

""" the variable item is the item in the supermarket  """        
item={"BODY CREAM":"1500.75","CRAYON":"600.30","BREAD":"300.70",\
      "KNIFE":"800.08","CHOCOLATES":"400.04",\
      "DRINKS":"400.62","BODY SPRAYER":"2000.40","BICYCLE":"8000.54",\
      "ICE CREAM":"500.50","SHIRT":"25000.04"}
com=[i for i in item.keys()]

pick=[]
price=[]
units=[]

total=[]







def  receipt( ):
    
    print("K & K SUPERMARKET RECEIPT".center(58))

    
    print("\n")
    
    number=1
    
    for i,j,z in zip(pick,price,units):
      print(str(number).ljust(7),end=" ")
       
      number+=1
      print(f" {z} unit of {i} at #{j} each ")
      print("\n")
    print("TOTAL=".rjust(20),"#",format( sum(total),".2f"))
        
       




def items():
    n=1
    for i in item.keys():
        if  len(str(n))==1:
         print(n, i.rjust(len(i)+10))
        else:
            print(n,i.rjust(len(i)+8))
        n+=1
print("\n")
        
      
x="yes"
n=0

while x=="yes":
    if n>=1:
        x=input("SHOW YOU THE SUPERMARKET LIST AGAIN ?(YES OR NO):  ").lower()
        
    else:
        x=input("SHOW YOU THE SUPERMARKET LIST ?(YES OR NO):  ").lower()
        
     
    if x== "yes":
        print( "please wait")
         
        time.sleep(3),
        items()
        
        j=(input("SELECT AN OPTION (BETWEEN 1-10):  "))
        if j.isdigit():
            j=int(j)
            pick.append(com[j-1])
            price.append(item[com[j-1]])
        else:
            print("YOU HAVE ENTERED A WOUNG INPUT.....please try again later")
            break
            
        unit=(input(f"HOW MANY UNIT OF {com[j-1]} DO YOU WANT:  "))
        if unit.isdigit():
            unit=int(unit)
            units.append(unit)
            print("\n")
            print(f" {unit}-{com[j-1]}  has been selected")
            print("\n")
            total.append(float(price[n])*units[n])
            n+=1
        else:
             print("YOU HAVE ENTERED A WOUNG INPUT.....please try again later")
            
             break





    elif x=="no" :
        if n==0:
            print("THANKS")
            break
        else :
            print("\n")
            print("LOADING........")
            
            time.sleep(2)
            print("\n")
            cool=card_details()
            if cool=="TRY AGAIN LATER":
                print("TRY AGAIN LATER AS YOU HAVE TRIED TO \
INPUT YOUR CARD DETAILS THREE TIMES")
                break
            else:
                print("please wait, we are processing the receipt")
                print("\n")
                time.sleep(5)
                receipt()
                print("THANKS FOR USING THE SERVICES!!!")
                break
    else:   
        n=0
        x="yes"
        print("\n")
        time.sleep(1)
        print("YOU HAVE ENTERED WRONG COMMAND .YOU HAVE TO START YOUR ORDER AGAIN........")
        print("\n")
        time.sleep(2)
        continue
        








              
 

        

                  
            
            
            
