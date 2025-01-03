import random, sys

HEARTS = chr(9829)  # Character 9829 is '♥'
DIAMONDS = chr(9830)# Character 9829 is '♦'
SPADES = chr(9824)  # Character 9829 is '♠'
CLUBS = chr(9827)   # Character 9829 is '♣'
# A list of chr codes is at https://inventwithpython.com/charactermap
BACKSIDE = 'backside'

def main():
    print('''Blackack, by AL Sweigart al@inventwithpython.com
    
    Rules:
        Try to get as close to 21 without going over.
        Kings, Queens, and Jacks are worth 10 points.
        Aces are worth 1 or 11 points.
        Cards 2 through 10 are worth their face value.
        (H)it to take another card.
        (S)tand to stop taking cards.
        On your first play, you can (D)ouble down to increase your bet but must hit exactly one more time before standing.
        In case of a tie, the bet is returned to the player.
        The dealer stops hitting at 17.''')

    money = 5000
    while True:
        if money <= 0:
            print("You're broke!")
            print("Good thing you weren't playing with real money.")
            print('Thanks for playing!')
            sys.exit()

        print(f'Money: {money}')
        bet = getBet(money)

        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        print('Bet:', bet)
        while True:
            displayHands(playerHand, dealerHand, False)
            print()

            # Check if the player has bust
            if getHandValue(playerHand) >= 21:
                break

            # Get the player's move, either H, S, D
            move = getMove(playerHand, money - bet)

            # Handle the player actions
            if move == 'D':
                # Player is doubling down, thay can increase their bet
                additionalBet = getBet(min(bet, money - bet))
                bet += additionalBet
                print(f'Bet increased to {bet}')
                print('Bet:', bet)

            if move in ('H', 'D'):
                # Hit/doubling down takes another card.
                newCard = deck.pop()
                rank, suit = newCard
                print(f'You drew a {rank} of {suit}.')
                playerHand.append(newCard)

                if getHandValue(playerHand) > 21:
                    # The player has busted
                    continue

            if move in ('S', 'D'):
                # Stand/doubling down stops the player's turn'
                break

        # Handle the dealer's actions
        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                # The dealer hits
                print('Dealer hits...')
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)

                if getHandValue(dealerHand) > 21:
                    break
                input('Press Enter to continue...')
                print('\n\n')

        # Show the final hands
        displayHands(playerHand, dealerHand, True)

        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)
        # Handle whether the player won, lost, or tied
        if dealerValue > 21:
            print(f'Dealer busts! You win ${bet}')
            money += bet
        elif (playerValue > 21) or (playerValue < dealerValue):
            print('You lost!')
            money -= bet
        elif playerValue > dealerValue:
            print(f'You won ${bet}!')
            money += bet
        else:
            print("It's a tie, the bet is returned to you.")

        input('Press Enter to continue...')
        print('\n\n')



def getBet(maxBet):
    """Ask the player how much they want to bet for this round."""
    while True:
        print(f'How much do you bet? (1-{maxBet}. or QUIT)')
        bet = input('> ').upper().strip()

        if bet == 'QUIT':
            sys.exit()

        if not bet.isdecimal():
            continue    # If the player didn't enter a number, ask again.
        else:
            bet = int(bet)

        if 1 <= bet <= maxBet:
            return bet


def getDeck():
    """Return a list of (rank, suit) tuples for all 52 cards."""
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck


def getHandValue(cards):
    """Returns the value of the cards. Face cards are worth 10, aces are worth 11 or 1 (this function picks the most
    suitable ace value)."""
    value = 0
    numberOfAces = 0

    # Add the vlaue for the non-ace cards
    for card in cards:
        rank = card[0]
        if rank == 'A':
            numberOfAces += 1
        elif rank in ('J', 'Q', 'K'):
            value += 10
        else:
            value += int(rank)

    value += numberOfAces

    for i in range(numberOfAces):
        if value + 10 <= 21:
            value += 10

    return value


def displayHands(playerHand, dealerHand, showDealerHand):
    """Show the player's and dealer's cards. Hide the dealer's first card if showDealerHand is False."""
    print()
    if showDealerHand:
        print('DEALER:', getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print('DEALER: ???')
        displayCards([BACKSIDE] + dealerHand[1:])

    print('PLAYER:', getHandValue(playerHand))
    displayCards(playerHand)

def displayCards(cards):
    """Display all the cards in the cards list."""
    rows = ['', '', '', '', ''] # The text to display on each row.

    for i, card in enumerate(cards):
        rows[0] += ' ___  '
        if card == BACKSIDE:
            # Print a card's back
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            # Print a card's back
            rank, suit = card
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(rank.rjust(2, "_"))

    # Print each row on the screen
    for row in rows:
        print(row)


def getMove(playerHand, money):
    """Asks the player for their move, and return 'H for hit, 'S' for stand, and 'D' for double down."""
    while True:
        moves = ['(H)it', '(S)tand']

        # The player can double down on their first move, which we can
        # tell because they'll have exactly tow cards'
        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble down')

        movePrompt = ', '.join(moves) + '> '
        move = input(movePrompt).upper()

        if move in ('H', 'S'):
            return move
        if move == 'D' and '(D)ouble down' in moves:
            return move

if __name__ == '__main__':
    main()