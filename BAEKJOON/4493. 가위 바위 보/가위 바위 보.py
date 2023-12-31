N1 = int(input())

player1 = 0
player2 = 0

for i in range(N1):
    N2 = int(input())
    for j in range(N2):

        W1, W2 = input().split()
        
        if W1 == 'R':
            if W2 == 'S':
                player1 += 1
            if W2 == 'P':
                player2 += 1
        if W1 == 'S':
            if W2 == 'R':
                player2 += 1
            if W2 == 'P':
                player1 += 1

        if W1 == 'P':
            if W2 == 'R':
                player1 += 1
            if W2 == 'S':
                player2 += 1

    if player1 > player2:
        print("Player 1")
    if player1 < player2:
        print("Player 2")
    if player1 == player2:
        print("TIE")

    player1 = 0
    player2 = 0