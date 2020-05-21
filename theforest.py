import os
import sys
import time


message = (r"""

▄▄▄█████▓ ██░ ██ ▓█████      █████▒▒█████   ██▀███  ▓█████   ██████ ▄▄▄█████▓
▓  ██▒ ▓▒▓██░ ██▒▓█   ▀    ▓██   ▒▒██▒  ██▒▓██ ▒ ██▒▓█   ▀ ▒██    ▒ ▓  ██▒ ▓▒
▒ ▓██░ ▒░▒██▀▀██░▒███      ▒████ ░▒██░  ██▒▓██ ░▄█ ▒▒███   ░ ▓██▄   ▒ ▓██░ ▒░
░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄    ░▓█▒  ░▒██   ██░▒██▀▀█▄  ▒▓█  ▄   ▒   ██▒░ ▓██▓ ░ 
  ▒██▒ ░ ░▓█▒░██▓░▒████▒   ░▒█░   ░ ████▓▒░░██▓ ▒██▒░▒████▒▒██████▒▒  ▒██▒ ░ 
  ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░    ▒ ░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░░ ▒░ ░▒ ▒▓▒ ▒ ░  ▒ ░░   
    ░     ▒ ░▒░ ░ ░ ░  ░    ░       ░ ▒ ▒░   ░▒ ░ ▒░ ░ ░  ░░ ░▒  ░ ░    ░    
  ░       ░  ░░ ░   ░       ░ ░   ░ ░ ░ ▒    ░░   ░    ░   ░  ░  ░    ░      
          ░  ░  ░   ░  ░              ░ ░     ░        ░  ░      ░           
                                                                             

                            ████                                        ████                        
                          ██▓▓▓▓██                                    ██▒▒▓▓██                      
                       ██▓▓██▓▓▓▓██        ████████████████        ██▓▓▓▓██▓▓██                    
                    ████████▓▓▒▒██    ██▓▓██▓▓▓▓▓▓▓▓██▓▓██    ██▓▓▓▓████████                    
                     ████▓▓▓▓▓▓████▒▒██▒▒▒▒██  ██▒▒▒▒██  ██▒▒████▒▒████▓▓▓▓▓▓████                  
                   ████▒▒▓▓██████████▓▓▓▓▒▒██▓▓██▒▒▒▒██▓▓██▒▒██▓▓██████████▓▓▒▒████                
                 ██▓▓▒▒▒▒██▒▒▓▓▓▓▓▓▓▓██▓▓██▒▒██▒▒▒▒▒▒▒▒██▒▒██▓▓▓▓▒▒▒▒▓▓▓▓▒▒██▒▒▒▒▒▒██              
          ████▓▓██████▓▓▓▓▓▓████▒▒██▓▓██▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓██▒▒██▒▒████▓▓▓▓▓▓██████▓▓████          
           ██▓▓▓▓██  ██▒▒▒▒████▓▓▒▒██▓▓████▓▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓████▒▒██▓▓▓▓████▒▒▒▒██  ██▓▓▓▓██        
       ████▓▓████    ██▒▒██  ██▓▓▓▓████▓▓████▓▓▓▓▓▓▓▓▓▓▓▓████▓▓████▓▓▓▓██  ██▒▒██    ████▓▓████    
      ██▓▓▓▓██      ██▒▒██    ██▓▓▓▓██▓▓██▓▓▓▓██▓▓▓▓▓▓▓▓██▓▓▓▓██▓▓██▓▓▓▓██    ██▓▓██      ██▓▓▓▓██  
    ██▓▓████      ██▓▓██        ██▓▓████▓▓██▒▒▒▒██▓▓▓▓██▒▒▒▒██▓▓████▓▓██        ██▓▓██      ████▓▓██
    ████        ██▓▓██          ██▒▒██  ██▓▓██▒▒██▓▓▓▓██▒▒██▓▓██  ██▒▒██          ██▓▓██        ████
             ██▓▓██            ██▒▒▒▒██  ████▒▒████▓▓██▒▒████  ██▒▒▒▒██            ██▓▓██          
             ██▓▓██              ██▓▓██    ██▓▓██    ██▓▓██    ██▓▓██              ██▓▓██          
           ██▓▓██                ██▓▓██      ██        ██      ██▓▓██                ██▓▓██        
         ██▓▓██                  ██▓▓██                        ██▓▓██                  ██▓▓██      
        ██▓▓██                    ██▓▓██                        ██▓▓██                    ██▓▓██    
       ████                        ██▒▒██                    ██▓▓██                        ▓▓██    
                                ██▓▓██                    ██▓▓▓▓                                
                                   ██▒▒▓▓                    ██▒▒██                                
                                   ██▒▒██                    ██▓▓██                                
                                     ██▒▒██                ██▓▓██                                  
                                     ██▓▓██                ██▓▓██                                  
                                     ██▓▓██                ██▓▓██                                  
                                     ████                    ████ """)



def game_start(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()

        if char !="\n":
            time.sleep(0.0001)
        else:
            time.sleep(0.05)

os.system("cls")

game_start(message)

num = 6
while num > 0:
    num -= 1
    print (" \n Starting game in {}...".format(num))
    time.sleep(1)

message = "\033[1;33;40m  \n You wake up in the woods after a heavy night of drinking. Your buddy, Jamie, who is a little worse for wear seems to be struggling to remember your name." 

def typewriter(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()

        if char !="\n":
            time.sleep(0.02)
        else:
            time.sleep(1)

os.system("cls")

typewriter(message)

global player_name
player_name = input("\033[2;31;40m \n Remind Jamie what your name is >>: ")

message = "\033[1;36;40m \n Jamie: Right, sorry, how could I forget my best friend {}! Listen, I feel really uneasy, can we get out of here?".format(player_name)

typewriter(message)

inventory = [
"\n A - A torch",
"\n B - A lighter",
"\n C - An axe", 
"\n D - A half-full water bottle", 
"\n E - A mobile phone", 
"\n F - A can of deodorant",
"\n G - A rope"
]
message = "\033[1;33;40m \n \n Noticing Jamie is a little spooked, you make haste to gather up the contents of your camp from the night before. Checking your backpack you see that you have gathered: {}.".format(",".join(inventory))

typewriter(message)

message = "\033[1;33;40m \n \n You both enter a clearing when suddenly loud cracking noises shatter the silence - a giant man eating spider bursts through the trees."

typewriter(message)

message = (r"""
  / _ \
\_\(_)/_/
 _//o\\_ 
  /   \
    """)

typewriter(message)

message = "\033[1;33;40m \n Choose from the following options: \n A - Fight the spider, you are not afraid! \n B - Run away as fast as you can. \n C - Try to talk to the spider, maybe you can reason with it. \n D - Stand still, maybe it will not notice you" 

typewriter(message)

def choice1():
  choice = input("\033[2;31;40m \n Which option would you like to choose - A, B, C or D >>: ")
  if choice.upper() == "B":
    message = "\033[1;33;40m You quickly run away - a smart choice!"
    typewriter(message)

  elif choice.upper() == "A":
    message = "\033[1;33;40m The spider easily kills you, you're just an unarmed person and its a giant armoured vicious monster. Let's try that again.."
    typewriter(message)
    choice1()
  elif choice.upper() == "C":
    message = "\033[1;33;40m The Spider doesn't understand you, and immediately eats you. Let's try that again..."
    typewriter(message)
    choice1()
  elif choice.upper() == "D":
    message = "\033[1;33;40m The Spider easily spots you with its many eyes and proceeds to eat you. Let's try that again..."
    typewriter(message)
    choice1()
  else:
    message = "\033[1;33;40m Sorry, I didn't get that."
    typewriter(message)
    choice1()

choice1()

message = "\033[1;33;40m \n \n You and Jamie immediately turn and flee from the monstrosity. \n It roars and gives chase, but is slower in navigating through the thick trees."
typewriter(message)

message = "\033[1;33;40m \n After 5 minutes of running, you reach a river. "
typewriter(message)

message = "\033[1;33;40m \n You could probably wade through, but the current looks really strong, and there are many sharp rocks downstream."
typewriter(message)

message = "\033[1;33;40m \n You can hear the spider giving a bestial roar not far behind you. You reckon you have 3 minutes before it gets to you."
typewriter(message)

message = "\033[1;33;40m \n Perhaps you could use an item to help you, but do you have the time?"
typewriter(message)

message = "\033[1;33;40m \n \n Choose from one of the following options: \n A - Time is precious, wade through now. \n B - Quickly search your backpack for an item to use."
typewriter(message)

def item1(): 
    item = input("\033[2;31;40m \n What item do you try to use? - A, B, C, D, E, F or G? >>:")
    if item.upper() == "G":
        message = "\033[1;33;40m You chose correctly."
        typewriter(message)
        inventory.remove("\n G - A rope")
    elif item.upper() == "A":
        message = "\033[1;33;40m How would a torch help you in this situation? Maybe try a different item."
        typewriter(message)
        item1()
    elif item.upper() == "B":
        message = "\033[1;33;40m You can't set fire to the river. It's a river. Maybe try a different item."
        typewriter(message)
        item1()
    elif item.upper() == "C":
        message = "\033[1;33;40m You could hack at the river with the axe, but that wouldn't help anything except your stress. Maybe try a different item."
        typewriter(message)
        item1()
    elif item.upper() == "D":
        message = "\033[1;33;40m The river water doesn't look clean, so is best not to drink it. Maybe try a different item."
        typewriter(message)
        item1()
    elif item.upper() == "E":
        message = "\033[1;33;40m Who would you call? Who could help you in such a situation? No. Maybe try a different item."
        typewriter(message)
        item1()
    elif item.upper() == "F":
        message = "\033[1;33;40m This is life and death, it doesn't matter how you smell. Maybe try a different item."
        typewriter(message)
        item1()
    else:
        message = "\033[1;33;40m Sorry, I didn't get that."
        typewriter(message)
        item1()
        
def choice2():
    choice = input("\033[2;31;40m \n What do you do? - A or B? >> ")
    if choice.upper() == "A":
        message = "\033[1;33;40m \n You make it only a few metres into the river when the current pulls you away. \n You soon hit your head on a rock and are instantly killed. \n The spider is watching this from the bank, clanking its pincers in a strange way. \n It's laughing at your demise. Lets try that again.."
        typewriter(message)
        choice2()
    elif choice.upper() == "B":
        message = "\033[1;33;40m \n You look through your backpack. You have: {}".format(",".join(inventory))
        typewriter(message)
        item1()
    else:
        message = "\033[1;33;40m Sorry, I didn't get that."
        typewriter(message)
        choice2()

choice2()

#Scenario 3​

message = "\033[1;33;40m \n \n Using the rope, you tie Jamie to you. With your combined strength and grip, you are able to make it across the river just before the spider arrives."
typewriter(message)

message = "\033[1;33;40m \n The spider wails in fury that you managed to cross the raging torrent, and begins to cross itself."
typewriter(message)

message = "\033[1;33;40m \n \n You need to keep running. You're about to run to the right, when Jamie quickly stops you."
typewriter(message)

message = "\033[1;36;40m \n Jamie: That way looks bad {}, we should run left instead.".format(player_name)
typewriter(message)

message = "\033[1;33;40m \n Jamie seems confident that left is best, but your gut says to go right."
typewriter(message)

message = "\033[1;33;40m \n \n Choose one of the following options: \n A - Jamie seems confident, trust her judgement. Go Left \n B - Jamie is a fool, follow your gut instinct. Go Right"
typewriter(message)

def choice3():
    choice = input("\033[2;31;40m \n What do you do? - A or B? >> ")
    if choice.upper() == "A":
        message = "\033[1;33;40m \n You follow Jamie's reasoning and go left. \n You were right to trust Jamie, as this path seems to be the correct path."
        typewriter(message)
    elif choice.upper() == "B":
        message = "\033[1;33;40m You follow your gut, ignore Jamie, and go right. \n Jamie shouts at you to stop, and you look behind you to see what's wrong. \n Not paying attention to where you are going, you immediately run off a cliff. \n You fall screaming to your messy death on the rocks below. \n At least you're not spider food. Let's try that again..."
        typewriter(message)
        choice3()
    else:
        message = "\033[1;33;40m Sorry, I didn't get that."
        typewriter(message)
        choice3()
        
choice3()

#SCENARIO 6
message = "\033[1;33;40m \n \n As you move deeper into the woods the feeling you are being followed grows, your eyes keep darting through the trees looking for any sign of the monster. \n You feel the ground shake and hear loud thuds behind you - the spider has caught up!"

typewriter(message)

message = "\033[1;33;40m \n \n It quickly moves into your path, blocking you from going any further. You get the feeling you might not be able to run away without a fight this time. Jamie grabs your attention"

typewriter(message)

message = "\033[1;36;40m \n Jamie: {}, do you have anything in the backpack that would help?".format(player_name)

typewriter (message)

message = "\033[1;33;40m \n \n Checking the backpack you see the following items remaining inside: {}".format(",".join(inventory))

typewriter(message)

def item3():
  choice = input("\033[2;31;40m \n Which item would you like to use? >>: A, B, C, D, E or F ")
  if choice.upper() == "A":
    message = "\033[1;33;40m The torch has a limited effect but isn't quite enough.. the spider rushes forward and devours you both.. let's try again."
    typewriter(message)
    item3()
  elif choice.upper() == "B":
    message = "\033[1;33;40m Thinking fire may have an effect you pull out the lighter and try to ignite the spider. Before it catches ablaze you are crushed under its giant legs.. let's try again. "
    typewriter(message)
    item3()
  elif choice.upper() == "C":
    message = "\033[1;33;40m You are no match for the spider in a straight up battle, try something else!"
    typewriter(message)
    item3()
  elif choice.upper() == "D":
    message = "\033[1;33;40m You throw the water bottle at the spider.. it has almost no effect, if anything enraging the monster further. Let's try again. "
    typewriter(message)
    item3()
  elif choice.upper() == "E":
    message = "\033[1;33;40m You pull out your mobile phone planning to call for help. Unfortunately you are eaten before help can arrive. Let's try again."
    typewriter(message)
    item3()
  elif choice.upper() == "F":
    message = "\033[1;33;40m \n Grabbing the can of deodorant you target the spiders many eyes with the toxic gas. Success! The spider rears backwards in pain having been blinded by your attack."
    typewriter(message)
    inventory.remove("\n F - A can of deodorant")
  else:
    message = "\033[1;33;40m Sorry, I didn't get that."
    typewriter(message)
    item3()

item3()

#SCENARIO 7
message = "\033[1;33;40m \n The spider is suffering from deodorant burns to its eyes and is thrashing around in pain. You decide to withdraw for the time being."

typewriter(message)

message = "\033[1;36;40m \n \n Jamie: Quick, let's climb a tree! Maybe we can climb across the branches!"

typewriter(message)

message = "\033[1;33;40m \n \n Choose from the following options:\n A - Ignore Jamie and try to run past the spider \n B - Follow Jamies advice and climb a tree" 

typewriter(message)

def choice7():
  choice = input("\033[2;31;40m \n Which option would you like to choose - A or B >>: ")
  if choice.upper() == "B":
    message = "\033[1;33;40m \n You climb the tree finding temporary safety."
    typewriter(message)
  elif choice.upper() == "A":
    message = "\033[1;33;40m The spider is thrashing about wildly, you cannot get past. Perhaps try Jamies suggestion?"
    typewriter(message)
    choice7()
  else:
    message = "\033[1;33;40m Sorry, I didn't get that."
    typewriter(message)
    choice7()

choice7()

#Scenario8

message = "\033[1;33;40m \n After a quick breather and a moment to gather your thoughts, you decide to create a distraction to allow you to escape. \n \n Choose from the following options: \n A - Play music on your mobile and throw it into the trees. \n B - Use the torch to blind the spider."

typewriter(message)

def choice8():
  choice = input("\033[2;31;40m \n Which option would you like to choose - A or B >>: ")
  if choice.upper() == "A":
    message = "\033[1;33;40m \n The spider is still suffering from the burns. The loud sounds coming from the mobile successfully catch its attention and it chases the phone into the trees. You take advantage of this to climb down from the tree and continue into the forest."
    typewriter(message)
  elif choice.upper() == "B":
    message = "\033[1;33;40m The spider is already blinded from the deodorant burns to its eyes. The torch has no effect."
    typewriter(message)
    choice8()
  else:
    print("\033[1;33;40m Sorry, I didn't get that. Please choose option A or B.")
    choice8()

choice8()

#Scenario 9

message = "\033[1;33;40m \n \n You both approach a bridge. Upon inspection you can see it´s old and in disrepair and may not be safe to cross."
typewriter(message)
message = "\033[1;33;40m \n \n Choose from the following options: \n A - You think you can see the way out of the forest, rush on the other side of bridge! \n B - Discuss it with Jamie \n C - Start to freak out \n D - Try to find something in your backpack that could help "
typewriter(message)

# def new(): 
#   choice = input("\033[2;31;40m \n \n    you died would you like to try it again [NEW] start over or [LAST] repeat last scene?    ")
#   if choice.upper == "new":
#     message = "\033[1;34;40m \n Lets start new game!"
#     typewriter(message)
#     choice10()
#   elif choice.upper == "last":
#     message = "Lets Try again!"
#     typewriter(message)
#     choice9()
# global player_name 
# player_name = " "   

def choice9():
  choice = input("\033[2;31;40m \n Which option would you like to choose - A, B, C or D >>: ")
  if choice.upper() == "B":
    message = "\033[1;33;40m \n You talk to Jamie and she suggests to go one by one to make sure to be safe... \n SUCCESS! You both make it to other side"
    typewriter(message)
  elif choice.upper() == "A":
    message = "\033[1;33;40m You rushed on the other side but suddenly the bridge broke, you fall and die. Lets try again.."
    typewriter(message)
    choice9()
  elif choice.upper() == "C":
    message = "\033[1;33;40m You started freaking out but it doesnt help you. Try again"
    typewriter(message)
    choice9()
  elif choice.upper() == "D":
    message = "\033[1;33;40m Too bad, you can't see anything that could help. Try again"
    typewriter(message)
    choice9()
  else:
    message = "\033[1;33;40m Sorry, I didn't get that."
    typewriter(message)
    choice9() 
choice9()

#Scenario 10
message = "\033[1;33;40m \n \n Having passed the bridge you see an entrance to a cave blocked by spider webs."
typewriter(message)
message = "\033[1;33;40m \n \n Choose from the following options: \n A - Slap Jamie for no reason  \n B - Try to enter the cave \n C - Start to sing your favorite song " 
typewriter(message)
def choice10():
  choice = input("\033[2;31;40m \n Which option would you like to choose - A, B or C >>: ")
  if choice.upper() == "A":
    message =  "\033[1;33;40m \n Jamie is completely freaking out! You hear her mumbling 'burn it' Suddenly you remember you have a lighter in your backpack "     
    typewriter(message)  
  elif choice.upper() == "B":
    message = "\033[1;33;40m You tried to enter into the cave but you become stuck in the webs! Luckily Jamie manages to free you.. try something else."
    typewriter(message)
    choice10()
  elif choice.upper() == "C":
    message = "\033[1;33;40m Great {}, you started to sing your favorite song - sadly it had no effect! ".format(player_name)
    typewriter(message)
    choice10()
  else:
    message = "\033[1;33;40m Sorry, I didn't get that."
    typewriter(message)
    choice10() 
choice10()
#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
message = "\033[1;33;40m \n \n Choose from the following options: \n A - Slap Jamie again for no reason  \n B - Try to enter the cave \n C -  Use lighter to burn webs down " 
typewriter(message)

def choice11():
  choice = input("\033[1;31;40m \n \n Which option would you like to choose - A, B or C >>: ")
  if choice.upper() == "C":
    message = "\033[1;33;40m Great {} ! All webs burned down. You are entering the most terrifying cave you ever seen".format (player_name) 
    typewriter(message)
    inventory.remove("\n B - A lighter")
  elif choice.upper() == "B":
    message = "\033[1;33;40m You tried to enter into the cave but you just get stuck in the web! Jamie manages to free you - let's try something else.."
    typewriter(message)
    choice11()
  elif choice.upper() == "A":
    message = "\033[1;33;40m You raise your hand to slap Jamie again but realise it wouldn't help.. let's try something else.."
    typewriter(message)
    choice11()
    
  else:
    print("Sorry, I didn't get that.Try again! ")
    choice11() 

choice11()
has_sword = True
message = "\033[1;33;40m \n \n You and Jamie are now in the Spider's lair, and the beast is before you. It appears still injured after the deodrant attack. \n It may be blinded, but it can still smell you, and is slowly scuttling towards you, sniffing the air as it goes. \n You can see a sharp ray of light behind it. \n It's a small tunnel, and perhaps a proper escape from the cursed spider."
typewriter(message)
if has_sword:
    message = "\033[1;33;40m \n \n You are reminded by the weight on your back of the presence of the axe. \n With the beast blinded maybe now is the moment to attack and finish it once and for all. \n On the other hand, even blinded, it is still a formidable creature, with quick reflexes and strong armour."
    typewriter(message)

message = "\033[1;33;40m \n \n If it can be distracted for long enough, then either you or Jamie could have enough time to dart around it and escape for good. \n One of you might have to sacriice themselves."
typewriter(message)

message = "\033[1;33;40m \n \n Choose one of the following options: \n A - Save yourself. \n B - Save Jamie. \n C - It's now or never - Attack!"
typewriter(message)

def choice12():
    if has_sword:
        choice = input("\033[2;31;40m \n \n What do you do? - A, B or C? >> ")
        if choice.upper() == "A":
            message = "\033[1;33;40m You give Jamie a sharp shove into the spider. \n \033[1;36;40m Jamie: 'Wait {}! No! No! AHHHHHHHHHH!' \n \033[1;33;40m You quickly dart around the Spider, trying to ignore the screams and bestial roars as Jamie is devoured by the Spider.".format(player_name)
            typewriter(message)
            message = "\033[1;33; \n 40m You scuttle through the tunnel and emerge on the other side in a bright clearing. You're finally out of the forest, and free from the Spider. \n \n You survived...but at what cost? \n \n"
            typewriter(message)
        elif choice.upper() == "B":
            message = "\033[1;33;40m Before Jamie can say anything, you close your eyes and step forward. \n \033[1;36;40m Jamie:  '{}! NOOOOOOOOOOOO!' \n \033[1;33;40m The spider imediately pounces on you and begins ripping out and feasting on your insides".format(player_name.upper())
            typewriter(message)
            message = "\033[1;33;40m \n Before you black out, you see through the Spider's legs that Jamie has reached the tunnel and is crawling to freedom. \n \n You did the right thing in the end...even if you didn't ultimately survive. \n \n "
        elif choice.upper() == "C":
            message = "\033[1;33;40m With a mighty roar of fury, you charge the Spider with your axe! \n Blinded, it is unable to react fast enough as you plant the weapon in its head and stab into its brain. Foul black blood begins to ooze out of the wound, and with a quick spasm, it curls up into a ball. \n \033[1;36;40m Jamie:'Oh my god {}! You killed it!' \033[1;33;40m \n Together, you and Jamie crawl through the tunnel and reach your freedom, leaving the Spider behind you for good. \n You and Jamie have both survived, and you have slain a foul monster! \n \n ".format(player_name)
            typewriter(message)
        else:
            message = "\033[1;33;40m Sorry, I didn't get that."
            typewriter(message)
            choice12()
    else:
        choice = input("\033[2;31;40m \n What do you do? - A or B? >> ")
        if choice.upper() == "A":
            message = "\033[1;33;40m You give Jamie a sharp shove into the spider. \n Jamie: \033[1;36;40m 'Wait {}! No! No! AHHHHHHHHHH!' \n \033[1;33;40m You quickly dart around the Spider, trying to ignore the screams and bestial roars as Jamie is devoured by the Spider.".format(player_name)
            typewriter(message)
            message = "\033[1;33;40m \n You scuttle through the tunnel and emerge on the other side in a bright clearing. You're finally out of the forest, and free from the Spider. \n \n You survived...but at what cost? \n \n "
            typewriter(message)
        elif choice.upper() == "B":
            message = "\033[1;33;40m Before Jamie can say anything, you close your eyes and step forward. \n Jamie: \033[1;36;40m '{}! NOOOOOOOOOOOO!' \n \033[1;33;40m The spider imeediately pounces on you and begins ripping out and feasting on your insides \n \n \n ".format(player_name.upper())
            typewriter(message)
            message = "\033[1;33;40m \n Before you black out, you see through the Spider's legs that Jamie has reached the tunnel and is crawling to freedom. \n \n You did the right thing in the end...even if you didn't ultimately survive. \n \n "
            typewriter(message)
        else:
            message = "\033[1;33;40m Sorry, I didn't get that."
            typewriter(message)
            choice12()

choice12()

message = (r""" 
           ,  . .,  °          .·¨'`;        ,.·´¨;\                  _,.,  °                                      _,.,  °               ,.         ,·´'; '      ;'*¨'`·- .,  ‘            
   ;'´    ,   ., _';\'       ';   ;'\       ';   ;::\          ,.·'´  ,. ,  `;\ '                             ,.·'´  ,. ,  `;\ '        ;'´*´ ,'\       ,'  ';'\°     \`:·-,. ,   '` ·.  '      
   \:´¨¯:;'   `;::'\:'\      ;   ;::'\      ,'   ;::';       .´   ;´:::::\`'´ \'\                           .´   ;´:::::\`'´ \'\        ;    ';::\      ;  ;::'\      '\:/   ;\:'`:·,  '`·, '   
     \::::;   ,'::_'\;'      ;  ;::_';,. ,.'   ;:::';°     /   ,'::\::::::\:::\:'                         /   ,'::\::::::\:::\:'      ;      '\;'      ;  ;:::;       ;   ;'::\;::::';   ;\   
         ,'  ,'::;'  ‘      .'     ,. -·~-·,   ;:::'; '    ;   ;:;:-·'~^ª*';\'´                          ;   ;:;:-·'~^ª*';\'´       ,'  ,'`\   \      ;  ;:::;       ;  ,':::;  `·:;;  ,':'\' 
         ;  ;:::;  °      ';   ;'\::::::::;  '/::::;      ;  ,.-·:*'´¨'`*´\::\ '                         ;  ,.-·:*'´¨'`*´\::\ '      ;  ;::;'\  '\    ;  ;:::;       ;   ;:::;    ,·' ,·':::; 
         ;  ;::;'  ‘        ;  ';:;\;::-··;  ;::::;      ;   ;\::::::::::::'\;'                         ;   ;\::::::::::::'\;'      ;  ;:::;  '\  '\ ,'  ;:::;'       ;  ;:::;'  ,.'´,·´:::::; 
         ;  ;::;'‚          ':,.·´\;'    ;' ,' :::/  '     ;  ;'_\_:;:: -·^*';\                         ;  ;'_\_:;:: -·^*';\     ,' ,'::;'     '\   ¨ ,'\::;'       ':,·:;::-·´,.·´\:::::;´'  
         ',.'\::;'‚           \:::::\    \·.'::::;        ';    ,  ,. -·:*'´:\:'\°                       ';    ,  ,. -·:*'´:\:'\°   ;.'\::;        \`*´\::\; °       \::;. -·´:::::;\;·´     
          \::\:;'‚             \;:·´     \:\::';          \`*´ ¯\:::::::::::\;' '                       \`*´ ¯\:::::::::::\;' '  \:::\'          '\:::\:' '          \;'\::::::::;·´'        
           \;:'      ‘                    `·\;'             \:::::\;::-·^*'´                              \:::::\;::-·^*'´         \:'             `*´'‚               `\;::-·´            
             °                              '                `*´¯                                         `*´¯                                                                         
    """)
game_start(message)
message = "\033[1;33;40m \n THE FOREST"
typewriter(message)
message = "\033[1;33;40m \n \n Written and Developed by the Electric Chameleons \n George Tilley \n Ollie Morris \n Matthew Ackerley \n Zdenek Slehubr"
typewriter(message)
message = "\033[1;33;40m \n \n Made using Python in Visual Studio Code"
typewriter(message)
message = "\033[1;33;40m \n \n Produced by CodeNation"
typewriter(message)
message = "\033[1;33;40m \n \n Credits for Ascii Art to the people who made them"
typewriter(message)
message = "\033[1;33;40m \n \n Special Thanks to Liam"
typewriter(message)
message = "\033[1;33;40m \n \n No spiders were harmed in the making of this game"
typewriter(message)

message = (r'''

           ;               ,           
         ,;                 '.         
        ;:                   :;         
       ::                     ::       
       ::                     ::       
       ':                     :         
        :.                    :         
     ;' ::                   ::  '     
    .'  ';                   ;'  '.     
   ::    :;                 ;:    ::   
   ;      :;.             ,;:     ::   
   :;      :;:           ,;"      ::   
   ::.      ':;  ..,.;  ;:'     ,.;:   
    "'"...   '::,::::: ;:   .;.;""'     
        '"""....;:::::;,;.;"""         
    .:::.....'"':::::::'",...;::::;.   
   ;:' '""'"";.,;:::::;.'""""""  ':;   
  ::'         ;::;:::;::..         :;   
 ::         ,;:::::::::::;:..       :: 
 ;'     ,;;:;::::::::::::::;";..    ':. 
::     ;:"  ::::::"""'::::::  ":     :: 
 :.    ::   ::::::;  :::::::   :     ; 
  ;    ::   :::::::  :::::::   :    ;   
   '   ::   ::::::....:::::'  ,:   '   
    '  ::    :::::::::::::"   ::       
       ::     ':::::::::"'    ::       
       ':       """""""'      ::       
        ::                   ;:         
        ':;                 ;:"         
          ';              ,;'           
            "'           '"             
              ' 
''')
game_start(message)