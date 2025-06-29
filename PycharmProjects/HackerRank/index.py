
def validate_pin(pin):
    if pin.isdigit() and (len(pin) == 4 or len(pin) == 6):
        print("pin gecerlidir")
    else : print ("gecersiz pin")
    
validate_pin("454546")