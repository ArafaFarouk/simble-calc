while True:
  # check if the user has entered a number
  while True:
    try:
      first_number = float (input("Enter first number: "))
      break
    except ValueError:
      print("Invalid input. Please enter a numaric value .")

  # check if the user has entered a opeartion
  while True:
    try:
       operation = input("Enter operation type: ")
       if operation in ("+","-","*","/"):
         break
       else:
         raise ValueError  
    except ValueError:
      print("Invalid operator, please enter +,-,*,/")
  # check if the user has entered a number    
  while True:
    try:
      second_number = float(input("Enter second number: "))
      if second_number == 0  and operation == '/':
        raise ZeroDivisionError
      break
    except ValueError:
      print("Invalid input. Please enter a numaric value .")
    except ZeroDivisionError:
      print("cannot divide by zero  ")
#--------------------------------------------------#
  # print the result
  # if operation == "+":
  #   print(first_number + second_number)
  # elif operation == "-":
  #   print(first_number - second_number)
  # elif operation == "/":
  #   print(first_number / second_number)
  # elif operation == "*":
  #   print(first_number * second_number)
  # else:
  #   print("Error")
#---------------------------------------------------#
  # the result use match 
  match operation:
    case "+":
      result = first_number + second_number
    case "-":
      result = first_number - second_number
    case "/":
      result = first_number / second_number
    case "*":
      result = first_number * second_number
    case _:
      result = None
  
  if result != None:
    print (result)
    
  # ask the user if he wants to perform another operation
  repeat = input("Do you want to perform another operation (y/n): ")
  if repeat == "n" or repeat == "N":
    break
  elif repeat == "y" or repeat == "Y":
    continue
  else:
    print("Invalid input. Please enter 'y' or 'n'.")
            
print("Program exited")

  