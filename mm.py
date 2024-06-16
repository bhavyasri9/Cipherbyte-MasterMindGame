def res(secret,guess):
    crtPos=sum(1 for s, g in zip(secret,guess) if s == g)
    crtDig=sum(min(secret.count(x),guess.count(x)) for x in set(guess))
    wrnPos=crtDig-crtPos
    return crtPos,wrnPos
def play(secret):
    atmpt=0
    while True:
        guess=input("guess a 4-digit number : ")
        atmpt+=1
        crtPos,wrnPos=res(secret,guess)
        if crtPos==4:
            print("🎉 Correct! You've guessed the number!")
            break
        else:
            print(f"🟩 Correct position: {crtPos} | 🟨 Correct number, wrong position: {wrnPos}")
    return atmpt
def MASTERMIND():
    print("Player 1, set your number.")
    p1_secret=input("Player 1, enter a 4-digit secret number: ")
    print("\nPlayer 2, it's your turn to guess.")
    p2_atmpts=play(p1_secret)

    print("\nSwitching roles....")
    print("Player 2, set your number.")
    p2_secret=input("Player 1, enter a 4-digit secret number: ")
    print("\nPlayer 1, it's your turn to guess.")
    p1_atmpts=play(p2_secret)

    print("\nGame Over!")
    print(f"Player 1 attempts: {p1_atmpts}")
    print(f"Player 2 attempts: {p2_atmpts}")

    if p1_atmpts < p2_atmpts:
        print("🏆 Player 1 wins and is crowned Mastermind!")
    elif p1_atmpts > p2_atmpts:
        print("🏆 Player 2 wins and is crowned Mastermind!")
    else:
        print("🤝 It's a tie!")
MASTERMIND()