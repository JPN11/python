import random

cards = [
    {"name": "Ace", "value": 11},
    {"name": "2", "value": 2},
    {"name": "3", "value": 3},
    {"name": "4", "value": 4},
    {"name": "5", "value": 5},
    {"name": "6", "value": 6},
    {"name": "7", "value": 7},
    {"name": "8", "value": 8},
    {"name": "9", "value": 9},
    {"name": "10", "value": 10},
    {"name": "Jack", "value": 10},
    {"name": "Queen", "value": 10},
    {"name": "King", "value": 10},
]


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.bet = 0
        self.money = 1000  # Each player starts with $1000

    def deal_card(self):
        draw = random.choice(cards)
        self.hand.append(draw)
        if draw["name"] == "Ace":
            ace_value = int(
                input(
                    f"{self.name}, you were dealt an Ace. Do you want to count Ace as 11 or 1? [11/1] "
                )
            )
            while ace_value not in [11, 1]:
                ace_value = int(
                    input(
                        f"Invalid choice, {self.name}. Do you want to count Ace as 11 or 1? [11/1] "
                    )
                )
            draw["value"] = ace_value  # Update the value of Ace in the hand

    def calculate_hand_value(self):
        total_value = sum(card["value"] for card in self.hand)
        # Adjust for Aces if total value exceeds 21
        aces_count = sum(1 for card in self.hand if card["name"] == "Ace")
        while total_value > 21 and aces_count:
            total_value -= 10  # Count Ace as 1 instead of 11
            aces_count -= 1
        return total_value

    def hit_or_stay(self):
        choice = input(f"{self.name}, do you want to hit? [y/n] ")
        if choice.lower() == "y":
            self.deal_card()
            print(f"{self.name} got a {self.hand[-1]['name']}")
        elif choice.lower() == "n":
            pass
        else:
            print("Invalid choice. Please enter y or n.")
            self.hit_or_stay()

    def place_bet(self):
        while True:
            try:
                self.bet = int(input(f"{self.name}, enter your bet: "))
                if self.bet > self.money:
                    print("You don't have enough money to bet that much.")
                else:
                    self.money -= self.bet  # Deduct the bet from player's money
                    break
            except ValueError:
                print("Invalid bet. Please enter a number.")


class Game:
    def __init__(self):
        self.players = []
        self.gameover = False

    def dealer_turn(self, dealer):
        dealer_value = dealer.calculate_hand_value()
        print(f"Dealer's hand value is {dealer_value}")

        for player in self.players:
            player_value = player.calculate_hand_value()
            if player_value > 21:
                print(f"{player.name} busts! Dealer wins.")
                print(f"{player.name} now has ${player.money}")
            elif dealer_value > 21:
                print(f"Dealer busts! {player.name} wins.")
                player.money += player.bet * 2
                print(f"{player.name} now has ${player.money}")
            elif player_value > dealer_value:
                print(f"{player.name} wins!")
                player.money += player.bet * 2
                print(f"{player.name} now has ${player.money}")
            elif player_value < dealer_value:
                print("Dealer wins!")
                print(f"{player.name} now has ${player.money}")
            else:
                print("It's a tie!")
                player.money += player.bet  # Player gets their bet back
                print(f"{player.name} now has ${player.money}")

        # Ask if players want to play again
        play_again = input("Do you want to play again? [y/n] ")
        if play_again.lower() == "y":
            for player in self.players:
                player.hand = []
                player.bet = 0
        else:
            self.gameover = True

    def main(self):
        print(r""".------..------..------..------..------..------..------..------..------.
|B.--. ||L.--. ||A.--. ||C.--. ||K.--. ||J.--. ||A.--. ||C.--. ||K.--. |
| :(): || :/\: || (\/) || :/\: || :/\: || :(): || (\/) || :/\: || :/\: |
| ()() || (__) || :\/: || :\/: || :\/: || ()() || :\/: || :\/: || :\/: |
| '--'B|| '--'L|| '--'A|| '--'C|| '--'K|| '--'J|| '--'A|| '--'C|| '--'K|
`------'`------'`------'`------'`------'`------'`------'`------'`------'""")
        print("Starting money: 1000")
        player_num = int(input("How many players? "))
        for _ in range(player_num):
            player_name = input("Enter player name: ")
            self.players.append(Player(player_name))

        while not self.gameover:
            dealer = Player("Dealer")
            dealer.deal_card()
            dealer.deal_card()
            print(f"Dealer's up card is {dealer .hand[0]['name']}")

            for player in self.players:
                player.place_bet()
                player.deal_card()
                player.deal_card()
                print(
                    f"{player.name}'s hand is {player.hand[0]['name']} and {player.hand[1]['name']}"
                )
                player.hit_or_stay()
                print(f"{player.name}'s hand value is {player.calculate_hand_value()}")

            while dealer.calculate_hand_value() < 17:
                dealer.deal_card()
            self.dealer_turn(dealer)


# To start the game, create an instance of Game and call the main method
if __name__ == "__main__":
    game = Game()
    game.main()
