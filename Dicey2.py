import random 

Even_bonus = 10
Odd_subtract = -5

#Player 1 Round 1

Name1 = input(" Enter your name ")
 
Dice1 = random.randint(1,6)
Dice2 = random.randint(1,6)
  
Player_1_Score = Dice1 + Dice2 

print("Score before bonus is "+ str(Player_1_Score))

if Player_1_Score % 2 == 0:
    print("even!")
    Player_1_ScoreA = (int(Even_bonus) + int(Dice1) + int(Dice2))
elif Player_1_Score % 2 == 1:
    print("odd!")
    Player_1_ScoreA = (int(Odd_subtract) + int(Dice1) + int(Dice2))
   
print("In round 1 you have scored " + str(Player_1_ScoreA))

#Player 2 Round 1

Name2 = input(" Second player enter your name ")
print("Welcome " + Name2)

Dice3= random.randint(1,6)
Dice4 = random.randint(1,6)

Player_2_Score = Dice3 + Dice4

print("Score before bonus is " + str(Player_2_Score))

if Player_2_Score % 2 == 0:
    print("even!")
    Player_2_ScoreA = (int(Even_bonus) + int(Dice3) + int(Dice4))
elif Player_2_Score % 2 == 1:
    print("odd!")
    Player_2_ScoreA = (int(Odd_subtract) + int(Dice3) + int(Dice4))

print("In round 1 you have scored " + str(Player_2_ScoreA))

if Player_2_ScoreA > Player_1_ScoreA:
   print("Player 2 Is Winning")
else:
   print("Player 1 is Winning")

#Player 1 Round 2

P1R2 = input("Are You ready for round 2 ")
print("Player 1 round 2")

Dice1a = random.randint(1,6)
Dice2a = random.randint(1,6)
  
Player_1_Scorev2 = Dice1a + Dice2a

print("Score before bonus is " + str(Player_1_Scorev2))

if Player_1_Scorev2 % 2 == 0:
    print("even!")
    Player_1_ScoreAv2 = (int(Even_bonus) + int(Dice1a) + int(Dice2a))
elif Player_1_Scorev2 % 2 == 1:
    print("odd!")
    Player_1_ScoreAv2 = (int(Odd_subtract) + int(Dice1a) + int(Dice2a))
   
print("In round 2 you have scored " + str(Player_1_ScoreAv2))
x = (Player_1_ScoreA) + (Player_1_ScoreAv2)
print("Player 1 total score is " + str(x))

#Player 2 Round 2 

P2R2 = input("Are You ready for round 2 ")
print("Player 2 round 2")

Dice3a = random.randint(1,6)
Dice4a = random.randint(1,6)
  
Player_2_Scorev2 = Dice3a + Dice4a

print("Score before bonus is " + str(Player_2_Scorev2))

if Player_2_Scorev2 % 2 == 0:
    print("even!")
    Player_2_ScoreAv2 = (int(Even_bonus) + int(Dice3a) + int(Dice4a))
elif Player_2_Scorev2 % 2 == 1:
    print("odd!")
    Player_2_ScoreAv2 = (int(Odd_subtract) + int(Dice3a) + int(Dice4a))
   
print("In round 2 you have scored " + str(Player_2_ScoreAv2))
z = (Player_2_ScoreA) + (Player_2_ScoreAv2)
print("Player 2 total score is " + str(z))

if z > x:
   print("Player 2 Is Winning")
else:
   print("Player 1 is Winning")

#End of round 2. 
#Player 1 Round 3 

P1R3 = input("Are You ready for round 3 ")
print("Player 1 round 3")

Dice1b = random.randint(1,6)
Dice2b = random.randint(1,6)
  
Player_1_Scorev3 = Dice1b + Dice2b

print("Score before bonus is " + str(Player_1_Scorev3))

if Player_1_Scorev3 % 2 == 0:
    print("even!")
    Player_1_ScoreAv3 = (int(Even_bonus) + int(Dice1b) + int(Dice2b))
elif Player_1_Scorev3 % 2 == 1:
    print("odd!")
    Player_1_ScoreAv3 = (int(Odd_subtract) + int(Dice1b) + int(Dice2b))
   
print("In round 3 you have scored " + str(Player_1_ScoreAv3))
x3 = int(x) + (Player_1_ScoreAv3)
print("Player 1 total score is " + str(x3))

#Player 2 Round 3

P2R3 = input("Are You ready for round 3 ")
print("Player 2 round 3")

Dice3b = random.randint(1,6)
Dice4b = random.randint(1,6)
  
Player_2_Scorev3 = Dice3b + Dice4b

print("Score before bonus is " + str(Player_2_Scorev3))

if Player_2_Scorev3 % 2 == 0:
    print("even!")
    Player_2_ScoreAv3 = (int(Even_bonus) + int(Dice3b) + int(Dice4b))
elif Player_2_Scorev3 % 2 == 1:
    print("odd!")
    Player_2_ScoreAv3 = (int(Odd_subtract) + int(Dice3b) + int(Dice4b))
   
print("In round 3 you have scored " + str(Player_2_ScoreAv3))
z3 = int(z) + (Player_2_ScoreAv3)
print("Player 2 total score is " + str(z3))

if z3 > x3:
   print("Player 2 Is Winning")
else:
   print("Player 1 is Winning")

#End of Round 3
#Crackdown
 
END = input("Is this the end")

with open ('Myfile.txt', 'w') as Scores:
    Scores.write("Player 2 has scored " + str(z3) + " Player 1 has scored " + str(x3))







