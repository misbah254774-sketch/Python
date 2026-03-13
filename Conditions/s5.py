def weather_condition():
    while True:
        try:
            weather =str(input("enter weather condition :--")).lower()
            if weather =="exit":
                break
            elif weather == "sunny":
                print("go for induction program as there is ac installed ")
            elif weather =="Rainy":
                print("eat pakoda ")
            elif weather == "snowy":
                print("swim in a near by pond ")
            else:
                print("enter exact weather condition ")
        except ValueError:
            print("are you an idiot enter correct condition")
            
            
a= weather_condition()
