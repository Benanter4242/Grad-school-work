#Prompt the user to ask a score between the floating integers 0.0 and 1.0.
#If user puts in a floating integer out of the 0.0 and 1.0 rage print an error message explaining the problem
#Depending on what score the user puts it will showcase either in A, B, C, D, or F


input_score = input('Enter a score between 0.0 and 1.0: ')
try:
  if (float(input_score) >= 0) and ( float(input_score) <= 1 ):
    print('valid input, thanks!')
  else:
    print ('Invalid input please give numeric number')
    input_score = input('Enter a score between 0.0 and 1.0: ')
except:
  print ('Invalid input please give numeric number')
  input_score = input('Enter a score between 0.0 and 1.0: ')

input_score = float(input_score)

if input_score < 0.6:
  print ('F')

elif input_score >= 0.9:
  print ('A')

elif input_score >= 0.8:
  print ('B')

elif input_score >= 0.7:
  print('C')

elif input_score >= 0.6:
  print('D')

else:
  print ('error please try again')
