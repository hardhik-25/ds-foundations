def main(n):
    triangle(n)

def triangle(n):
    for i in range(0,n): 
        for j in range(i+1):
            print("*",end="")
        print()    
main(4)


#  PROBLEM 1
def main(number):
    num(number)
def num(n):
    for i in range(1,n+1):
        if i%3 == 0:
            print(i)
main(15)

# PROBLEM 2
def main(number):
    num(number)

def num(n):
    for i in range(1,11):
        mult = n*i
        print(f'{n}*{i} = {mult}')
main(7)

# PROBLEM 3
n = 4
for i in range(n):
    for j in range(n):
        if i==0 or i == n-1 or j ==0 or j == n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
            
