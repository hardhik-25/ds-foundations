def main(number):
    greater_number(number)
def greater_number(n):
    for i in range(len(n)):
        if n[i]>10:
            print(n[i])
main([5,12,8,20,3,15])

