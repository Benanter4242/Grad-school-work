#prompts the user to enter the number of hours.
#prompt the user to enter the rate of money earned per hour.
# If users enter non-numeric output say error message explaining why calculation cannot resume.
#If the user puts in more than 40 hours calculate accordingly by subtracting the extra time.
# Afterwords calculate the value of extra pay by multiplying the extra time by .5 and the hourly rate times the extra time.
#print the total and market as pay


hours = input('enter hours: ')
try:
  float(hours)>=0
except:
  print ('error please give numeric number')

  hours = input('please enter hours: ')

rate = input('please enter rate: ')
try:
  float(rate) >=0
except:
  print ('error please give numeric number')
  rate = input('please enter rate: ')

hours = float(hours)
rate = float(rate)

if hours > 40:
  extra_time = hours - 40
else:
  extra_time = 0

extra_pay = 0.5 * rate * extra_time

pay = hours * rate + extra_pay

print ('pay: '),
print pay
