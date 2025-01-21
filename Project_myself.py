import random
import time
from tabulate import tabulate
import vlc
feast=vlc.MediaPlayer("feast.mp3")
respect =vlc.MediaPlayer("respect.mp3")

hogwards= vlc.MediaPlayer("music.mp3")
hogwards.play()
Gryffindor_SONG =vlc.MediaPlayer("Gryffindor.mp3")
Slytherin_SONG =vlc.MediaPlayer("Slytherin.mp3")
Hufflepuff_SONG =vlc.MediaPlayer("Hufflepuff.mp3")
Ravenclaw_SONG =vlc.MediaPlayer("Ravenclaw.mp3")
starting = vlc.MediaPlayer("starting.mp3")
first_announcment = vlc.MediaPlayer("first_anncounment.mp3")

voice_teacher = ["qurriell.mp3","lockhart.mp3","lupin.mp3","moddy.mp3","umbridge.mp3","snape.mp3"]
Albus_speech = ["motive1.mp3","motive2.mp3","motive3.mp3","motive4.mp3","motive5.mp3","motive6.mp3","motive7.mp3"]
 
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
    print("Headmaster Dumbledore : Professor slughorn I am happy to say has agreed to resume his old post as potion master meanwhile the post of defense against the dark arts will takes by Professor Snape")
    potion_master = vlc.MediaPlayer("potion_master.mp3")
    potion_master.play()
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
glasstape = vlc.MediaPlayer("glasstape.mp3")
glasstape.play()
time.sleep(3.5)
print("\n              Now, let the feast begin! \n\n")
feast.play()
time.sleep(3.9)  # Ensure the audio has time to start


  