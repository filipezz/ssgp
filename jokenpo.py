import random

def play():
    user = input("Choose one: 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 's', 'p'])

    if user == computer:
        return 'tie'
    if is_win(user, computer):
        return 'You won!'
    print(f'Computer choice: {computer}')
    return 'You lost!'

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())