antwoord = ""
aantalGeraden = 1

while antwoord != "quit":
    antwoord = input("Wat is het antwoord?: ")
    print("Dat is niet het goede antwoord")
    print("Je hebt het antwoord " + str(aantalGeraden) + " keer geraden.")
    aantalGeraden = aantalGeraden + 1

    if antwoord == "quit":
        print("----------------------------")
        print("Je hebt het antwoord geraden.")
        quit()