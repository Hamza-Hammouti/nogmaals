# name of student: Hamza Hammouti
# number of student: 99069686
# purpose of program: 
# function of program: 
# structure of program: 

coins200 = 0
coins100 = 0
coins50 = 0
coins20 = 0
coins10 = 0
coins5 = 0
coins2 = 0
coins1 = 0

toPay = int(float(input('Amount to pay: '))* 100) #
paid = int(float(input('Paid amount: ')) * 100) #
change = paid - toPay # Berekent of je teveel hebt betaald
if change > 0: # Hij kijkt of je teveel hebt betaald
  coinValue = 200 # Beginwaarde van het geld
  while change > 0 and coinValue > 0: # Blijft doorgaan tot i alles terug kan geven
    nrCoins = change // coinValue # Checkt hoeveel munten je kan geven maximaal
    if nrCoins > 0: # checkt of de rest van het getal van munten nog bestaat
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #
      change -= nrCoinsReturned * coinValue #
# comment on code below:
    if coinValue == 200:
      coinValue = 100
      coins200 = nrCoinsReturned
    elif coinValue == 100:
      coinValue = 50
      coins100 = nrCoinsReturned
    elif coinValue == 50:
      coinValue = 20
      coins50 = nrCoinsReturned
    elif coinValue == 20:
      coinValue = 10
      coins20 = nrCoinsReturned
    elif coinValue == 10:
      coinValue = 5
      coins10 = nrCoinsReturned
    elif coinValue == 5:
      coinValue = 2
      coins5 = nrCoinsReturned
    elif coinValue == 2:
      coinValue = 1
      coins2 = nrCoinsReturned
    else:
      coinValue = 0
      coins1 = nrCoinsReturned
if change > 0: # Checkt of er nog geld is
  print('Change not returned: ', str(change) + ' cents')
  input('press enter to contine')
else:
  print(f"""++++++++++++++++++++++++++++++++++++++++++++++++++++++
|You've returned {coins200} of 200 cent coins.
|You've returned {coins100} of 100 cent coins.
|You've returned {coins50} of 50 cent coins.
|You've returned {coins20} of 20 cent coins.
|You've returned {coins10} of 10 cent coins.
|You've returned {coins5} of 5 cent coins.
|You've returned {coins2} of 2 cent coins.
|You've returned {coins1} of 1 cent coins.
+++++++++++++++++++++++++++++++++++++++++++++++++++++1""")
  input('press enter to contine')