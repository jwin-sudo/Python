import random


diamonds = ["AD", "2D", "3D", "4D", "5D",
            "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:
    response = input("Press enter to pick a card, or Q then enter to quit")
    if(response == "Q"):
        break

    selected_card = random.choice(diamonds)
    diamonds.remove(selected_card)
    hand.append(selected_card)
    print(f'Your hand: {hand}')
    print(f'Remaining cards: {diamonds}')

    if not diamonds:
        print('There are no more cards to pick.')
