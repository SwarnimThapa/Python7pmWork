class ComputerStore:
    def ComputerList(self):
        self.macs = 791
        self.dell = 971
        self.acers = 1082
        print(f'There are {self.macs} macs, {self.dell} dell and {self.acers} acers laptops in stock currently.')
        print('Pricing: ')
        print('mac: 50000')
        print('dell: 10000')
        print('acers: 25000')
        self.totalstock = (self.macs+self.dell+self.acers)
        print(f'Total stocks: {self.totalstock}')
        return f'There are {self.macs} macs, {self.dell} and {self.acers} acer laptops in stocks currently. The macs cost 50,000 the dell costs 10000 and the acers cost 25000'
    def macbuy(self):
        macs = 50000
        mactaxone = 3846
        mactaxtwo = 5000
        mactaxthree = 3333
        stocks = (self.macs-1)
        print('Choose a location: ')
        x = input('Kahtmandu, Lalitpur, and Pokhara.')
        if x == 'kathmandu':
            print(f'You have bought a mac for the price of {macs+mactaxone}. Now, there are {stocks} macs left.')
        elif x == 'lalitpur':
            print(f'You have bought a mac for the price of {macs+mactaxtwo}. Now, there are {stocks} macs left.')
        elif x =='pokhara':
            print(f'You have bought a mac for the price of {macs+mactaxthree}. Now, there are {stocks} macs left.')
        else:
            print('Enter a valid option please.')
            exit()
            return
    def dellbuy(self):
        dell = 10000
        delltaxone = 769
        delltaxtwo = 1000
        telltaxthree = 666
        stonks = (self.dell-1)
        print('Choose a location. ')
        x = input('Kathmandu, Lalitpur, Pokhara.')
        if x == 'kathmandu':
            print(f'You have bought a mac for the price of {dell+delltaxone}. Now, there are {stonks} macs left.')
        elif x == 'lalitpur':
            print(f'You have bought a mac for the price of {dell + delltaxtwo}. Now, there are {stonks} macs left.')
        elif x == 'pokhara':
            print(f'You have bought a mac for the price of {dell + telltaxthree}. Now, there are {stonks} macs left.')
        else:
            print('Enter a valid option please')
            exit()
            return
    def acerbuy(self):
        acer = 25000
        acctaxnone = 1923
        acctaxtwo = 2500
        acctaxthree = 1666
        stocks = (self.acers-1)
        print('Choose a location. ')
        x = input('Kathmandu, lalitpur, and pokhara. ')
        if x == 'kathmandu':
            print(f'You have bought a mac for the price of {acer+acctaxnone}. Now, there are {stocks} macs left.')
        elif x == 'lalitpur':
            print(f'You have bought a mac for the price of {acer + acctaxtwo}. Now, there are {stocks} macs left.')
        elif x == 'pokhara':
            print(f'You have bought a mac for the price of {acer + acctaxthree}. Now, there are {stocks} macs left.')
        else:
            print('Enter a valid option please.')
            return


comp = ComputerStore()
comp.ComputerList()
x = input('Which laptop would you like to buy? ')
if x == 'mac':
    comp.macbuy()
    exit()
elif x == 'dell':
    comp.dellbuy()
    exit()
elif x == 'acer':
    comp.acerbuy()
    exit()
else:
    print('Enter a valid option please.')

