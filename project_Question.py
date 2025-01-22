# Sample inputs to test the function
Question_1 = input("Do you prefer daring adventures or studying new spells? (adventure/spells):    ")
Question_2 = input("Would you rather have power and control or make new friends? (power/friends):  ")
Question_3 = input("Do you value loyalty or creativity more? (loyalty/creativity):  ")
Question_4 = input("Do you prefer bravery or cunning to get what you want? (bravery/cunning):  ")

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

# Output the result
print(f"\nBased on your answers, you belong to {house} House!")
