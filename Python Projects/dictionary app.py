dict = {}
while True:
  print("Mini Dictionary App: \n1) Add/Update a word \n2) Retrieve a word's definition \n3) Delete a word \n4) View all words \n5) Exit the program \n6) Check if a word exists in the dictionary \n7) Clear the dictionary \nPlease chooose a number from 1 - 7")
  choice = int(input())
  if choice == 1:
    word = str(input("Please enter the word")).strip() #strip function removes the spaces in the beginning and end
    definition = str(input("Please enter the defenition")).strip()
    dict[word] = definition
    print("word '{}' added/updated successfully! :)".format(word))
  
  elif choice == 2:
    word = str(input("Please enter the word that you would like to know the definition of")).strip()
    if word in dict:
      print("{} - {}".format(word, definition))
      
  elif choice == 3:
    word = str(input("Please enter the word that you would like to delete")).strip()
    if word in dict:
      del dict [word]
      print("The word {} has been deleted".format(word))
    else:
      print("Error 404: word not found")
      
  elif choice == 4:
    if dict:
      print("Words in the dictionary:")
      for i in dict:
        print("{} - {}").format(i, dict[i])
    else:
      print("The dictionary is empty")
      
  elif choice == 5:
    print("Exiting mini dictionary app...")
    break #exits the loop
  
  elif choice == 6:
    word = str(input("Please enter the word that you would like to check")).strip()
    if word in dict:
      print("The word {} is in the dictionary".format(word))
    else:
      print("The word {} is not in the dictionary".format(word))
  
  elif choice == 7:
    if dict:
      dict.clear()
      print("dictionary deleted")
    else:
      print("Error 404: dictionary not found")
  
  else:
    print("Invalid choice")