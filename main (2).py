#Carina D'Souza & Ember Prole
#8 Dec 2021 
#A6cheat.py
#Creating the card game "cheat" on a text-based interface

import random
import time

#EMBER
#mainMenu()
#prints a welcome message to the user and explains how to play.
#@param: none
#@return: none
def mainMenu():
      #printing ze instructions
      print("Welcome to our wonderful edition of Cheat!"
            )  #just general politeness
      print(
          "Just in case you don't know how the game works, here's a brief overview:"
      )
      print(
          "On your turn, players can play between one and four cards. The player must state what the cards are, but does not have to tell the truth."
      )
      print(
          "Each turn the number that you are supposed to play increases by one. For example, the first person plays ace, then the next person plays two, then three, etc."
      )
      print(
          "The player must claim the cards are all of the same value. For example, a player could say they have '3 Kings', and place any 3 cards in the centre."
      )
      print(
          "The other players can call 'cheat' if they think the player is lying about the value of the cards."
      )
      print(
          "If 'CHEAT' is called, the played cards will be shown to everyone else."
      )
      print(
          "If the challenger who called cheat is correct and the player was lying, the cheater must pick up all the cards in the discard pile. The challenger takes the next turn. If the challenger is wrong, that player picks up the discard pile. The player to the left of the player who played the cards takes the next turn."
      )
      print("The winner is the first person to get rid of all their cards.")
      print("So let's get started!")


#CARINA
#dealCards()
#deals out 52 cards into 4 even decks
#@param: none
#@return: playerDeck:str[], comp1Deck:str[], comp2Deck:str[], comp3Deck:str[]
def dealCards():  
    print("")
    #this is a list of all possible cards (52)
    possibleCards = [
        "A", "A", "A", "A", "2", "2", "2", "2", "3", "3", "3", "3", "4", "4",
        "4", "4", "5", "5", "5", "5", "6", "6", "6", "6", "7", "7", "7", "7",
        "8", "8", "8", "8", "9", "9", "9", "9", "10", "10", "10", "10", "J",
        "J", "J", "J", "Q", "Q", "Q", "Q", "K", "K", "K", "K"
    ]
    #shuffles the list and then divides them into decks using indexes
    random.shuffle(possibleCards)
    playerDeck = possibleCards[0:13]
    comp1Deck = possibleCards[13:26]
    comp2Deck = possibleCards[26:39]
    comp3Deck = possibleCards[39:52]

    return playerDeck, comp1Deck, comp2Deck, comp3Deck


#CARINA
#sortCards()
#sorts the cards (which are taken in as a param) in order of value
#@param: playerCards:str[]
#@return: sortedCards:str[]
def sortCards(playerCards):  
    intList = [] #this converts the values of the non-integer cards (A, J, Q, K) and assigns them numerical values to get sorted - otherwise, the sorted() function wouldn't sort them properly 
    for card in playerCards:
        if card == "J":
            val = 11
        elif card == "Q":
            val = 12
        elif card == "K":
            val = 13
        elif card == "A":
            val = 1
        elif card == "10":
            val = 10
        else:
          val = int(card)
        intList.append(val) #appends these cards with only their values to a list

    sortedInts = sorted(intList) #sorts the interger list of cards ands stores in a list called sortedInts 
    sortedCards = []

    for i in sortedInts: #appends all of the cards to a new list. for appending the non-integer cards, it first turns them back into their corresponding cards (eg. 1 --> "A") 
        if i > 1 and i < 10:
            sortedCards.append(str(i))
        if i == 10:
          sortedCards.append("10")
        if i == 11:
            sortedCards.append("J")
        if i == 12:
            sortedCards.append("Q")
        if i == 13:
            sortedCards.append("K")
        if i == 1:
            sortedCards.append("A")
    return sortedCards


#EMBER
#getRange()
#helps with displaying the cards by getting a range of where each type of card is located in a list, once sorted.
#@param: hand:str[], lookingFor:str
#@return: hand:str[] or []
def getRange(hand, lookingFor):
    if lookingFor in hand:
          num = hand.count(lookingFor)
          start_index = hand.index(lookingFor)
          end_index = start_index + num
          return hand[start_index:end_index]
    else:
          return []


#EMBER
#showCards()
#gets sorted cards as a parameter and shows them to the user.
#@param: sortedCards:str[]
#@return: none
def showCards(sortedCards):  
      print("\nHere are your cards:\n")
      print("A: {}".format(len(getRange(sortedCards, "A"))))
      print("2: {}".format(len(getRange(sortedCards, "2"))))
      print("3: {}".format(len(getRange(sortedCards, "3"))))
      print("4: {}".format(len(getRange(sortedCards, "4"))))
      print("5: {}".format(len(getRange(sortedCards, "5"))))
      print("6: {}".format(len(getRange(sortedCards, "6"))))
      print("7: {}".format(len(getRange(sortedCards, "7"))))
      print("8: {}".format(len(getRange(sortedCards, "8"))))
      print("9: {}".format(len(getRange(sortedCards, "9"))))
      print("10: {}".format(len(getRange(sortedCards, "10"))))
      print("J: {}".format(len(getRange(sortedCards, "J"))))
      print("Q: {}".format(len(getRange(sortedCards, "Q"))))
      print("K: {}".format(len(getRange(sortedCards, "K"))))

#EMBER
#getPlayerMove()
#Gets input for cards to be played, stores if the play is a cheat, then returns an updated hand with the play and cheat status.
#@param: sortedCards:str[], supposedToPlay:str
#@return: play:str[], sortedCards:str[], cheat:boolean
def getPlayerMove(sortedCards, supposedToPlay):
      play = []
      showCards(sortedCards)
      turnIsGoing = True
      cheatNum = 0
      while turnIsGoing:
          playedCard = input("What card would you like to play? ")
          playedCard = playedCard.upper()
          if playedCard in sortedCards:
              if playedCard != supposedToPlay:  #checking for cheat
                  print("You have cheated.")
                  cheatNum = cheatNum + 1
              try:
                  play.append(playedCard)
                  sortedCards.remove(playedCard)
              except:
                  print("Invalid input. Try again!")
              askShowCards = True
              while askShowCards:
                show = input("Do you want to check your cards again? y for yes, n for no: ")
                show = show.lower()
                if show == "y":
                    showCards(sortedCards)
                    askShowCards = False
                elif show == "n":
                    askShowCards = False
                else:
                    print("Invalid Input!")

              
              turnOverLoop = True
              while turnOverLoop:
                turnOver = input("Are you finished with your turn, or is there another card you want to play? y for yes, n for no")
                turnOver = turnOver.lower()
                if turnOver == "n":
                    print("Your turn is over.")
                    turnIsGoing = False 
                    turnOverLoop = False
                elif turnOver == "y":
                    print("")
                    turnIsGoing = True
                    turnOverLoop = False
                else:
                    print("Invalid input! Try again!")
          else:
              print("You don't have that card!")
          if cheatNum != 0:
            cheat = True
          else:
            cheat = False
      return play, sortedCards, cheat


#CARINA
#isPlayerCheating()
#given certain scenarios (based on the current play + user's deck) gives a probability for whether or not to call cheat
#@param: playerCards:str, numCards:int, discardPile:str[], callerCards:str[]
#@return: True:boolean or False:boolean
def isPlayerCheating(playedCards, numCards, discardPile, callersCards):
  #detects whether the computer should call cheat
    chanceCheated = 1 #creating chanceCheated - gets modified later in the function
    if playedCards in callersCards: #if the computer (caller) has one of the same cards as the player is supposed to have played (eg. if player is supposed to play an "A", this detects if the caller has an "A")
        howManyInCompDeck = callersCards.count(playedCards) #counts how many of the given card the computer has 
        howManyPlayed = numCards
        if howManyInCompDeck + howManyPlayed > 4: #if the number of cards of the supposed type the caller played + the number in the user deck is greater than 4, the player must have cheated
            chanceCheated = 0 
        elif howManyInCompDeck + howManyPlayed == 4:
            chanceCheated = random.randint(0, 3) #one in four chance of getting called if the sum of the number of the given card the player has and the computer has is equal to 4
        else:
          chanceCheated = random.randint(0, 20) #if the caller has the card in the deck, but doesn't meet above conditions: 1 in  21 chance
    elif numCards > 4: #if the caller doesn't have the said card, but amount played still exceeds 4, or is greater than 4
      chanceCheated = 0
    elif numCards == 4:
      chanceCheated = random.randint(0,1)
    else:
      chanceCheated = random.randint(0,100) #otherwise, 1 in 101 chance of calling 
    
    if chanceCheated == 0:
      return True
    else: 
      return False

#EMBER
#computerMove()
#gets the computer to create a play by looking at the cards they have- if they have the card they're supposed to play, they play it. Otherwise it cheats using the card that is has most of.
#@param: computerCards:str[], mustPlay:str, compNum:str
#@return: play:str[], computerCards:str[], cheatCalled:boolean
def computerMove(computerCards, mustPlay, compNum):  #EMBER
      cards = computerCards
      mustPlay = str(mustPlay)
      cards = sortCards(cards)
      #print(cards)
      play = []
      print("The computer is thinking...")
      time.sleep(3)

      if mustPlay in cards:
        cheat = False
        if cards.count(mustPlay) == 1:  #if it has one or more of the card
              play.append(
                  str(mustPlay))  #add it to a list of the cards it's playing
              cards.remove(mustPlay)  #taking it out of the computer's hand
              
        
        while True:
            if cards.count(mustPlay) >= 1:
              try:
                play.append(str(mustPlay))
                cards.remove(str(mustPlay))
              except:
                break
            else:
              break

      else: 
          #counting how many different cards are in the computer's hand
          cheat = True
          differentCards = []
          for card in cards:
              if card in differentCards:
                  continue
              else:
                  differentCards.append(card)
          differentCards = sortCards(differentCards)

          #calculating which card it has most of
          numMost = 1
          for i in differentCards:
              if cards.count(card) >= numMost:  #checks if it's larger or the same. better to cheat with higher number
                  most = i
                  numMost = cards.count(most)
          if numMost > 1:
            card_range = random.randint(1, numMost)
          else:
            card_range = 1
          for i in range(card_range):
              play.append(str(most))
              cards.remove(str(most))


      cheatNum = 0
      for i in play:
          if i != mustPlay:
              cheatNum = cheatNum + 1
      if cheatNum != 0:
        cheated = True
      else:
        cheated = False

      print("The computer has played {} {}'s, and has {} cards left.".format(len(play), mustPlay, len(cards)))
      #print("The computer actually played {}".format(play))
      #loop for getting player cheat calls on computer
      cheatCall = True
      while cheatCall:
        playerSays_cheat = input("Is computer {} cheating? y for oui, n for non ".format(compNum))
        playerSays_cheat = playerSays_cheat.lower()
        if playerSays_cheat == "y":
            if cheated:
                print("You are right. Computer {} played {}, and cheated.".format(compNum, play))
                cheatCalled = "cheat correctly called"
                cheatCall = False
            else:
                print("You are wrong! Computer {} played {}, and did not cheat.".format(compNum, play))
                cheatCalled = "cheat incorrectly called"
                playerSays_cheat = False
                cheatCall = False
        elif playerSays_cheat == "n":
            cheatCalled = "not called"
            cheatCall = False
        else:
            print("Invalid input! Try again!")
            

        
      return play, cards, cheatCalled, cheat


#CARINA
#isGameOver()
#detects if the game is over (False, returned) or who won (returns string)
#@param: deck1:str[], deck2:str[], deck3:str[], deck4:str[]
#@return: player:str or comp 1:str or comp 2:str or comp 3:str depending on who wins, else returns False:boolean
def isGameOver(deck1, deck2, deck3, deck4):
  #checks the length of each deck (entered as a param) and returns either the winner, or returns False if the game is not over
    if len(deck1) == 0:  
        return "player"
    elif len(deck2) == 0:
        return "comp 1"
    elif len(deck3) == 0:
        return "comp 2"
    elif len(deck4) == 0:
        return "comp 3"
    else:
      return False

#CARINA
#printEndMsg()
#prints end message and determines the winner based on the isGameOver() function
#@param: none
#@return:none
def printEndMsg():
  endTime = time.monotonic()
  timeSpent = endTime - startTime
  winner = isGameOver(playerCards, comp1Cards, comp2Cards, comp3Cards)
  if winner == "player":
      print("Player wins!")
  elif winner == "comp 1":
      print("Computer 1 wins!")
  elif winner == "comp 2":
      print("Computer 2 wins!")
  elif winner == "comp 3":
      print("Computer 3 wins!")
  print("In total, your game lasted {} seconds! We hope you enjoyed it :)".format(timeSpent))

playing = True
while playing:
  startTime = time.monotonic()
  discardPile = []
  decks = dealCards()
  playerCards = decks[0]
  comp1Cards = decks[1]
  comp2Cards = decks[2]
  comp3Cards = decks[3]
  mainMenu()
  playerCards = sortCards(playerCards)
  comp1Cards = sortCards(comp1Cards)
  comp2Cards = sortCards(comp2Cards)
  comp3Cards = sortCards(comp3Cards)

  cardNum = 1
  playerNum = 1


  cardToPlay = 1


  while isGameOver(playerCards, comp1Cards, comp2Cards, comp3Cards) == False:
    turnGoing = True #loop for if the turn is ongoing

    #Setting what card needs to be played, as a string. This ensures that when the computer cycles through the cards as numbers, the string versions of the cards can still be read and played.

    lie = str(cardToPlay)
    if lie == "1":
        lie = "A"
    if lie == "13":
        lie = "K"
    if lie == "12":
        lie = "Q"
    if lie == "11":
        lie = "J"
    print("")
    print("Player {}, play a {}!".format(playerNum, lie))
    shouldPlay = []

    #("Discard Pile: " + str(discardPile))



    # Player turn.

    if playerNum == 1:
      move = getPlayerMove(playerCards, lie)
      playerCards = move[1]
      # print("Move[1]:", move[1])
      # print("Player cards:", playerCards)
      play = move[0]
      discardPile.extend(play)
      cheat = move[2]
      
      #Making sure only one person calls cheat
      called = False
      # Get cheat calls, if applicable

      comp1Called = isPlayerCheating(lie, len(play), discardPile, comp1Cards)
      comp2Called = isPlayerCheating(lie, len(play), discardPile, comp2Cards)
      comp3Called = isPlayerCheating(lie, len(play), discardPile, comp3Cards)

      

      if comp1Called and called == False:
        if cheat:
          print("CHEAT! Computer #1, you were correct. Player, take this pile of {} cards!".format(len(discardPile)))
          playerCards.extend(discardPile)
          playerCards = sortCards(playerCards)
          discardPile = []
          called = True
        else:
          print("CHEAT! Computer #1, you were incorrect. Take this pile of {} cards!".format(len(discardPile)))
          comp1Cards.extend(discardPile)
          comp1Cards = sortCards(comp1Cards)
          discardPile = []
          called = True

      if comp2Called and called == False:
        if cheat:
          print("CHEAT! Computer #2, you were correct. Player, take this pile of {} cards!".format(len(discardPile)))
          playerCards.extend(discardPile)
          playerCards = sortCards(playerCards)
          discardPile = []
          called = True
        else:
          print("CHEAT! Computer #2, you were incorrect. Take this pile of {} cards!".format(len(discardPile)))
          comp2Cards.extend(discardPile)
          comp2Cards = sortCards(comp2Cards)
          discardPile = []
          called = True
      
      if comp3Called and called == False:
        if cheat:
          print("CHEAT! Computer #3, you were correct. Player, take this pile of {} cards!".format(len(discardPile)))
          playerCards.extend(discardPile)
          playerCards = sortCards(playerCards)
          discardPile = []
          called = True
        else:
          print("CHEAT! Computer #3, you were incorrect. Take this pile of {} cards!".format(len(discardPile)))
          comp3Cards.extend(discardPile)
          comp3Cards = sortCards(comp3Cards)
          discardPile = []
          called = True

    # Computer 1 turn
    elif playerNum == 2:
      move = computerMove(comp1Cards, lie, '1')
      play = move[0]
      # print(comp1Cards)
      comp1Cards = move[1]
      # print("Move[1]:", move[1])
      # print("Player cards:", comp1Cards)
      discardPile.extend(play)
      cheatCall = move[2]
      cheat = move[3]

      # Checking if it was a cheat, and initiating the moving of cards
      called = False

      if cheatCall == "cheat correctly called":
        print("Computer 1 picks up {} cards.".format(len(discardPile)))
        comp1Cards.extend(discardPile)
        comp1Cards = sortCards(comp1Cards)
        discardPile = []
        called = True
      elif cheatCall == "cheat incorrectly called":
        print("Player picks up {} cards.".format(len(discardPile)))
        playerCards.extend(discardPile)
        playerCards = sortCards(playerCards)
        discardPile = []
        called = True
      
      # Get cheat calls, if applicable
      comp2Called = isPlayerCheating(lie, len(play), discardPile, comp2Cards)
      comp3Called = isPlayerCheating(lie, len(play), discardPile, comp3Cards)

    

      if comp2Called and called == False:
        if cheat:
          print("CHEAT! Computer #2, you were correct. Player, take this pile of {} cards!".format(len(discardPile)))
          comp1Cards.extend(discardPile)
          comp1Cards = sortCards(comp1Cards)
          discardPile = []
          called = True
        else:
          print("CHEAT! Computer #2, you were incorrect. Take this pile of {} cards!".format(len(discardPile)))
          comp2Cards.extend(discardPile)
          comp2Cards = sortCards(comp2Cards)
          discardPile = []
          called = True
      
      if comp3Called and called == False:
        if cheat:
          print("CHEAT! Computer #3, you were correct. Player, take this pile of {} cards!".format(len(discardPile)))
          comp1Cards.extend(discardPile)
          comp1Cards = sortCards(comp1Cards)
          discardPile = []
          called = True
        else:
          print("CHEAT! Computer #3, you were incorrect. Take this pile of {} cards!".format(len(discardPile)))
          comp3Cards.extend(discardPile)
          comp3Cards = sortCards(comp3Cards)
          discardPile = []
          called = True


    # Computer 2 turn
    elif playerNum == 3:
      move = computerMove(comp2Cards, lie, '2')
      play = move[0]
      discardPile.extend(play)
      comp2Cards = move[1]
      # print("Move[1]:", move[1])
      # print("Player cards:", comp2Cards)
      cheatCalled = move[2]
      cheat = move[3]

      # Checking if it was a cheat, and initiating the moving of cards
      called = False

      if cheatCalled == "cheat correctly called":
        print("Computer 2 picks up {} cards.".format(len(discardPile)))
        comp2Cards.extend(discardPile)
        comp2Cards = sortCards(comp2Cards)
        discardPile = []
        called = True
      elif cheatCalled == "cheat incorrectly called":
        print("Player picks up {} cards.".format(len(discardPile)))
        playerCards.extend(discardPile)
        playerCards = sortCards(playerCards)
        discardPile = []
        called = True
      
      # Get cheat calls, if applicable
      comp1Called = isPlayerCheating(lie, len(play), discardPile, comp1Cards)
      comp3Called = isPlayerCheating(lie, len(play), discardPile, comp3Cards)

      

      if comp1Called and called == False:
        if cheat:
          print("CHEAT! Computer #1, you were correct. Player, take this pile of {} cards!".format(len(discardPile)))
          comp2Cards.extend(discardPile)
          comp2Cards = sortCards(comp2Cards)
          discardPile = []
          called = True
        else:
          print("CHEAT! Computer #1, you were incorrect. Take this pile of {} cards!".format(len(discardPile)))
          comp1Cards.extend(discardPile)
          comp1Cards = sortCards(comp1Cards)
          discardPile = []
          called = True
      
      if comp3Called and called == False:
        if cheat:
          print("CHEAT! Computer #3, you were correct. Player, take this pile of {} cards!".format(len(discardPile)))
          comp2Cards.extend(discardPile)
          comp2Cards = sortCards(comp2Cards)
          discardPile = []
          called = True
        else:
          print("CHEAT! Computer #3, you were incorrect. Take this pile of {} cards!".format(len(discardPile)))
          comp3Cards.extend(discardPile)
          comp3Cards = sortCards(comp3Cards)
          discardPile = []
          called = True

    elif playerNum == 4:
        move = computerMove(comp3Cards, lie, '3')
        play = move[0]
        # print(comp3Cards)
        discardPile.extend(play)
        comp3Cards = move[1]
        # print("Player cards:", comp3Cards)
        cheatCalled = move[2]
        cheat = move[3]
        # Checking if it was a cheat, and initiating the moving of cards
        called = False

        if cheatCalled == "cheat correctly called":
          print("Computer 3 picks up {} cards.".format(len(discardPile)))
          comp3Cards.extend(discardPile)
          comp3Cards = sortCards(comp3Cards)
          discardPile = []
          called = True
        elif cheatCalled == "cheat incorrectly called":
          print("Player picks up {} cards.".format(len(discardPile)))
          playerCards.extend(discardPile)
          playerCards = sortCards(playerCards)
          discardPile = []
          called = True
        
        # Get cheat calls, if applicable
        comp1Called = isPlayerCheating(lie, len(play), discardPile, comp1Cards)
        comp2Called = isPlayerCheating(lie, len(play), discardPile, comp2Cards)



        if comp1Called and called == False:
          if cheat:
            print("CHEAT! Computer #1, you were correct. Player, take this pile of {} cards!".format(len(discardPile)))
            comp3Cards.extend(discardPile)
            comp3Cards = sortCards(comp3Cards)
            discardPile = []
            called = True
          else:
            print("CHEAT! Computer #1, you were incorrect. Take this pile of {} cards!".format(len(discardPile)))
            comp1Cards.extend(discardPile)
            comp1Cards = sortCards(comp1Cards)
            discardPile = []
            called = True
        
        if comp2Called and called == False:
          if cheat:
            print("CHEAT! Computer #2, you were correct. Player, take this pile of {} cards!".format(len(discardPile)))
            comp3Cards.extend(discardPile)
            comp3Cards = sortCards(comp3Cards)
            discardPile = []
            called = True
          else:
            print("CHEAT! Computer #2, you were incorrect. Take this pile of {} cards!".format(len(discardPile)))
            comp2Cards.extend(discardPile)
            comp2Cards = sortCards(comp2Cards)
            discardPile = []
            called = True


    #Moving on to the next turn. Sets the next player to the next player, and changes the card to the next one in order.
    
    playerNum = playerNum + 1
    if playerNum == 5:
      playerNum = 1
      
    cardToPlay = cardToPlay + 1
    if cardToPlay == 14:
      cardToPlay = 1

  else:
    printEndMsg()

  #ask to play again
  againLoop = True
  while againLoop:
    again = input("Do you want to play again? y for yes, n for no ")
    again = again.lower()
    if again == "y":
      playing = True
      againLoop = False
    elif again == "n":
      playing, againLoop = False
    else:
      print("Invalid input! Try again")





