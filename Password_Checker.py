def Check(password):
    score=0
    advice=""
    if len(password)>12:
        score+=1
    else:
        advice+="Try having more than 12 characters.\n"  
    d={"UpperCase":0,"LowerCase":0,"Digits":0,"SpecialCharacters":0}
    for i in password:
        if i.isupper():
            d["UpperCase"]+=1
        if i.islower():
            d["LowerCase"]+=1
        if i.isdigit():
            d["Digits"]+=1
        if i.isalnum()==False:
            d["SpecialCharacters"]+=1
    for i in d:
        if d[i]>0:
            score+=1
        elif i=="UpperCase":
            advice+="Try having more uppercase letters.\n"
        elif i=="LowerCase":
            advice+="Try having more lowercase letters.\n"
        elif i=="Digits":
            advice+="Try having more numbers.\n"
        elif i=="SpecialCharacters":
            advice+="Try having more special characters.\n"
    return (score,advice)
    

def Remarks(score,advice):
    print("Your score is",str(score*20)+"/100")
    if score<5:
        print("Please do the following to make the password better: ")
        print(advice)
    else:
        print("Excellent password!!!") 
          
    
    
    
    