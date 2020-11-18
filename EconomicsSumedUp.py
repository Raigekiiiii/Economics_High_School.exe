print("Okay, we all hate Kelaiditi, watchu gonna do wee-lad?")
choice = str(input("Do you want to start or terminate the process? Type Y or N respectively"))
while choice=="Y":
    type = input("What do you want to find? 1 for Ed, 2 for Ey ,3 for Arcuate Elasticity,4 for Opportunity cost(KEx/y),5 for finding Qd (using α(positive)) , β(negative) , and p ) and 6 for finding p using Qd,7 for total cost \n")
    if int(type) == 1:
        qd1 = input("What is the 1st desired quantity?(Qd1) ")
        qd2 = input("What is the 2nd desired quantity?(Qd2) ")
        p1 = input("What is the 1st/Starting price?(P1) ")
        p2 = input("What is the 2nd/Final price?(P2) MUST BE DIFFERENT FROM THE 1st ")
        ed = ((float(qd2) - float(qd1)) / (float(p2) - float(p1))) * float(p1) / float(qd1)
        print(str(ed))
        if abs(float(ed)) == 1:
            print("Singular Elasticity")
        elif abs(float(ed)) < 1:
            print("Elastic Demand")
        elif abs(float(ed)) == 0:
            print("Absolute Anelastic Demand")
        elif abs(float(ed)) < 1:
            print("Anelastic Demand")
    elif int(type) == 2:
        qd1 = input("What is the 1st desired quantity?(Qd1) ")
        qd2 = input("What is the 2nd desired quantity?(Qd2) ")
        y1 = input("What is the 1st/Starting income?(Y1)")
        y2 = input("What is the 2nd/Final income?(Y2) MUST BE DIFFERENT FROM THE 1st ")
        ey = ((float(qd2) - float(qd1)) / (float(y2) - float(y1))) * float(y1) / float(qd1)
        print(str(ey))
        if float(ey) >= 1:
            print("Normal Product")
        elif float(ey) < 1:
            print("Inferior Product")
    elif int(type) == 4:
        x1 = input("How many units of product X are first being produced? ")
        x2 = input("How many units of product X are finally being produced? ")
        y1 = input("How many units of product Y are first being produced? ")
        y2 = input("How many units of product Y are finally being produced? ")
        Kex = abs(float(y1 - y2)) / abs(float(x1 - x2))
        Key = 1 / float(Kex)
        print(Kex)
        print(Key)
    elif int(type) == 3:
        qd1 = input("What is the 1st desired quantity?(Qd1) ")
        qd2 = input("What is the 2nd desired quantity?(Qd2) ")
        p1 = input("What is the 1st/Starting price?(P1) ")
        p2 = input("What is the 2nd/Final price?(P2) MUST BE DIFFERENT FROM THE 1st ")
        edac = ((float(qd2) - float(qd1)) / (float(p2) - float(p1))) * (float(p1) + float(p2)) / (
                    float(qd1) + float(qd2))
        print(edac)
        if abs(float(edac)) == 1:
            print("Singular Elasticity")
        elif abs(float(edac)) < 1:
            print("Elastic Demand")
        elif abs(float(edac)) == 0:
            print("Absolute Anelastic Demand")
        elif abs(float(edac)) < 1:
            print("Anelastic Demand")
    elif int(type) == 5:
        a = input("How much is α ")
        b = input("How much is β ")
        p = input("How much is the Price (P) ")
        qd = float(a) + float(b) * float(p)
        print(qd)
    elif int(type) == 6:
        a = input("How much is α ")
        b = input("How much is β ")
        qd = input("How much is the Desired Quantity (Qd) ")
        p = (float(qd) - float(a)) / -float(b)
        print(p)
    elif int(type) == 7:
        qd = input("How much is the Desired Quantity(Qd) ")
        p = input("How much is the Price(P) ")
        tc = float(qd) * float(p)
        print(tc)
    choice = str(input("Do you want to continue or end? Press 'Y' to continue or 'E' to terminate the process"))



