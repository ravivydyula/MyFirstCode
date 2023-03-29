print ("Welcome to Treasure Island ")
print ("-------------------------- ")
print ("Below are the choices you have: ")
print ("1. Play ")
print ("2. Quit ")
i_choice = int(input("Enter your choice: "))
print ("your choice is ", i_choice)
if i_choice == 2:
  SystemExit()
else:
  print("Good! You made right choice")
  print("Which direction you want to go?")
  print ("1. Left")
  print ("2. Right")
  i_choice_1 = int(input("Enter your choice: "))
  if i_choice_1 == 2:
    print("YOU LOSE")
    SystemExit()
  else:
    print("Ola! Glad you made it!")
    print("Here is a river. You need to cross it?")
    print ("1. Do you want to swim?")
    print ("2. Do you want to wait for boat?")
    i_choice_2 = int(input("Enter your choice: "))
    if i_choice_2 == 1:
      print("YOU LOSE")
      SystemExit()
    else:
      print("You have reached the tressure")
      print("Which door you want to open?")
      print ("1. Red")
      print ("2. Yellow")
      print ("3. Blue")
      i_choice_3 = int(input("Enter your choice: "))
      if i_choice_3 == 2:
        print("YOU WIN")
      else:
        print("YOU LOSE! TRY AGAIN")
        
      
      
  