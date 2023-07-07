a = input('Enter your name: ')
b = input('Enter your age: ')
print('Hello,',b,'years old',a)
c = input('Do you want to start? (yes or no): ')
print('wait a moment...')
import time
time.sleep(5)
if c=='yes':
	print('ok, let\'s start')
	print('what is the consequence of a and b?''\n''a=?''\n''b=?''\n''print((a+b)//3)''\n''output:558')
	a1=int(input('a= '))
	b1=int(input('b= '))
	if (a1+b1)//3==558:
		print('well done!''\n''now next question: ')
		d=input('what means this operation in python3: **''\n''answer: ')
		if d=='exponentiation':
			print('well,you know more than I thouhght')
			print('next question')
			e=input('for what in pyton3 uses this operator: while''\n')
			if e=='for making endless cycle':
				print('so, cycles you know too')
			else:
				print('come back when you revise cycles!')
		else:
			print('you should go and learn basic information about python3!!!')
	else:
		print('go and learn maths!!!')
elif c=='no':
	print('oh, it is your choice')
else:
	print('wrong answer,please,try again')
input('Press ENTER to exit')
