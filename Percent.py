nep = int(input("Enter your obtained mark in nepali."))
eng = int(input("Enter your obtained mark in english."))
math = int(input("Enter your obtained mark in maths."))
health = int(input("Enter your obtained marks in health"))
sci = int(input("Enter your obtained marks in science."))

fullnep = int(input("enter your full mark in nepali."))
fulleng = int(input("Entery your full mark in english."))
fullmath = int(input("enter your full mark in english."))
fullhealth = int(input("Enter your full mark in health."))
fullsci = int(input("Enter your full marks in science"))

obmask = nep + eng + math + health + sci
fullmask = fullnep + fulleng + fullmath + fullhealth + fullsci

print("You got ", obmask, " out of ", fullmask)

if nep > 100 or nep > fullnep:
    print("Error.")
elif eng > 100 or eng > fulleng:
    print("Error.")
elif math > 100 or math > fullmath:
    print("Error.")
elif health > 100 or health > fullhealth:
    print("Error.")
elif sci > 100 or sci > fullsci:
    print("Error.")

percent = obmask / fullmask * 100
print("You got ", percent, "%")

if percent < 50:
    print("Failed")
elif percent == 50:
    print("Passed")
elif percent < 75:
    print("C")
elif percent < 80:
    print("B")
elif percent < 90:
    print("A")
elif percent > 90:
    print("A+")



