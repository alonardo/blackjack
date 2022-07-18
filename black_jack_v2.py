import random
import os
from colorama import Fore, Style
from pyfiglet import figlet_format

class Blackjack():
    def __init__(self):
        self.deck = ['2h','3h','4h','5h','6h','7h','8h','9h','10h','11h','12h','13h','14h',
        '2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d', '10d', '11d', '12d', '13d', '14d',
        '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', '10s', '11s', '12s', '13s', '14s',
        '2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', '10c', '11c', '12c', '13c', '14c',]*3
        self.dealer_cards = []
        self.player_cards = []
        self.dealer_count = 0
        self.player_count = 0
        self.temp_count = 0
        

    def deal_cards_to_dealer_start(self):
        random.shuffle(self.deck)
        for x in range(2):
            deal = self.deck.pop()
            
            if len(deal) == 2:
                x = int(deal[0])
                self.dealer_count += x 

            elif len(deal) == 3:
                x = int(deal[:2])
                if x > 10 and x != 14:
                    self.dealer_count += 10
                elif x == 14 and self.dealer_count >= 11:
                    self.dealer_count += 1
                elif x == 14 and self.dealer_count < 11:
                    self.dealer_count += 11
                else:
                    self.dealer_count += x    

            if x == 11:
                deal = 'J' + deal[-1]
            if x == 12:
                deal = 'Q' + deal[-1]
            if x == 13:
                deal = 'K' + deal[-1]
            if x == 14:
                deal = 'A' + deal[-1]
            self.dealer_cards.append(deal)
            
    def hit_me_start(self):
        random.shuffle(self.deck)
    
        for x in range(2):
            deal = self.deck.pop()
            
            if len(deal) == 2:
                x = int(deal[0])
                self.player_count += x 

            elif len(deal) == 3:
                x = int(deal[:2])
                if x > 10 and x != 14:
                    self.player_count += 10
                elif x == 14 and self.player_count >= 11:
                    self.player_count += 1
                elif x == 14 and self.player_count < 11:
                    self.player_count += 11
                else:
                    self.player_count += x

            if x == 11:
                deal = 'J' + deal[-1]
            if x == 12:
                deal = 'Q' + deal[-1]
            if x == 13:
                deal = 'K' + deal[-1]
            if x == 14:
                deal = 'A' + deal[-1]
            self.player_cards.append(deal)

        self.show_cards_hide_dealer_card()

    def show_final_results(self):            
        print('**************************************')
        print(Fore.RED, Style.BRIGHT, 'Dealer Cards: ', self.dealer_cards)
        print('Dealer Count: ', self.dealer_count, Style.RESET_ALL)     
        print('**************************************')  
        print(Fore.BLUE, Style.BRIGHT, 'Player Cards: ', self.player_cards)
        print('Player Count: ', self.player_count, Style.RESET_ALL)
        print('**************************************')  

    def show_cards_hide_dealer_card(self):
        print('**************************************')
        print(Fore.RED, Style.BRIGHT, 'Dealer Cards: ', self.dealer_cards[0], Style.RESET_ALL)
        print('')       
        print('**************************************')  
        print(Fore.BLUE, Style.BRIGHT,'Player Cards: ', self.player_cards)
        print('Player Count: ', self.player_count, Style.RESET_ALL)
        print('**************************************')

    def another_round(self):
        prompt = input('Another round? (y/n/):\n')
        if prompt == 'y':
            self.dealer_cards.clear()
            self.player_cards.clear()
            self.dealer_count = 0
            self.player_count = 0
            os.system('cls' if os.name == 'nt' else 'clear')
            self.main()

        elif prompt == 'n':
            quit()

    def hit_me(self):
        for x in range(1):
            deal = self.deck.pop()
            
            if len(deal) == 2:
                x = int(deal[0])
                self.player_count += x 

            elif len(deal) == 3:
                x = int(deal[:2])
                if x > 10 and x != 14:
                    self.player_count += 10
                elif x == 14 and self.player_count >= 11:
                    self.player_count += 1
                elif x == 14 and self.player_count < 11:
                    self.player_count += 11
                else:
                    self.player_count += x
            
            if x == 11:
                deal = 'J' + deal[-1]
            if x == 12:
                deal = 'Q' + deal[-1]
            if x == 13:
                deal = 'K' + deal[-1]
            if x == 14:
                deal = 'A' + deal[-1]
            self.player_cards.append(deal)

        if self.player_count < 21:
            self.show_cards_hide_dealer_card()
            self.user_decision()

        self.check_scores()
        self.show_cards_hide_dealer_card()

    def user_decision(self):
        self.decision = input("Hit or hold? Type 'quit' to quit\n")
        
        if self.decision.lower() == "hit":
            self.hit_me()
        elif self.decision.lower() == "hold":
            self.dealer_choice()
        elif self.decision.lower() == "quit":
            quit()
        else:
            print('Not an option dummy.')
        
        self.show_cards_hide_dealer_card()

    def check_scores(self):
        if self.dealer_count == 21:
            print('**************************************')
            print(Fore.RED, Style.BRIGHT,'Dealer hit 21, you lose.', Style.RESET_ALL)
            self.show_final_results()            
            self.another_round()

        elif self.player_count > 21:
            self.show_final_results()
            print(Fore.RED, Style.BRIGHT,'You went over 21, you lose.', Style.RESET_ALL)
            self.another_round()

        elif self.dealer_count > 21:
            self.show_final_results()
            print(Fore.BLUE, Style.BRIGHT,'Dealer busted, you win!.', Style.RESET_ALL)
            self.another_round()
        
        elif self.player_count == self.dealer_count:
            print('**************************************')
            print(Fore.RED, Style.BRIGHT,'Tie game, but dealer wins. (Dumb rule, I know!).', Style.RESET_ALL)
            self.show_final_results()
            self.another_round()
        
        elif self.player_count > self.dealer_count:
            print('**************************************')
            print(Fore.BLUE, Style.BRIGHT,'You win!!!', Style.RESET_ALL)
            self.show_final_results()
            self.another_round()

        elif self.player_count < self.dealer_count:
            print('**************************************')
            print(Fore.RED, Style.BRIGHT,'You lose, sucka!', Style.RESET_ALL)
            self.show_final_results()
            self.another_round()

    def dealer_choice(self):
        if self.dealer_count >= 17:
            self.check_scores()
        
        elif self.dealer_count <17:
            self.deal_cards_to_dealer()
            

    def deal_cards_to_dealer(self):
        random.shuffle(self.deck)
        for x in range(1):
            deal = self.deck.pop()

            if len(deal) == 2:
                x = int(deal[0])
                self.dealer_count += x 

            elif len(deal) == 3:
                x = int(deal[:2])
                if x > 10 and x != 14:
                    self.dealer_count += 10
                elif x == 14 and self.dealer_count >= 11:
                    self.dealer_count += 1
                elif x == 14 and self.dealer_count < 11:
                    self.dealer_count += 11
                else:
                    self.dealer_count += x  

            if x == 11:
                deal = 'J' + deal[-1]
            if x == 12:
                deal = 'Q' + deal[-1]
            if x == 13:
                deal = 'K' + deal[-1]
            if x == 14:
                deal = 'A' + deal[-1]

            self.dealer_cards.append(deal)

        self.dealer_choice()
   
    def main(self):
    
        if self.temp_count == 0:
            print(Fore.GREEN, Style.BRIGHT, '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
            print(figlet_format('  BLACKJACK!'))
            print(Fore.GREEN, Style.BRIGHT, '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$', Style.RESET_ALL)
            input("Enter any key to play: \n")
        self.temp_count += 1

        # Deal cards to dealer to start.
        self.deal_cards_to_dealer_start()

        if self.dealer_count == 21:
            print('BLACKJACK, dealer wins. You suck.')
            self.show_final_results()
            self.another_round()

        #Deal first cards to player
        self.hit_me_start()

        if self.player_count == 21:
            print("BLACKJACK, winner winner chicken dinner.")
            self.show_final_results()
            self.another_round()

        self.user_decision()
        

play = Blackjack()
play.main()
