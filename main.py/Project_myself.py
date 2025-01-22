import random
import time
import os
from tabulate import tabulate
import vlc

mp3_dir = ".mp3's"

# Create media players with os.path.join
feast = vlc.MediaPlayer(os.path.join(mp3_dir,"End" ,"feast.mp3"))
respect = vlc.MediaPlayer(os.path.join(mp3_dir,"Professor's.mp3's", "respect.mp3"))

# For the Hogwarts music, ensure the subdirectory is correctly handled
hogwarts_music_dir = os.path.join(mp3_dir, "Hogwards_music.mp3")
hogwarts = vlc.MediaPlayer(os.path.join(hogwarts_music_dir, "music.mp3"))

hogwarts.play()

# Define base directories
houses_dir = os.path.join(".mp3's", "Houses_Announcment.mp3's")
professors_dir = os.path.join(".mp3's", "Professor's.mp3's")

# Create media players with os.path.join
Gryffindor_SONG = vlc.MediaPlayer(os.path.join(houses_dir, "Gryffindor.mp3"))
Slytherin_SONG = vlc.MediaPlayer(os.path.join(houses_dir, "Slytherin.mp3"))
Hufflepuff_SONG = vlc.MediaPlayer(os.path.join(houses_dir, "Hufflepuff.mp3"))
Ravenclaw_SONG = vlc.MediaPlayer(os.path.join(houses_dir, "Ravenclaw.mp3"))

starting = vlc.MediaPlayer(os.path.join(professors_dir, "starting.mp3"))
first_announcment = vlc.MediaPlayer(os.path.join(professors_dir, "first_anncounment.mp3"))



voice_teacher = [
    os.path.join(".mp3s", "Professor's.mp3's", "qurriell.mp3"),
    os.path.join(".mp3s", "Professor's.mp3's", "lockhart.mp3"),
    os.path.join(".mp3s", "Professor's.mp3's", "lupin.mp3"),
    os.path.join(".mp3s", "Professor's.mp3's", "moddy.mp3"),
    os.path.join(".mp3s", "Professor's.mp3's", "umbridge.mp3"),
    os.path.join(".mp3s", "Professor's.mp3's", "snape.mp3")
]


base_dir = os.path.join(".mp3's", "Motivation.mp3's")

# List of files using os.path.join
Albus_speech = [
    os.path.join(base_dir, "motive1.mp3"),
    os.path.join(base_dir, "motive2.mp3"),
    os.path.join(base_dir, "motive3.mp3"),
    os.path.join(base_dir, "motive4.mp3"),
    os.path.join(base_dir, "motive5.mp3"),
    os.path.join(base_dir, "motive6.mp3"),
    os.path.join(base_dir, "motive7.mp3")
]

parv = random.randint(0,5)


 
# Houses_1 = ['GARUDDWAR', 'NAAGSHAKT', 'MEHENATKAS', 'CHEELGHAAT']
Dark_Arts_teacher = ["Professor Quirinus Quirrell", "Professor Gilderoy Lockhart", "Professor Remus Lupin", "Professor Alastor 'Mad-Eye' Moody ", "Professor Dolores Umbridge", "Professor Severus Snape"]
professor = Dark_Arts_teacher[parv]


House1 = ['Gryffindor', 'Slytherin', 'Hufflepuff', 'Ravenclaw']

# Qualities

Gryffindor = "Courage, bravery, daring, and chivalry."
Slytherin= "Ambition, cunning, resourcefulness, and leadership."
Hufflepuff = "Hard work, loyalty, patience, and fair play."
Ravenclaw = "Intelligence, creativity, wisdom, and wit."

Qualities = [Gryffindor,Slytherin,Hufflepuff,Ravenclaw]
 
  

print("\n                   ******* Participate in Hogwarts Sorting Ceremony *******")
time.sleep(2)
print("""\nInstructions For This Ceremony :\n\n1. Professor McGonagall has to write his name in the list first\n2. Each student is called forward, and the Sorting Hat is placed on their head.\n   the Hat determines their house based on their answers.\n3. The Hat announces the student's house aloud.\n4. The student joins their house table amid cheers.""")

Student_name = input("\nEnter Your Name so Professor McGonagall can call you : ")
time.sleep(2)
print(f"\n       'Professor McGonagall' is calling  Now ............")
time.sleep(3)
print(f"\n{Student_name}! from the list of first-year students")
time.sleep(3)
print(f"\n{Student_name}! walk up to the front of the Great Hall, sit on the stool, and the Sorting Hat is placed on his head")

#   Questions
Question_1 = input("\nQuestion 1 - Do you prefer daring adventures or studying new spells? (adventure/spells):  ")
Question_2 = input("Question 2 - Would you rather have power and control or make new friends? (power/friends):  ")
Question_3 = input("Question 3 - Do you value loyalty or creativity more? (loyalty/creativity):  ")
Question_4 = input("Question 4 - Do you prefer bravery or cunning to get what you want? (bravery/cunning):  ")


house = ""
# Check all combinations
if Question_1 == "adventure":
    if Question_2 == "power":
        if Question_3 == "loyalty":
            if Question_4 == "bravery":
                house = "Gryffindor"
            elif Question_4 == "cunning":
                house = "Slytherin"
        elif Question_3 == "creativity":
            if Question_4 == "bravery":
                house = "Gryffindor"
            elif Question_4 == "cunning":
                house = "Slytherin"
    elif Question_2 == "friends":
        if Question_3 == "loyalty":
            if Question_4 == "bravery":
                house = "Gryffindor"
            elif Question_4 == "cunning":
                house = "Hufflepuff"
        elif Question_3 == "creativity":
            if Question_4 == "bravery":
                house = "Ravenclaw"
            elif Question_4 == "cunning":
                house = "Hufflepuff"

elif Question_1 == "spells":
    if Question_2 == "power":
        if Question_3 == "loyalty":
            if Question_4 == "bravery":
                house = "Slytherin"
            elif Question_4 == "cunning":
                house = "Slytherin"
        elif Question_3 == "creativity":
            if Question_4 == "bravery":
                house = "Ravenclaw"
            elif Question_4 == "cunning":
                house = "Slytherin"
    elif Question_2 == "friends":
        if Question_3 == "loyalty":
            if Question_4 == "bravery":
                house = "Hufflepuff"
            elif Question_4 == "cunning":
                house = "Hufflepuff"
        elif Question_3 == "creativity":
            if Question_4 == "bravery":
                house = "Ravenclaw"
            elif Question_4 == "cunning":
                house = "Ravenclaw"

if house=='Gryffindor':
    quality = Gryffindor
elif house=='Slytherin':
    quality = Slytherin
elif house=='Hufflepuff':
    quality = Hufflepuff
elif house=='Ravenclaw':
    quality = Ravenclaw


time.sleep(3)
print(f"\n     Sorting Hat : 'It's difficult to say where i should keep you' ")
time.sleep(4)
print(f"\n     Sorting Hat : Ah, I see...{quality}... ")
time.sleep(5)
print(f"\n     Sorting Hat : You have This is clear! \n                  '{house.upper()}!'    ")
if house=='Gryffindor':
     announcement = Gryffindor_SONG.play()
elif house=='Slytherin':
     announcement = Slytherin_SONG.play()
elif house=='Hufflepuff':
     announcement = Hufflepuff_SONG.play()
elif house=='Ravenclaw':
     announcement = Ravenclaw_SONG.play()   
time.sleep(2.5)
print(f"\n{Student_name} walks confidently to the '{house}' table, where they are greeted with applause from their new housemates.\n")
time.sleep(2.5)
print("Professor McGonagall : 'Now the Headmaster Dumbledore will say something'")
time.sleep(2.5)
print("\nHeadmaster Dumbledore :  'Welcome to another year at Hogwarts! Before we begin our feast,\n I have a few announcements to share' ")
starting.play()
time.sleep(8)
if professor == "Professor Severus Snape":
    print("\nHeadmaster Dumbledore : Professor slughorn I am happy to say has agreed to resume his old post as potion master meanwhile the post of defense against the dark arts will takes by Professor Snape\n\n")
    mp3_dir = ".mp3's"
    potion_master = vlc.MediaPlayer(os.path.join(mp3_dir,"Professor's.mp3's", "potion_master.mp3"))
    potion_master.play()
    time.sleep(8.5)
else:  
    print(f"\nHeadmaster Dumbledore : firstly I am pleased to announce that we have a new Defense Against the Dark Arts teacher this year. Please join me in welcoming {professor}! .\n\n")
    first_announcment.play()
    time.sleep(8.2)
    voice = vlc.MediaPlayer(voice_teacher[parv])
    voice.play()
time.sleep(5)
Data = [
    ["Transfiguration" , "Professor Minerva McGonagal"],
    ["Potions" , "Professor Severus Snape"],
    ["Charms" , "Professor Filius Flitwick"],
    ["Herbology" , " Professor Pomona Sprout"],
    ["Defense Against the Dark Arts" ,  professor],
    ["Astronomy" , "Professor Sinistra"],
    ["History of Magic" , "Professor Cuthbert Binns"],
    ["Divinationn" , "Professor Sybill Trelawneyl"],
    ["Care of Magical Creatures" , "Professor Rubeus Hagrid"],
    ["Muggle Studies" , "Charity Burbage"],
    ["Arithmancy" , "Professor Septima Vector"],
    ["Flying" , "Madam Rolanda Hooch"]
    
     ]

if professor == "Professor Severus Snape":
    Data[1][1] = "Professor Horace Slughorn"



Headers = ["Subjects","Teachers"]
print(tabulate(Data,headers=Headers,tablefmt="grid"))
time.sleep(3)
print("\n    Headmaster Dumbledore : These professors, along with the rest of the Hogwarts staff, are here to guide and\nsupport you throughout the year . Please give them your utmost respect and attention.\n")
respect.play()
time.sleep(12)
Motivate = [ "It does not do to dwell on dreams and forget to live.",
             "We are only as strong as we are united, as weak as we are divided."
             ,"You think the dead we loved ever truly leave us? You think that we don’t recall them more clearly\nthan ever in times of great trouble?"
             ,"The truth is a beautiful and terrible thing, and should therefore be treated with great caution."
             ,"Fear of a name increases fear of the thing itself."
             ,"We must all face the choice between what is right and what is easy."
             ,"Happiness can be found, even in the darkest of times, when only remembers to turn on the light." ]

motive = random.randint(0,6)
motivation = Motivate[motive]
time.sleep(4)
print(f"     Headmaster Dumbledore :  {motivation}")
albus_motivation = vlc.MediaPlayer(Albus_speech[motive])

albus_motivation.play()
time.sleep(8.5)

mp3_dir = ".mp3's"
glasstape = vlc.MediaPlayer(os.path.join(mp3_dir,"End","glasstape.mp3"))
glasstape.play()
time.sleep(3.5)

print("\n              Now, let the feast begin! \n\n")
feast.play()
time.sleep(3.9)  # Ensure the audio has time to start


  