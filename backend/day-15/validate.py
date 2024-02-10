import re  

def email(email):
    try:
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):  
            return email
        else:
            raise TypeError()
    except TypeError:
        print("Invalid email! Please try again!")
        exit()
        
def boolean():
    print("boolean validation")