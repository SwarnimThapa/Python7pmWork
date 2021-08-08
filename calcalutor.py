import os.path

if not os.path.exists('db.txt'):
    fs = open('db.txt', 'w')
    fs.close()

def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mult(x,y):
    return x*y


def zerofinder(function):
    def inar(x, y):
        if y == 0:
            print("Cannot divide by 0.")
            exit()
        else:
            return function(x, y)
        return inar
@zerofinder
def div(x,y):
    return x/y


x = int(input('Enter your first number: '))
z = input("Enter either add, sub, mult, or div. ")
y = int(input("Enter your second number: "))
if z == 'add':
    ans = (f"Result is: {x+y}.")
    print(ans)
    handle = open('db.txt', 'a')
    handle.write(ans)
    handle.write('\n')
    handle.close()
    exit()
elif z == 'sub':
    ans = (f"Result is: {x-y}.")
    print(ans)
    handle = open('db.txt', 'a')
    handle.write(ans)
    handle.write('\n')
    handle.close()
    exit()
elif z == 'mult':
    ans = (f"Result is: {x*y}")
    print(ans)
    handle = open('db.txt','a')
    handle.write(ans)
    handle.write('\n')
    handle.close()
    exit()
elif z == 'div':

    ans = (f"Result is: {x/y}")
    print(ans)
    handle = open('db.txt', 'a')
    handle.write(ans)
    handle.write('\n')
    handle.close()
    exit()


