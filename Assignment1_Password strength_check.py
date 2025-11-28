# Assignment 1 - Password strength program
def password_strength(password):
    pass_val = False
    while pass_val == False and password != 'q':
    
      for y in str(password):
         contains_num = y.isdigit()
         if contains_num == True:
          break
         
      for y in str(password):
         contains_alpha = y.isalpha()
         if contains_alpha == True:
            break
      
      for y in str(password):
         contains_only_alnum = y.isalnum()
         if contains_only_alnum == False:
            break
         
      length = len(password)
      upper_Case = password[0].isupper()    
      
      if contains_num == True:
         if length >= 8:
               if contains_alpha == True:
                  if contains_only_alnum == False:
                     if upper_Case == True:
                        print("It is a valid password")
                        pass_val = True
                     else:
                         print("Invalid password, first charecter shoud be upper case alphabet")
                         password = input("Enter a valid password, press q to quit: ")   
                  else:
                     print("Invalid password, password should contain atleast one special charecter")
                     password = input("Enter a valid password, press q to quit: ")                 
               else:
                  print("Invalid password, password doesnt contain alphabets")
                  password = input("Enter a valid password, press q to quit: ") 
         else:
            print(f"Invalid password, password length is just {length}")
            password = input("Enter a valid password, press q to quit: ") 
      else:
         print("Invalid password, doesnt contain numerals")
         password = input("Enter a valid password, press q to quit: ") 

print("""Please setup a strong password:
         Minimum length: The password should be at least 8 characters long.
         Contains both uppercase and lowercase letters.
         Contains at least one digit (0-9).
         Contains at least one special character (e.g., !, @, #, $, %)""")
password = input("Enter the password, press q to quit: ")
password_strength(password)