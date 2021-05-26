import unittest


def find(num):
   
    if num%2 == 0:
        numtype="even"
    else:
        numtype = "odd"
    return numtype

num = int(input('Enter the number: '))  
numtype = find(num)                     
print('Given number is',numtype)


if __name__ == '__main__':
    unittest.main()








"""

def is_odd_or_even(n):
    return "odd" if n&1 else "even"

"""




"""

num = int(input("Enter any number: "))
flag = num%2
if flag == 0:
    print(num, "is an even number")
elif flag == 1:
    print(num, "is an odd number")
else:
    print("Error, Invalid input")

"""


"""

def evenOdd(a,b):
	if(a>b):
		return
	print(a ,end=" ")
	return evenOdd(a+2,b)


x=2
y=10
if(x % 2 ==0):
	x=x
	
else:
	
	x+=1
evenOdd(x,y)

"""