print ("""
  You have woken up in a small room alone. 
  There are 3 doors infront of you - If you guess right you can leave.
  Well what are you waiting for? Lets see what the gods of fortune have in store for you... 
  Muahhahahahahahahahahahaha 
""")


Doors = ['Door A', 'Door B', 'Door C']

for i in Doors:
 print (i)

Answer =(input ("Which Door have you chosen? Enter as a capital letter "))

if Answer == ("A"):
 print ("""
             ___          
            /   \\        
       /\\ | . . \\       
     ////\\|     ||       
   ////   \\ ___//\       
  ///      \\      \      
 ///       |\\      |     You face the grim reaper! The grim reaper strikes his scythe and takes your soul
//         | \\  \   \    
/          |  \\  \   \   
           |   \\ /   /   
           |    \/   /    
           |     \\/|     
           |      \\|     
           |       \\     
           |        |     
           |_________\    
""")

elif Answer == ("B"):
 print ("""

  /\_/
 ( o.o )     
  > ^ <

You face the ultra cute kitty of doom! With an adorable meow it disintegrates you. 
-- you have been reduced to kitty litter
""")
else:
  Answer == ("C")
  print ("You are freeeeeeeee")

