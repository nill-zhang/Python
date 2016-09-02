# input a number, caltulate it until it is 1
# by sfzhang 2016/5/10
import math

def collaz(number):
	if number % 2 == 0:
	    print(number // 2)
	    return number // 2
	else:
	    print(number * 3 + 1)
	    return number * 3 + 1

while True:
	try:
	    r_number = int(input('please give a number:'))
	    break
	except ValueError:
	    print('what the fuck, try again, I told you that is a number !!')

while True:
	# if collaz(r_number) != 1:
	    # r_number = collaz(r_number)
	# else:
	    # break
    r_number = collaz(r_number)
	if r_number == 1:
	    break
 
