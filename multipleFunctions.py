class multipleFunctions():
    def Subfields():
        print("Subfields in AI are:")
        List=['Machine Learning', 'Neural Networks', 'Vision', 'Robotics', 'Speech Processing', 'Natural Language Processing']
        for item in List:
            print(item)                        # Tried ways for print statement in single line without 'for in'
        return (List)

    def OddEven():
        Num=int(input('Enter a number: '))
        print(f"{Num} is {'Even'if Num %2==0 else 'Odd'} number")
        return(Num %2==0)
    
    def percentage():
        ListofSubject=['Subject1','Subject2','Subject3','Subject4','Subject5']
        ListofMark=[98,87,95,95,93]         # All copied frm function assigment
        Total=sum(ListofMark)               #except to value in ListofMark
        Percentage=(Total/500)*100
        for ListofSubject,ListofMark in zip(ListofSubject,ListofMark):   #List line onward to learn-both list zip
            print(f"{ListofSubject}={ListofMark}")                       #zip so item and value referd 
        print("Percentage:", Percentage)
        return (Percentage)
    
    def Elegible():
        Gender=str(input('Your Gender:'))
        Age=int(input('Your Age:'))
        if (Gender=="Male" and Age>=21):
            print("ELIGIBLE")
            Eligibility=str("ELIGIBLE")
        elif (Gender=="Female" and Age<=18):
            print("ELIGIBLE")
            Eligibility=str("ELIGIBLE")
        else:
            print("Not ELIGIBLE")
            Eligibility=str("NOT ELIGIBLE")
        return (Eligibility)
    
    def triangle():
        def Area():
            Height=32
            Breadth=34
            Area="(Height*Breadth)/2"
            AreaCal=(Height*Breadth)/2
            print("Height:", Height)
            print("Breadth:", Breadth)
            print(f"Area formula: ",Area)
            print("Area of Triangle: ", AreaCal)
            return(AreaCal)
        def Perimeter():
            Height=3
            Breadth=4
            Area="(Height*Breadth)/2"
            AreaCal=(Height*Breadth)/2
            Height1=2
            Height2=4
            Breadth=4
            Perimeter="Height1+Height2+Breadth"
            PerimeterCal=Height1+Height2+Breadth
            print("Height1:",Height1)
            print("Height2:",Height2)
            print("Breadth:",Breadth)
            print(f"Perimeter formula: ",Perimeter)
            print("Perieter of Triangle: ",PerimeterCal)
            return (PerimeterCal)
        return(Area(), Perimeter())
    
    def BMI():
        BMI=int(input("Enter the BMI Index :"))#Dcl Interger, otherwise would be string
        if(BMI<18):                             #Operator on lowest if(condition) must ends with :
            print("Underweight")                
            BMICat="Underweight"                #print need ()& andthing within "" string, doesn't have :
        elif(BMI<25):                         
            print("Healthy Weight")
            BMICat="Healthy Weight"
        elif(BMI<30):                          #BMI within 25 to 29
            print("Overweight")
            BMICat="Overweight"
        else:                                  #else statement finishes remaining with output, else do no have (), just :
            print("Very Overweight")           # Input 30 and onwards is overweight
            BMICat="Very Overweight"
        return (BMICat)                     

    def Category():
        age=int(input("age:"))
        if(age<18):                     #Faced difficulties here due to spaceing, alignment
            print("Child")          #errors was shown in syntaxs which correct
            Cat="Child"
        elif(age<35):
            print("Adult")
            Cat="Adult"
        elif(age<59):
            print("Citizen")
            Cat="Citizen"
        else:
            print("Senior Citizen")
            Cat="Senior Citizen"
        return (Cat)
           