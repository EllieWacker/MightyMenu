def take_quiz():
  print()
  print ('Welcome to the which book should you read quiz!')
  pride_and_prejeduce = 0
  the_hobbit = 0
  the_martian = 0
  print()

  print('Question 1:')
  print('Where do you want to live?')
  a = 'a = A mountain, '
  b = 'b = Space or'
  c = 'c = A mansion'
  print(a,b,c)
  question_1 = input('Type answer here: ')
  if question_1 == 'a':
    the_hobbit = the_hobbit + 1
  elif question_1 == 'b': 
    the_martian = the_martian + 1
  elif question_1 == 'c':
    pride_and_prejeduce = pride_and_prejeduce + 1
  else: print('That is not an answer!')
  print()

  print('Question 2:')
  print('What kind of books do you like?')
  a = 'a = Romantic, '
  b = 'b = Fantasy or'
  c = 'c = Sci-fi'
  print(a, b, c)
  question_2 = input('Type your answer here: ')
  if question_2 == 'a':
    pride_and_prejeduce = pride_and_prejeduce + 1
  elif question_2 == 'b': 
    the_hobbit = the_hobbit + 1
  elif question_2 == 'c':
    the_martian = the_martian + 1
  print()
  
  print('Question 3:')
  print('What time would you like to live in?')
  a = 'a = The 1800s, '
  b = 'b = Medieval times or'
  c = 'c = The Future'
  print(a,b,c)
  question_3 = input('Type your answer here: ')
  if question_3 == 'a':
    pride_and_prejeduce = pride_and_prejeduce + 1
  elif question_3 == 'b': 
    the_hobbit = the_hobbit + 1
  elif question_3 == 'c':
    the_martian = the_martian + 1
  else: print('That is also not an answer!')
  print()

  print('Question 4:')
  print('What type of music do you like?')
  a = 'a = Folk, '
  b = 'b = Classical or'
  c = 'c = Rock'
  print(a, b, c)
  question_4 = input('Type your answer here: ')
  if question_4 == 'a':
    the_hobbit = the_hobbit + 1
  elif question_4 == 'b': 
    pride_and_prejeduce = pride_and_prejeduce + 1
  elif question_4 == 'c':
   the_martian = the_martian + 1
  else: print('That is not an answer!')
  print()

  print('Question 5:')
  print('Who is your favorite Disney character?')
  a = 'a = Robin Hood, '
  b = 'b = Cinderella or'
  c = 'c = Stitch'
  print(a, b, c)
  question_5 = input('Type your answer here: ')
  if question_5 == 'a':
    the_martian = the_martian + 1
  elif question_5 == 'b': 
    pride_and_prejeduce = pride_and_prejeduce + 1
  elif question_5 == 'c':
   the_martian = the_martian + 1
  else: print('That is not an answer!')
  print()
    
  if the_hobbit > the_martian and the_hobbit > pride_and_prejeduce:
   print('You should read the Hobbit!')
   print('Full of fantasy and adventure, the Hobbit is the perfect book for you!')
  elif pride_and_prejeduce > the_hobbit and pride_and_prejeduce > the_martian:
    print('You should read Pride and Prejeduce!')
    print('Romantic and dramatic, Pride and Prejeduce will make you swoon!')
  elif the_martian > pride_and_prejeduce and the_martian > the_hobbit:
    print('You should read The Martian!')
    print('Exciting and grand, you will be facinated by The Martian!')
  elif the_martian == the_hobbit and the_hobbit > pride_and_prejeduce:
    print('You should read the martian and the hobbit! You will love both adventure stories!')
  elif the_martian == pride_and_prejeduce > the_hobbit:
    print('You should read the Martian and Pride and Prejeduce! You will love ')
  elif the_hobbit == pride_and_prejeduce > the_martian:
    print('You should read the Hobbit and Pride and Prejeduce! You will love both beautifully written books and their colorful characters!')
    
  else: print('You should read none of these!') 
  print()
  print()
def calculate_math():
  print()
  question_1 = input ('Hi, do you need help with your math? Please input if you want addition, subtraction, multiplication or division. ')
  if question_1 == ('addition'):
    addition_1 = int(input('Please enter your 1st number: '))
    addition_2 = int(input('Please enter your 2nd number: '))
    print('Your number =', (addition_1) + (addition_2))
    
  elif question_1 == ('subtraction'):
    subtraction_1 = int(input('Please enter your 1st number: '))
    subtraction_2 = int(input('Please enter your 2nd number: '))
    print('Your number =', (subtraction_1) - (subtraction_2))

  elif question_1 == ('multiplication'):
    multiplication_1 = int(input('Please enter your 1st number: '))
    multiplication_2 = int(input('Please enter your 2nd number: '))
    print('Your number =', (multiplication_1) * (multiplication_2))
  
  elif question_1 == ('division'):
    division_1 = int(input('Please enter your 1st number: '))
    division_2 = int(input('Please enter your 2nd number: '))
    print('Your number =', (division_1) / (division_2))

  else: print('Please try again.')
  print()
print('Welcome to Mighty Menu. Please enter all answers in lower_case! What would you like to do?')
choice = input('a = take a quiz or b = math calculator: ')
if choice == 'a':
  take_quiz()
if choice == 'b':
  calculate_math()
repeat = input('Do you want to start over? y/n ')
print()
while repeat == 'y':
  print('Welcome to Mighty Menu. Please enter all answers in lower_case! What would you like to do?')
  choice = input('a = take a quiz or b = math calculator: ')
  if choice == 'a':
    take_quiz()
  if choice == 'b':
    calculate_math()

    
print('Goodbye!')