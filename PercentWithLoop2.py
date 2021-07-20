#Because full marks is needed one time input, it is kept outside loop.

#Enter school name.
schoolname = input("Please enter school name.")
schoolclass =input("Enter your school class.")

#Enter full marks and pass marks of every subject.
#Since full marks and pass marks are same for every students, it will be entered once.

nepful = int(input("Enter full marks in nepali."))
neppass = int(input("Enter pass marks of nepali."))

engful = int(input("Enter full marks in english."))
engpass = int(input("Enter pass marks of english."))

sciful = int(input("Enter full marks in science."))
scipass = int(input("Enter pass marks of science."))

mathful = int(input("Enter full marks in maths."))
mathpass = int(input("Enter pass marks of maths."))

popful = int(input("Enter full marks in population."))
poppass = int(input("Enter pass marks of population."))


fullmarks = nepful + engful + sciful + mathful + popful
print("Total full marks is " ,fullmarks)

#Variable y definded for incremental and x for number of student.
y = 1
x = int(input("Amount of students?"))

#Input all student (x students) obtainded marks.
while y<=x:
    y+=1
    name = input("Please input the students name")

#Input of marks obtained by student.

    nep = int(input("Enter obtained marks in nepali."))
    eng = int(input("Enter obtained marks in english."))
    sci = int(input("Enter obtained marks in science."))
    math = int(input("Enter obtained marks in maths."))
    pop = int(input("Enter obtained marks in population."))

#To check invalid obtained marks.
    if nep > nepful and eng > engful and sci > sciful and math > mathful and pop > popful:
        print("Invalid input.")

    fullobmarks = nep + eng + sci + math + pop
    percent = fullobmarks / fullmarks * 100
    print(percent, "%")
    print("===========================================")


