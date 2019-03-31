import time
import calendar


class infant:
    cusList = []

    def __init__(self):
        self.name = ''
        self.age = 0
        self.infantID = 0
        self.phnNo = 0
        self.address = ''

    def addinfant(self, name, age, id, address, phnNo):
        self.name = name
        self.age = age
        self.infantID = id
        self.address = address
        self.phnNo = phnNo

        infant.cusList.append(self)
        return True

    def mySortAlgo(self, cus):
        return cus.infantID

    def sortinfant(self):
        infant.cusList.sort(key=self.mySortAlgo)

    def reminder(self, age):
        if (age>= 6 and age<=7):
            print("Your child should get OPV1, Penta1(DPT+HepB+HiB)")
        elif (age>=10 and age<=12):
            print("Your child should get OPV2, Penta2(DPT+HepB+HiB)")
        elif (age >= 14 & age <= 16):
            print("Your child should get OPV3, Penta3(DPT+HepB+HiB),IPV")
        elif (age >= 36 & age <= 38):
            print("Your child should get MMR-1, /MR/Measels, JE Vaccine-1)")
        elif (age >= 64 & age <= 96):
            print("Your child should MMR-1, OPV Booster, DPT 1st Booster, JE Vaccine-2")
        else:
            print("Your child is in good health conditions")

def updateinfant(obb):
    print("Choose Any One:\n1.Name\n2.ID\n3.Age\n4.PhoneNo.\n5.Address")
    wish = int(input("Enter your choice"))
    if (wish == 1):
        while True:
            name2 = input("Enter Your Name")
            obj.addinfant(name2, age1, id1, address1, phnNo1)
            print("infant Updated successfully")
            if name2.isalpha():
                name2
                break
            else:
                print("Please use only letters, try again")
    if (wish == 2):
        while True:
            try:
                id2 = int(input("enter new phone number"))
                obj.addinfant(name1, age1, id2, address1, phnNo1)
                print("infant Updated successfully")
            except:
                print("This is not an Integer.")
                continue
    if (wish == 3):
        while True:
            try:
                age2 = int(input("enter new phone number"))
                obj.addinfant(name1, age2, id1, address1, phnNo1)
                print("infant Updated successfully")
            except:
                print("This is not an Integer.")
                continue
    if (wish == 5):
        address2 = input("enter new address")
        obj.addinfant(name1, age1, id1, address2, phnNo)
        print("infant Updated successfully")
    if (wish == 4):
        while True:
            try:
                phnNo2 = int(input("enter new phone number"))
                obj.addinfant(name1, age1, id1, address1, phnNo2)
                print("infant Updated successfully")
            except:
                print("This is not an Integer.")
                continue


def deleteinfant(obb):
    infant.cusList.remove(obb)


def searchinfant(infantID):
    # for i in range(0,len(infant.cusList)):
    #     if(infant.cusList[i].infantID==infantID):
    #         return infant.cusList[i]
    #     else:
    #         return False
    for cus in infant.cusList:
        if (cus.infantID == infantID):
            return cus
    else:
        return False

print("****Welcome to the infant Information Centre****")
while (True):
    print(
        "1.Add deatils about infant\n2.Show deatils about infant\n3.Delete deatils about infant\n4.Update deatils about infant\n5.Sort deatils about infant\n6.Vaccine Information(Add information about your infant first)")
    choice = int(input("Enter your choice"))
    if (choice == 1):
        print('Do You want to see the date and time?: press 1 for Yes and 2 for NO')
        answer = int(input(choice));
        if (answer == 1):
            var1 = time.time()
            print(var1)

            local = time.localtime(time.time());
            print(local)

            timeLocal = time.asctime(time.localtime(time.time()));
            print(timeLocal)

            calendarVar = calendar.month(2008, 1)
            print(calendarVar)
        if (answer == 1):
            print("You can proceed further!")
        obj = infant()
        while True:
            name1 = input("Enter Your Name")
            if name1.isalpha():
                name1
                break
            else:
                print("Please use only letters, try again")
        try:
            age1 = int(input("Enter infant's age in terms of weeks"))
        except ValueError:
            print("This is not an Integer.")
            continue
        try:
            id1 = int(input("Enter infant Birht ID"))
        except ValueError:
            print("This is not an Integer.")
            continue
        try:
            address1 = input("Enter Location")
        except ValueError:
            print("Don't put numerical value")
            continue
        try:
            phnNo = int(input("Enter Phone No"))
        except ValueError:
            print("This is not an Integer.")
            continue
        obj.addinfant(name1, age1, id1, address1, phnNo)
        print("infant added successfully")
        print('-------Next Operation-------')

    elif (choice == 2):
        idd = int(input("Enter id of infant"))
        obb = searchinfant(idd)
        print('-------Next Operation-------')

        if (obb != False):
            print("Name:", obb.name, "infant Id:", obb.infantID, "Age", obb.age, "Phone No.", obb.phnNo, "Address:",
                  obb.address)
    elif (choice == 3):
        idd = int(input("Enter id of infant"))
        obb = searchinfant(idd)
        deleteinfant(obb)
        print('-------Next Operation-------')

    elif (choice == 4):
        print('Do You want to see the date and time?: press 1 for Yes and 2 for NO')
        answer = int(input(choice));
        if (answer == 1):
            var1 = time.time()
            print(var1)

            local = time.localtime(time.time());
            print(local)

            timeLocal = time.asctime(time.localtime(time.time()));
            print(timeLocal)

            calendarVar = calendar.month(2008, 1)
            print(calendarVar)
        if (answer == 1):
            print("You can proceed further!")
        idd = int(input("Enter id of infant"))
        obb = searchinfant(idd)
        updateinfant(obb)
        print('-------Next Operation-------')

    elif (choice == 5):
        obb = infant()
        obb.sortinfant()
        print('-------Next Operation-------')

    elif (choice == 6):
        age = int(input("Enter the age of your child in terms of weeks"))
        obb = infant()
        obb.reminder(age)
        print('-------Next Operation-------')
