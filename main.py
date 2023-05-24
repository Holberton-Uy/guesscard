from requests import get
from card import Card

base_uri = 'https://deckofcardsapi.com/api/deck/'

def shuffle_deck(count=1):
    shuffle = f'{base_uri}new/shuffle/?deck_count={count}'
    r = get(shuffle)
    if(r):
        data = r.json()
        return data['deck_id']
    raise Exception

def draw_card_value(deck_id, count=1):
    shuffle = f'{base_uri}{deck_id}/draw/?count{count}'
    r = get(shuffle)
    if(r):
        data = r.json()
        card, remaining = Card(**data['cards'][0]), data['remaining']
        return card, int(remaining)
    raise Exception

def check_cards(guess, old_value, new_value):
    if (guess == '+'):
        return old_value <= new_value
    if (guess == '-'):
        return old_value >= new_value

def main():
    game_over = False
    points = 0
    try:
        deck_id = shuffle_deck(3)
        last_card, remaining = draw_card_value(deck_id, 1)
        print(f"Card value is: {last_card}")
        while not game_over and remaining:
            ans = input("Next is + (higher) or - (lower)? ")
            while (ans != '-' and ans != '+'):
                ans = input("Next is + (higher) or - (lower)? ")
            new_card, remaining = draw_card_value(deck_id, 1)
            print(f"Card value is: {new_card}")
            if (not check_cards(ans, last_card, new_card)):
                game_over = True
                break
            last_card = new_card
            points += 1
        if game_over:
            print(f"Sorry, you lose. Your score is {points}")
            exit(0)
        print("YOU WON!")
    except Exception as e:
        print(e)
        print("PANIC: Error contacting API.")
        exit(1)

main()