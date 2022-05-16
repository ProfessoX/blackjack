import random

game_start = False
draw_phase = False
gs = input("Welcome to Blackjack! Ready to play? 'Y' or 'N'\n").upper()

while game_start == False: 
  if gs == "Y":
    game_start = True
  else:
    gs = input("Welcome to Blackjack! Ready to play? 'Y' or 'N'\n").upper()

cards = [11, 2,  3,  4,  5,  6,  7,  8,  9,  10,  10, 10, 10]
user_c = []
comp_c = []

def deal_cardu():
  user_c.append(random.choice(cards))

def deal_cardc():
  comp_c.append(random.choice(cards))

while game_start == True:
  deal_cardc()
  deal_cardc()
  deal_cardu()
  deal_cardu()
  print(user_c)
  print(comp_c)

  user_score = user_c[0] + user_c[1]
  comp_score = comp_c[0] + comp_c[1] 
  print(f"User = {user_score}")
  print(f"Computer = {comp_score}")

  def score_check():
    if user_score == 21:     # Does either player have the ace + 10?
      print("User has Blackjack! You Win!")
      game_start = False
    elif comp_score == 21:
      print("Computer has Blackjack! You Lose.")
      game_start = False
    elif user_score > 21:
      if user_c[0] == 11 or user_c[1] == 11:
        user_c[0] = 1  or user_c[1] = 1
        if user_score > 21:
          print(f"You Bust with the score of {user_score}! You Lose.")
          game_start = False
    elif comp_score > 21:
      if comp_c[0] == 11 or comp_c[1] == 11:
        comp_c[0] = 1  or comp_c[1] = 1
        if comp_score > 21:
          print(f"Computer busts with the score of {comp_score}! You Win!")
          game_start = False      
    else:
      draw = input("Do you want to draw another card? 'Y' or 'N'\n").upper()
      if draw == "Y":
        draw_phase = True
  
  
  while draw_phase:
      new_draw_u = user_c.append(random.choice(cards))
      user_score += new_draw_u
      print(f"User = {user_score}")
      score_check()
  
  while comp_score < 17:
    new_draw_c = user_c.append(random.choice(cards))
    comp_score += new_draw_c
    print(f"User = {comp_score}")
    score_check()

  while user_score < 21 and comp_score < 21:
    if user_score > comp_score:
      print(f"Your score of {user_score} is closer to 21 than the computer's {comp_score}! You Win!")
      game_start = False
    elif user_score < comp_score:
      print(f"The computer's score {comp_score} is closer to 21 than your score {user_score}! You Lose.")
      game_start = False
    else:
      print(f"You both have the same score of {user_score}. Its a draw.")