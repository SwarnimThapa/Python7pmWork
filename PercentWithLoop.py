x = 1
while x <= 5:
    x += 1
    nep = int(input("Enter obtained marks in nepali."))
    eng = int(input("Enter obtained marks in english."))
    sci = int(input("Enter obtained marks in science."))
    math = int(input("Enter obtained marks in maths."))
    pop = int(input("Enter obtained marks in population."))

    nepful = int(input("Enter full marks in nepali."))
    engful = int(input("Enter full marks in english."))
    sciful = int(input("Enter full marks in science."))
    mathful = int(input("Enter full marks in maths."))
    popful = int(input("Enter full marks in population."))

    if nep > nepful and eng > engful and sci > sciful and math > mathful and pop > popful:
        print("Invalid input.")
    fullobmarks = nep + eng + sci + math + pop
    fullmarks = nepful + engful + sciful + mathful + popful
    percent = fullobmarks / fullmarks * 100
    print(percent ,"%")
    print("===========================================")






