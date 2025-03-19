import cards
import federal_law_statement
import time
import pyfiglet
import generate_title



def play():



    num_decks = int(input("Enter the number of decks you prefer:\n"))
    rounds = int(input("Enter the number of rounds you want to play:\n"))
    options = ['hit', 'stand']
    deck = cards.Cards(num_decks)
    print(f"The deck is now {deck.cards}, \nit has {len(deck.cards)} cards")
    deck.shuffle()
    cur_chips = int(input(f"How many chips do you want?\n"))
    min_bet = int(input(f"Enter the minimum bet you want\n"))


    def calculate(cards):
        value_map = {
            'A': 11,
            'J': 10,
            'Q': 10,
            'K': 10
        }
        ace_cnt = 0
        total = 0
        for card in cards:
            value = card.value
            if value in value_map.keys():
                total += value_map[value]
                if value == 'A':
                    ace_cnt += 1
            else:
                total += int(value)

        # 动态调整A的值，保证尽量不bust
        while total > 21 and ace_cnt > 0:
            ace_cnt -= 1
            total -= 10
        return total

    def hit(cur_cards):
        nonlocal cur_chips
        new_card = deck.deal_card()
        cur_cards.append(new_card)
        cur_sum = calculate(cur_cards)

        time.sleep(1)
        print("\n===================================")
        time.sleep(1)
        print(f"You drew: {new_card}")
        time.sleep(1)
        print(f"Your Hand: [{', '.join(map(str, cur_cards))}] (Total = {cur_sum})")
        time.sleep(1)
        print("===================================")

        if cur_sum < 21:
            print("You can continue.")
            return 'continue'
        elif cur_sum == 21:
            cur_chips += min_bet
            print(f"\nBlackjack! Bravo! You win! Your current chips are ${cur_chips}")
            return 'win'
        else:
            cur_chips -= min_bet
            print(f"\nYou bust! The dealer wins. Your current chips are ${cur_chips}")
            if not check_chips():
                return
            return 'lose'

    def stand(dealer_hands, player_sums):
        nonlocal cur_chips
        print("\nYou chose to stand. The dealer will now play.\n")
        dealer_sums = calculate(dealer_hands)
        time.sleep(1)
        print("===================================")
        time.sleep(1)
        print(f"Dealer's Hidden Card Revealed: {dealer_hands[1]}")
        time.sleep(1)
        print(f"Dealer's Hand: [{', '.join(map(str, dealer_hands))}] (Total = {dealer_sums})")
        time.sleep(1)
        print("===================================")

        while dealer_sums < 17:
            new_card = deck.deal_card()
            dealer_hands.append(new_card)
            dealer_sums = calculate(dealer_hands)

            time.sleep(1)
            print(f"\nDealer drew: {new_card}")
            time.sleep(1)
            print(f"Dealer's Hand: [{', '.join(map(str, dealer_hands))}] (Total = {dealer_sums})")
            time.sleep(1)

        # 胜负判断
        print("\n-----------------------------------")
        if dealer_sums > 21:
            cur_chips += min_bet
            print(f"Dealer busts! You win! Your current chips are ${cur_chips}")
            return 'win'
        elif dealer_sums == 21:
            cur_chips -= min_bet
            print(f"Dealer has a Blackjack! Your current chips are ${cur_chips}")
            if not check_chips():
                return
            return 'lose'
        elif dealer_sums > player_sums:
            cur_chips -= min_bet
            print(f"Dealer wins with {dealer_sums} vs your {player_sums}. Your current chips are ${cur_chips}")
            if not check_chips():
                return
            return 'lose'
        elif dealer_sums < player_sums:
            cur_chips += min_bet
            print(f"You win with {player_sums} vs Dealer's {dealer_sums}. Your current chips are ${cur_chips}")
            return 'win'
        else:
            print(f"It's a PUSH! Both have {player_sums}. Your current chips are ${cur_chips}")
            return 'push'

    def check_chips(): # return true if can continue, otherwise false
        nonlocal cur_chips
        if cur_chips <= 0:
            print("You have lost all your chips, please quit.")
            return False
        return True
    for i in range(rounds):
        print(f"\n————Round{i + 1}——————")
        bet_input = int(input(f"Enter your bet for this round, your bet must be greater than ${min_bet}:\n "))
        bet = bet_input if bet_input >= min_bet else min_bet
        deck.reset()
        deck.shuffle()

        dealer_card1 = deck.deal_card()
        player_card1 = deck.deal_card()
        dealer_card2 = deck.deal_card()
        player_card2 = deck.deal_card()

        dealer_cards = [dealer_card1, dealer_card2]
        dealer_cards_concealed = [dealer_card1, '*']
        player_cards = [player_card1, player_card2]


        dealer_sum, player_sum  = calculate(dealer_cards), calculate(player_cards)

        time.sleep(1)
        print("\n===================================")
        time.sleep(1)
        print(f"The Dealer's Hand: [{', '.join(map(str, dealer_cards_concealed))}]")
        time.sleep(1)
        print(f"Your Hand: [{', '.join(map(str, player_cards))}] (Total = {player_sum})")
        time.sleep(1)
        print("===================================")
        time.sleep(1)

        while True:
            if dealer_sum == 21:
                time.sleep(1)
                cur_chips -= min_bet
                print(f"\nDealer has a Blackjack with {dealer_cards}! Your current chips are ${cur_chips}")
                if not check_chips():
                    return
                break

            option = input("\nPlease choose 'Hit' or 'Stand': ").strip().lower()

            if option not in options:
                time.sleep(1)
                print(f"Invalid option '{option}'. Please select either '{options[0]}' or '{options[1]}'.")
                continue

            # 玩家选择 HIT
            if option == "hit":
                result = hit(player_cards)
                player_sum = calculate(player_cards)
                if result in ['lose', 'win']:
                    break

            # 玩家选择 STAND
            else:
                result = stand(dealer_cards, player_sum)
                if result in ['lose', 'win','push']:
                    break


federal_law_statement.verification()
play()

