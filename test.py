class test:
    def __init__(self, bosshealth, health, kickdamage, punchdamage, heal, bossdamage, bossdamage2, healamount):
        self.bosshealth = bosshealth
        self.health = health
        self.kickdamage = kickdamage
        self.punchdamage = punchdamage
        self.heal = heal
        self.bossdamage = bossdamage
        self.bossdamage2 = bossdamage2
        self.healamount = healamount







ts = test(1000, 100, 10, 75, 25, 15, 20, 7)




increnmental = 0

print('Enter end to end the loop.')


while increnmental<=1000:
    increnmental+=1
    damage = input('Would you like to kick, punch or heal? ')
    if damage == 'kick':
        ts.bosshealth-=ts.kickdamage
        print(f'The boss now has {ts.bosshealth} health left.')
        ts.health -= ts.bossdamage
        print(f'But, you now have {ts.health} health left.')
    elif damage == 'punch':
        ts.bosshealth-=ts.punchdamage
        print(f'The boss now hos {ts.bosshealth} health left.')
        ts.health -= ts.bossdamage2
        print(f'But, you now have {ts.health}')
    elif damage == 'heal':
        ts.health += ts.heal
        ts.healamount -= 1
        print(f'You have healed, and now have {ts.health} now, but you have {ts.healamount} healing left..')
    elif damage == 'end':
        print('You have now left the game!')
        exit()
    else:
        print('Enter a valid option please.')

    if ts.bosshealth == 0:
        print('You have defeated the game')
        exit()
    elif ts.health<=0:
        print('You have lost the game.')
        exit()

