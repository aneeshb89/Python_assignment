def password_strength(password):
    
    pass_val = False
    while pass_val == False:
    
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
                         password = input("Enter a valid password: ")   
                  else:
                     print("Invalid password, password should contain atleast one special charecter")
                     password = input("Enter a valid password: ")                 
               else:
                  print("Invalid password, password doesnt contain alphabets")
                  password = input("Enter a valid password: ") 
         else:
            print(f"Invalid password, password length is just {length}")
            password = input("Enter a valid password: ") 
      else:
         print("Invalid password, doesnt contain numerals")
         password = input("Enter a valid password: ") 


password = input("Enter the password: ")
password_strength(password)