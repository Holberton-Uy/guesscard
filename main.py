from requests import get

base_uri = 'https://deckofcardsapi.com/api/deck/'

cards = {'ACE':1, 'QUEEN':10, 'JACK':10, 'KING':10}

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
        value, remaining = data['cards'][0]['value'], data['remaining']
        if (not value.isnumeric()):
            value = cards[value]
        return int(value), int(remaining)
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
        last_value, remaining = draw_card_value(deck_id, 1)
        print(f"Card value is: {last_value}")
        while not game_over and remaining:
            ans = input("Next is + (higher) or - (lower)? ")
            while (ans != '-' and ans != '+'):
                ans = input("Next is + (higher) or - (lower)? ")
            new_value, remaining = draw_card_value(deck_id, 1)
            print(f"Card value is: {new_value}")
            if (not check_cards(ans, last_value, new_value)):
                game_over = True
                break
            last_value = new_value
            points += 1
        if game_over:
            print(f"Sorry, you lose. Your score is {points}")
            exit(0)
        print("YOU WON!")
    except Exception:
        print("PANIC: Error contacting API.")
        exit(1)

main()