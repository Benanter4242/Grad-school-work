#The program will be built in a try and accept loop so that way if an error occurs it can inform the user as such
 # the next part of the program involves an input float variable that describes clearly to the user the function of the program and how to use it.
try:
  TempF=float(input("Hello and thank you for using compute temperature 5000. Give me today's temperature in Fahrenheit and I will give you a rating on the weather and change the input to Celsius for you."))
  #This variable takes the input variable as discussed previously to convert it into a Celsius property.
  C= (TempF-32.0)*5.0/9.0
#Lastly this program uses a else if loop and determines based on what temperature they inputted a message and what degrees they entered in Celsius.
  if C <0:
    print("Don't forget your coat and hat!",C,"calculus")
  elif C  <11:
    print( "It's quite cold, isn't it?",C,"calculus")
  elif C  <19:
     print( "Might need a sweater",C,"calculus")
  elif C  <25:
     print("Pretty nice weather today!",C,"calculus")
  elif C  <30 or 30:
     print( "Getting a bit warm",C,"calculus")
  else :
     print("Summer, eh?",C,"calculus")


except:
  print("error please try again.")
