def get_leap_year():
    while True:
        try :
            leap_year= int(input("enter the year:--"))
            if leap_year%4==0 and leap_year%100!=0:
                print(" a leap year ")
            
                
            else:
                print("not a leap year")
        except ValueError:
            print("enter year in integer")
        
  
  

a = get_leap_year()




