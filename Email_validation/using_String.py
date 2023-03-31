email = input("Enter your email address : \n")
# to make a valid email atleast minimum 6 charactersare required ->a@g.com
#There can only be one @ symbol, No spacing 
if (len(email) >= 6) :
    
    if(email[0].isalpha()):
        if ( "@" in email ) and (email.count("@") == 1):
            if(email[-4] == ".") ^ (email[-3] == "."): # ^ is XOR operator -> any one should be rue
                for i in range(len(email)):
                    if(email[i] == " "):
                        print("Wrong email address because of space")
                    else:
                        print("Valid Email")
                        break
            else:
                print("Email wrong"   )
        else:
            print("Wrong email address because of @ ")
            
    else:
        print("Please enter a valid email ")

        
else:
    print("Please enter a valid email address")