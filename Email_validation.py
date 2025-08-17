email = input("enter your email:")
k,j,d=0,0,0
if len(email)>=6:
    if email[0].isalpha(): #isalpha checks the 0th index is alphabet or not.
        if ("@"in email) and (email.count("@")==1):
            if(email[-4]==".")^(email[-3]=="."): 
                   # here we use XOR(^) operator because we want either 1st or 2nd condition it give true but if both condition apply it give false.
                   # we didnt use or operator coz if both cond fulfill it give true, result in use "." in both indexes, whic we dont want.
                for i in email:
                    if i.isspace():
                        k=1
                    elif i.isalpha():
                        if i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1
                if k==1 or j==1 or d==1:
                    print("wrong email 5")
                else:
                    print("right email")
            else:
                print("wrong email 4")
        else:
            print("wrong email 3")
    else:
        print("wrong email 2")
else:
    print("wrong email 1")