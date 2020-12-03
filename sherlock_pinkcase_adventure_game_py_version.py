"""
Created : Thu Oct 20 17:52:46 2020


@author: madhuparna upadhyay
"""
"""
    DocString:
    
    A) Introduction:
    This game is based on the famous detective character Sherlock Holmes and the story-THE PINK SUITCASE.
    It consists of four stages, and also has defined functions
    for start, win, and lose. This game has a mysterious situation in the case mystery, and requires a
    slight amount of idea about Sherlock the how brilliant he can be.
    
    Round 1:'ROOM WITH A NOTE' - Decode the floor clue.
    Round 2:'SUITCASE AND A PHONE' - Crack the suitcase.
    Round 3:'BOTTLE WITH CAPSULE' - Guess the correct capsule to save Ms.Wilston.
    Round 'LUCKY CHANCE': - This round only pops up when you miss on an important clue. 
    
    B) Known Issues and/or Errors:
    None.
    
"""

# importing packages for time, random and color
import time, random, string
from random import randint
from colorama import Fore
from sys import exit

def begingame():

    # global parameters
    global detective_name
    global profession
    global average_type_speed
    
    # defining average typing speed for time function
    average_type_speed = 100
    
    ## These variables are defined as strings to contains texts as the set of instructions to be display to player.
    introduction_text = "It's the winter season in LONDON, Jennifer Wilston: A high profile person is filed missing from the town.SHERLOCK is investigating the case, but people are panicking and the press is asking questions."
    introduction_text3 = "SHERLOCK is in a crucial situation and wants to solve the case and rescue the people. \U0001f600"
    
    # using color coding for few texts
    print(f"""\n{Fore.GREEN}""")

    # for loop to slowly display the instructions for the player
    for letter in introduction_text:
        print(letter, sep='', end='')
        time.sleep(0.05)
    
    print(f"""Mr.Holmes needs help,ARE YOU READY?""")
    print(f"""\n\n{'*'*80}\n\n""")
    # Invoking sleep function based on random and average typing speed
    self_sleep()
    
    # for loop to slowly display the instructions for the player
    print(f"""You have been invited by Mr.Holmes to assist in the case.\U0001f600\n""")
    
    # prompt input to the player
    detective_name = input(prompt="Please tell him your NAME: \n")
    
    #conditional statement for blank or no text input for name
    if (len(detective_name)<=0):
        detective_name = 'X'
        print(f"""\n{Fore.GREEN}You did not enter a proper name, No worries we call you {detective_name}{Fore.RESET}\n""")
    
    print(f"{Fore.GREEN}Welcome, detective {detective_name}! We hope you can solve the case with Mr. HOLMES{Fore.RESET}\n")
    print(f"{Fore.BLUE}SHERLOCK {Fore.RESET}: Can you tell me more specifics about you {detective_name}\n")
    profession = input(prompt="Tell him, What's your profession ?\n")
    print(f"""\n{Fore.GREEN}NOW COMMON DETECTIVE {detective_name} hurry up!.\n{Fore.RESET}\n{'*'*80}""")

    #conditional statement for blank or no text input for profession
    if(len(profession)<=0):
        profession = 'Y'
        print("\n Well you didn't say your profession details. We will assume Y\n\n")
    
    for letter3 in introduction_text3:
        print(letter3, sep='', end='')
        time.sleep(0.05)
    
    input(prompt="\n<Press enter to begin solving the mystery>\n")
    
    # Function call for sleep iteration based on typing speed
    self_sleep()

    # Function call for the first game round to begin
    crime_scene_with_note()

#### 
#
#ROUND 1: crime_scene_with_note
#
####

def crime_scene_with_note():

    # storing all acceptable local variables of and in a list as option1,2,3
    # using level1 options in list and scene 1 text to be displayed as a string
    option1 = ["say 'rachel' might be the clue", "say rachel", "rachel", "one","1"]
    option2 = ["ask sherlock the meaning", "ask sherlock", "ask meaning", "two","2"]
    option3 = ["analyze 'rache' with german meaning of 'revenge'","3",
                 "analyze 'rache'", "german meaning of 'revenge'","three"
                 "analyze", "analyse", "german meaning", "revenge"]
    level1_avail_options = ["1) Say 'RACHEL' might be the clue.",
                            "2) Ask Sherlock the meaning.",
                            "3) Analyze 'RACHE' with german meaning of 'REVENGE'."]
    scene1_text = "You have only two chances in this scene to decode the clue"

    print(f"""Hey {detective_name} you have just entered the CRIME SCENE with SHERLOCK.\nThis is where Jeniffer was last seen.{Fore.GREEN}\n""")
    
    for lettr in scene1_text:
        print(lettr, sep='', end='')
        time.sleep(0.05)

    # loops concept: while for giving 2 chances to the user in round 1
    chance = 2
    while chance > 0:
        print(f"""\n\n{Fore.BLUE}SHERLOCK {Fore.RESET}: I am checking on every detail in the room,\nbut wait what is that scratch spelled 'RACHE', what do you think?\n""")
        
        # for loop to print array value with 3 choices
        for available_option in level1_avail_options:
            print(f"""{Fore.GREEN}{available_option}{Fore.RESET}""")
        
        self_sleep()
        your_choice = input(prompt="\n")
        your_choice = your_choice.lower()
        
        # try except handling the input of user decisions
        try:
            if your_choice in option1:

                # conditional statement for correct clue
                print(f"""\n{Fore.BLUE}SHERLOCK {Fore.RESET}: Okay! Impressing {detective_name}, 'RACHEL' it is.\n""")
                input(prompt="<Press enter to continue solving mystery>\n")
                # function call for level 2
                suitcase_and_phone()
                break

            elif your_choice in option2:
                
                # condition for wrong choice but another chance
                print(f"""\n{Fore.BLUE}SHERLOCK {Fore.RESET}: Shocking !! {detective_name} What might be inside your funny litlle brains?\n FIX IT WHILE YOU CAN !\n""")
                chance-=1
                print(f"""You have {chance} chances remaining""")

            elif your_choice in option3:
                
                # condition for wrong choice but another chance
                print(f"""\n{Fore.BLUE}SHERLOCK {Fore.RESET}: {detective_name} so your anasysis is that 'RACHE' denotes 'The person who is kidnapping is looking for REVENGE.'\n FIX IT WHILE YOU CAN !""")
                chance-=1
                print(f"""You have {chance} chances remaining""")

            else:
                if chance == 2:
                    print("It seems you did not give a proper reply. But it's alright ! Sherlock gives you one more chance\n")
                    chance-=1
                elif chance == 1:
                    chance-=1
                else:
                    fail()
                    break

            if(chance==0):
                fail()

        except KeyboardInterrupt:
            exit(0)
        except BaseException:
            print("")
        except:
            print("It seems you did not enter a proper reply. But it's alright ! Sherlock gives you one more chance\n")
            chance-=1

###
#
# ROUND 2: crime_scene_with_suitcase_and_phone
#
###
def suitcase_and_phone():

    # local variables for options and acceptable choices
    suitcase_option1 = ["search inside suitcase", "search", "suitcase", "one", "1"]
    suitcase_option2 = ["look for her cell phone","two","2","cell phone", "look for her cell"]
    suitcase_option3 = ["suggest rachel as a codeword", "rachel","three","rachel codeword", "codeword","3"]
    level2_avail_options = ["1) Search inside suitcase",
                            "2) Look for her cell phone",
                            "3) Suggest RACHEL as a codeword"]
    
    print(f"""{Fore.BLUE}SHERLOCK {Fore.RESET}: Another Mystery Situtation {detective_name}\n\nAlthough I should mention, you were correct about RACHEL, she was the daughter of the victim,\nI followed some more tracks and got a suitcase. How would you investigate ?You have these options...\n""")
    
    # for loop for user available option printing
    scene1_text = "CAREFUL you have only one chance in this scene to decode the clue"
    print(f"""{Fore.GREEN}""")
    
    # for loop to slowly display the instructions for the player
    for lett in scene1_text:
        print(lett, sep='', end='')
        time.sleep(0.05)
    
    print("\n")
    for option in level2_avail_options:
        print(f"""{Fore.GREEN}{option}{Fore.RESET}""")
    suitcase_choice = input(prompt="Your option?\n")
    suitcase_choice = suitcase_choice.lower()

    # try except handling the input of user decisions
    try:
        if suitcase_choice in suitcase_option1:
            print(f"""\n{Fore.BLUE}SHERLOCK {Fore.RESET}: You are too slow {detective_name}\n""")
            self_sleep()
            input(prompt="<Press enter to continue solving mystery>\n")
            lucky_chance()

        elif suitcase_choice in suitcase_option2:
            print(f"""\n{Fore.BLUE}SHERLOCK {Fore.RESET}: {detective_name} You are on right track but cell phone is yet to be tracked.\n""")
            self_sleep()
            input(prompt="<Press enter to continue solving mystery>\n")
            lucky_chance()
        
        elif suitcase_choice in suitcase_option3:
            print("\nYou just chose {}".format("".join(suitcase_choice)))
            print(f"""\n{Fore.BLUE}SHERLOCK {Fore.RESET}: AWESOME Breakthough !! you suggested codeword. I am stunned.""")
            self_sleep()
            input(prompt="<Press enter to continue solving mystery>\n")
            bottle_with_capsule()

        else:
            print(f"""{Fore.BLUE}SHERLOCK {Fore.RESET}: Are joking about the situation detective {detective_name} ?\n""")
            fail()
    # Key board interrupt for players to stop executing forcibly in other terminals
    except KeyboardInterrupt:
        exit(0)
    except Exception:
        print(f"""{Fore.BLUE}SHERLOCK {Fore.RESET}: If you tring to be goofy, by giving wrong inputs.\nYou get no more chance ! THANK YOU ! BYE {detective_name} !\n""")
        fail()

# ROUND 3: Crime-scene_with_bottle_and_capsule
def bottle_with_capsule():

    # local variables for options and acceptable choices and text to be displayed stored as string
    level3_option1 = ['a', 'bottle a', '1) bottle a', 'one', '1']
    level3_option2 = ['b', 'bottle b', '2) bottle b', 'two', '2']
    level3_avail_options = ["1) Bottle A", "2) Bottle B"]
    scene3_text2 = "As you enter the abandoned building, you find Ms. Wilston, but the criminal gives you a choice, says if he wins he demands money to spare everyone, but if SHERLOCK wins he will surrender"
    
    print(f"""\n{Fore.BLUE}SHERLOCK {Fore.RESET}: CLOSE ENOUGH TO FIND Ms. Wilston""")
    input(prompt="<Press enter to continue solving mystery>\n")
    print(f"""{Fore.GREEN}The CODEWORD and the email address in the suitcase unlocked her laptop.\nYeahhhh..It was tracked to the outskirts of LONDON.TIME TO RUN...{Fore.RESET}""")
    print(f"""\n\nBE VERY CAREFUL, One wrong move can be dangerous !""")
    
    # for loop to slowly display the instructions for the player
    for letr in scene3_text2:
        print(letr, sep='', end='')
        time.sleep(0.05)
    
    print(f"""\nGUESS: There are 2 identical bottles with two capsules, one is a poison other is a fake. Which one would you choose?\n\n""")
    print(f"""{Fore.GREEN}\nYOU WILL HAVE ONLY ONE CHANCE TO CRACK THIS !\n{Fore.RESET}""")
    
    for opinion in level3_avail_options:
        print(f"""{Fore.GREEN}{opinion}{Fore.RESET}""")

    bottle_choice = input(prompt="\nWhich bottle is your choice??\n")
    bottle_choice = bottle_choice.lower()
    
    # random string in ascii letter range of a or b
    bottle = random.choice(string.ascii_letters[0:2])
    print("\nHere : The correct option was in bottle:", bottle)
    # try except handling the input of user decisions

    try:
        # conditional statement to check if input matches to random letter a or b
        if bottle_choice in level3_option1:
            if bottle == 'a':
                win()
            else:
                fail()
        elif bottle_choice in level3_option2:
            if bottle == 'b':
                win()
            else:
                fail()
        else:
            print(f"""{Fore.BLUE}SHERLOCK {Fore.RESET}: You are tring to be goofy, in a wrong situation. You LOST! THANK YOU ! BYE {detective_name} ! \n""")
            fail()
    # Key board interrupt for players to stop executing forcibly in other terminals
    except KeyboardInterrupt:
        exit(0)
    except Exception:
        print(f"""{Fore.BLUE}SHERLOCK {Fore.RESET}: You are tring to be goofy, in a wrong situation. You LOST! THANK YOU ! BYE {detective_name} !\n""")
        fail()

####
#
# Round Lucky chance
#
###
def lucky_chance():

    # random integer between 1 to 5
    track_search = randint(1, 5)

    # local varibales for acceptable options
    level_lucky_option1 = ['call the police','call','police', 'one', '1']
    level_lucky_option2 = ["look at nearby sidewalks", "sidewalks", "look","2", "two", "nearby sidewalks"]
    print(f"""{Fore.BLUE}SHERLOCK {Fore.RESET}: You are yet to learn some skills, and too slow to process {detective_name}\nSo go on and find the clues which may be random but you have to try your luck.\n""")
    print(f"""{Fore.GREEN}1) Call the police.\n2) Look at nearby sidewalks for kidnapper missed clues.{Fore.RESET}""")
    track = input('\nWhat would be your approach ?\n')
    
    # try except handling the input of user decisions
    try:
        if track.lower() in level_lucky_option1:
            #random number 1,2,3 is good luck
            if ((track_search == 1) or (track_search == 2) or (track_search == 3)):
                print(f"""{Fore.BLUE}SHERLOCK {Fore.RESET}: Amazing ! Come on now, you tracked some taxi drivers as suspects""")
                bottle_with_capsule()
            else:
                fail()
        elif track.lower() in level_lucky_option2:
            #random number 4, 5 is player looses
            if ((track_search == 4) or (track_search == 5)):
                print(f"""{Fore.BLUE}SHERLOCK {Fore.RESET}: Amazing ! Come on now, you tracked some taxi drivers as suspects""")
                bottle_with_capsule()
            else:
                fail()
        else:
            print(f"""{Fore.BLUE}SHERLOCK {Fore.RESET}: You tring to be goofy, by giving wrong inputs. You get no more chance ! THANK YOU ! BYE {detective_name} ! \n""")
            fail()
    # Key board interrupt for players to stop executing forcibly in other terminals
    except KeyboardInterrupt:
        exit(0)
    except Exception:
        print(f"""{Fore.BLUE}SHERLOCK {Fore.RESET}: You tring to be goofy, by giving wrong inputs. You get no more chance ! THANK YOU ! BYE {detective_name} !\n""")
        fail()

# shortedned function just for sleep time
def self_sleep():
    time.sleep(random.random()*10.0/average_type_speed)

# Play again function for player
def play_again():
    fresh_start = input(prompt='\nWould you like to play from fresh again ??\n yes or no\n')

    # try except handling for user inputs
    try:
        fresh_start = fresh_start.lower()
        if fresh_start == 'yes':
            begingame()
        else:
            print(f"""THANK YOU for playing {detective_name} !""")
            quit()
    except KeyboardInterrupt:
        exit(0)
    except Exception:
        print(f"""There might have been an error in your reply.\n Anyway THANK YOU playing {detective_name} !""")
        exit(0)

# function for win Scenario
def win():
    print(f""" You win {detective_name}!!! You get a promotion in your profession {profession}""")
    print("   _____   ______    ___     _    _______   _________       ___    _________   ________ ")
    print("  /  ___| /  __  \  |   \   | |  /  _____| |   __    \     / _ \  |___   ___| /  ______| ")
    print(" |  |    |  |  |  | | |\ \  | | | |   ___  |  |__| __/    / /_\ \     | |     | |______  ")
    print(" |  |    |  |  |  | | | \ \ | | | |  |_  | |  |  \  \    / ____  \    | |     \_____   | ")
    print(" |  |___ |  |__|  | | |  \ \| | | |____| | |  |   \  \  / /    \  \   | |      _____|  | ")
    print("  \_____| \______/  |_|   \___|  \_______/ |__|    \__\/_/      \__\  |_|     |________| ")
    print("                                                                                         ")
    play_again()

# fail function for fail cases
def fail():
    print(f"""OHHHH NO!!. {detective_name} You made Sherlock fail the case !! You Lost.""")
    print("                                                      ")
    print("  __________      ___      ____      ____   _______  ")
    print(" /   _______|    / _ \     |   \    /   |  |  _____| ")
    print(" |  |   ____    / /_\ \    |    \  /    |  | |___    ")
    print(" |  |  |_   |  /  ___  \   |  |\ \/ /|  |  |  ___|   ")
    print(" |  |____|  | /  /   \  \  |  | \__/ |  |  | |_____  ")
    print(" \__________//__/     \__\ |__|      |__|  |_______| ")
    print("   ______   ___        ___   ________    _________      ")
    print("  /  __  \  \  \      /  /  |  _____|   |   __    \     ")
    print(" |  |  |  |  \  \    /  /   | |____     |  |__| __/     ")
    print(" |  |  |  |   \  \  /  /    |  ____|    |  |  \  \      ")
    print(" |  |__|  |    \  \/  /     | |_____    |  |   \  \     ")
    print("  \______/      \____/      |_______|   |__|    \__\    ")
    print("                                                       ")
    play_again()
    
# main function call to begin execution of code
begingame()