again=str(input("Do you want to Start or End? Type 'START' or 'END' respectively "))
while again != "END"  :
   chapter= int(input("\n\nWhich chapter do you want to work on? 1,2,3"))
   if int(chapter) == 1: 
        print("\n\nX , Y , α , KEx and KEy are ALWAYS positive while β is ALWAYS negative ")
        choice=int(input("\n\nWhat do you want to find? Type 1 for finding KEx and KEy, 2 for finding Y (using α,β,x), 3 for finding X (using α,β,y), 4 finding for α (using X,Y,β), 5 finding for β (using X,Y,α), or 6 to abort"))
        if choice == 1:
            x1 = float(input("How many units of product X are first being produced? "))
            x2 = float(input("How many units of procdut X are finally being produced?(Must be different from the 1st) "))
            y1 = float(input("How many units of product Y are first being produced? "))
            y2 = float(input("How many units of product Y are finally being produced?(Must be different from the 1st) "))
            Kex = abs((y1 - y2)/(x1 - x2))
            print("Kex =",Kex)
            Key = 1/Kex
            print("Key =",Key)
        elif choice == 2:
            a = float(input("How much is α(Always Positive)  "))
            b = float(input("How much is β(Always Negative)  "))
            x = float(input("How much is the value of X "))
            y = a + b*x
            print("Y =",y) 
        elif choice == 3:
            a = float(input("How much is α(Always Positive) "))
            b = float(input("How much is β(Always Negative) "))
            y = float(input("How much is the value of Y"))
            x = (y - a)/b
            print("X =",x)
        elif choice == 4:
            b = float(input("How much is β(Always Negative)  "))
            y= float(input("What is the value of Y"))
            x = float(input("How much is value of X "))
            a = y - b * x
            print("α =",a)
        elif choice == 5:
            a = float(input("How much is α(Always Positive) "))
            y= float(input("What is the value of Y"))
            x = float(input("How much is value of X "))
            b=(y-a)/x
            print("β =",b)
        elif choice== 6:
            print("Aborting....")
            print("In 3\n...2\n...1")
   elif chapter== 2:
        print("\n")
        print("Qd , P , α and Tc Are ALWAYS positive numbers while β is ALWAYS negative but E(d,y) or Arcuating Ed may be either negative or positive. P1 never has the same value as P2, if it does have the same value then the elasticity is ∞ \n\n")
        choice=int(input("What do you want to find?\n -1 for finding Ed using ΔQ/Q'%'/ΔP/P'%' , 0 for finding Ey usind ΔQ/Q'%'/Δy/y'%' 1 for Ed, 2 for Ey, 3 for Arcuating Elasticity\n 4 for finding Qd (using α,β,P), 5 for finding P (using α,β,Qd), 6 for finding α (using β,Qd,P), 7 for finding β (using α,Qd,P)\n 8 for finding Q1 using Q2,P1,P2,Ed, 9 for finding Q2 using Q1,P1,P2,Ed, 10 for finding P1 using Q1,Q2,P2,Ed, 11 for finding P2 using Q1,Q2,P1,Ed\n 12 for finding Tc using Qd and P, 13 for finding Qd using Tc and P, 14 for finding P using Qd , Tc\n 15 for '%' change of Qd, 16 for '%' change of P, 17 for '%' change of Tc"))
        if choice == -1:
            dq=float(input("What is the value of ΔQ/Q'%'"))
            dp=float(input("What is the value of ΔP/P'%'"))
            ed=dq/dp
            print("Ed =",ed)
        if choice == 0:
            dq=float(input("What is the value of ΔQ/Q'%'"))
            dy=float(input("What is the value of Δy/y'%'"))
            ey=dq/dy
            print("Ey =",ey)
        if choice== 1:
            qd1 = float(input("What is the 1st desired quantity?(Qd1) "))
            qd2 = float(input("What is the 2nd desired quantity?(Qd2) "))
            p1 = float(input("What is the 1st/Starting price?(P1) "))
            p2 = float(input("What is the 2nd/Final price?(P2) MUST BE DIFFERENT FROM THE 1st "))
            ed = ((qd2 -qd1)/(p2 - p1)) * (p1 / qd1)
            print(ed)
            if abs(float(ed)) == 1:
                print("Singular Elasticity")
            elif abs(float(ed)) > 1:
                print("Elastic Demand")
            elif abs(float(ed)) == 0:
                print("Absolute Anelastic Demand")
            elif abs(float(ed)) < 1:
                print("Anelastic Demand")
        elif choice == 2:
            qd1 = float(input("What is the 1st desired quantity?(Qd1) "))
            qd2 = float(input("What is the 2nd desired quantity?(Qd2) "))
            y1 = float(input("What is the 1st/Starting income?(Y1)"))
            y2 = float(input("What is the 2nd/Final income?(Y2) MUST BE DIFFERENT FROM THE 1st "))
            ey = ((qd2 - qd1) / (y2-y1)) * (y1 / qd1)
            print(ey)
            if ey >= 1:
                print("Normal Product")
            elif ey < 1:
                print("Inferior Product")
        elif choice == 3:
            qd1 = float(input("What is the 1st desired quantity?(Qd1) "))
            qd2 = float(input("What is the 2nd desired quantity?(Qd2) "))
            p1 = float(input("What is the 1st/Starting price?(P1) "))
            p2 = float(input("What is the 2nd/Final price?(P2) MUST BE DIFFERENT FROM THE 1st "))
            edac = ((qd2-qd1)/(p2-p1))*(p1+p2)/(qd1+qd2)
            print(edac)
            if abs(edac) == 1:
                print("Singular Elasticity")
            elif abs(edac) < 1:
                print("Elastic Demand")
            elif abs(edac) == 0:
                print("Absolute Anelastic Demand")
            elif abs(edac) < 1:
                print("Anelastic Demand")
        elif choice == 4:
            a = float(input("How much is α "))
            b = float(input("How much is β "))
            p = float(input("How much is the Price (P) "))
            qd = a+b*p
            print("Qd =",qd)
        elif choice == 5:
            a = float(input("How much is α "))
            b = float(input("How much is β "))
            qd= float(input("How much is the Desired Quantity (Qd)"))
            p = (qd-a)/b
            print("P =",p)
        elif choice == 6:
            b = float(input("How much is β(Always Negative)  "))
            qd= float(input("How much is the Desired Quantity (Qd)"))
            p = float(input("How much is the Price (P)"))
            a = qd - b * p
            print("α =",a)
        elif choice == 7:
            a = float(input("How much is α(Always Positive) "))
            qd= float(input("How much is the Desired Quantity (Qd)"))
            p = float(input("How much is the Price (P)"))
            b=(qd-a)/p
            print("β =",b)
        elif choice == 8:
            p1=float(input("What is the starting Price(P1)"))
            p2=float(input("What is the final Price(P2),(Must be different from the 1st"))
            q2=float(input("What is the final Desired Quantity (Qd2)"))
            ed=float(input("What is the Ed(Elastic Demand)"))
            dp=p2-p1
            qd1=(p1*q2)/(ed*dp+p1)
            print("Qd1 =",qd1)
        elif choice == 9:
            p1=float(input("What is the starting Price(P1)"))
            p2=float(input("What is the final Price(P2),(Must be different from the 1st"))
            q1=float(input("What is the starting Desired Quantity (Qd1)"))
            ed=float(input("What is the Ed(Elastic Demand)"))
            dp=p2-p1
            qd2=ed*(q1/p1)*(p2-q1)+q1
            print("Qd2 =",qd2)
        elif choice == 10:
            p2=float(input("What is the final Price(P2)"))
            q1=float(input("What is the starting Desired Quantity (Qd1)"))
            q2=float(input("What is the final Desired Quantity (Qd2)"))
            ed=float(input("What is the Ed(Elastic Demand)"))
            p1=(q1*ed*p2)/(q1*ed+q2-q1)
            print("P1 =",p1)
        elif choice == 11:
            p1=float(input("What is the starting Price(P1)"))
            q1=float(input("What is the starting Desired Quantity (Qd1)"))
            q2=float(input("What is the final Desired Quantity (Qd2)"))
            ed=float(input("What is the Ed(Elastic Demand)"))
            p2=p1+((q2-q1)*p1)/(ed*q1)
            print("P2 = ",p2)
        elif choice == 12:
            qd=float(input("What is the Desired Quantity(Qd)"))
            p= float(input("What is the Price(P)"))
            tc=qd*p
            print("Tc =",tc)
        elif choice == 13:
            p=float(input("What is the Price(P)"))
            tc=float(input("What is the Total Cost (Tc)"))
            qd=tc/p
            print("Qd =",qd)
        elif choice == 14:
            qd=float(input("What is the Desired Quantity (Qd)"))
            tc=float(input("What is the Total Cost (Tc)"))
            p=tc/qd
            print("P =",p)
        elif choice == 15:
            q1=float(input("What is the starting Q"))
            q2=float(input("What is the final Q"))
            c=(q2-q1)/q1
            print("Change =",c*100,"%")
        elif choice == 16:
            p1=float(input("What is the starting Price (P)"))
            p2=float(input("What is the final Price (P)"))
            c=(p2-p1)/p1
            print("Change =",c*100,"%")
        elif choice == 17:
            t1= float(input("What is the starting value of the Total Cost(TC1)"))
            t2= float(input("What is the final value of the Total Cost(TC2)"))
            c= (t2-t1)/t1
            print("Change =",c*100,"%")
   
   
   
   again= str(input("Do you want to continue or end? Type 'END' to abort "))
if again=="END":
    print("Aborting... \n in 3\n ...2\n ...1")