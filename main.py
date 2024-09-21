try:
     a=int(input('Enter a'))
if a%2==0:
    raise ValueError
  print('Number is: ',a) 
except ValueError:
print('Number is divisable by 2')

else:
   print('Successful')