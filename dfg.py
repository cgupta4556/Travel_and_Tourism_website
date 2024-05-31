try:

    import datetime
    def gettime():
        return datetime.datetime.now()
    def look (k):
        z=1
        while(z!=0):
            if k==1:
                c= int(input("enter 1 for excerise or 2 for food"))
                if c==1: 
                    value= input("write here  ")
                    with open ("ayush.txt food","a") as f:
                        f.write(str([str(gettime())]) + ":" + value + "\n")
                        print("write successfully")
                elif c==2:
                    value= input("write here  ")
                    with open ("ayush.txt excerise","a") as f:
                        f.write(str([str(gettime())]) + ":" + value + "\n")
                        print("write successfully")
            elif k==2:
                c= int(input("enter 1 for excerise or 2 for food"))
                if c==1: 
                    value= input("write here  ")
                    with open ("piyush.txt food","a") as f:
                        f.write(str([str(gettime())]) + ":" + value + "\n")
                        print("write successfully")
                elif c==2:
                    value= input("write here  ") 
                    with open ("piyush.txt excerise","a") as f:
                        f.write(str([str(gettime())]) + ":" + value + "\n")
                        print("write successfully")
            elif k==3:
                c= int(input("enter 1 for excerise or 2 for food"))
                if c==1: 
                    value= input("write here  ")
                    with open ("ashish.txt food","a") as f:
                        f.write(str([str(gettime())]) + ":"+ value + "\n")
                        print("write successfully")                   
                if c==2:
                    value= input("write here  ")
                    with open ("ashish.txt excerise","a") as f:
                        f.write(str([str(gettime())]) +":" + value + "\n")
                        print("write successfully")
                
            else:
                print("please enter valid input")        
                k=input("u write some more say 1 for yes or n for 0")
                # continue
    def reterive(k):
        if k==1:
            c= int(input("enter 1for food and 2 for excerise "))
            if c==1:
                with open ("ayush.txt food ") as f:
                    for i in f:
                        print( i, end=" ")
            elif c==2:
                with open ("ayush.text excerise") as f:
                    for i in f:
                        print(i , end="")
        elif k==2:
            c= int(input("enter 1for food and 2 for excerise "))
            if c==1:
                with open ("piyush.txt food ") as f:
                    for i in f:
                        print( i, end=" ")                                           
            elif c==2:
                with open ("piyush.txt food ") as f:
                    for i in f:
                        print(i, end="")
        elif k==3:
            c= int(input("enter 1for food and 2 for excerise "))
            if c==1:
                with open ("ashish.txt food ") as f:
                    for i in f:
                        print(i, end="")
            elif c==2:
                with open ("ashish.txt excerise ") as f:
                    for i in f:
                        print(i, end="")
        else:
            print("please enter valid input ")
            

    print( "HEALTH MANAGEMENT SYSTEM FOR COVID 19" )
    a=int(input("press 1 for look and 2 for retrieve  "))            
    if a==1:
        b=int(input("press 1 for ayush ,2 for piyush ,3 for ashish"))
        look(b)
    else:
        b=int(input("press 1 for ayush ,2 for piyush ,3 for ashish"))
        reterive(b)
except Exception as e:
    print(e)
                           

    