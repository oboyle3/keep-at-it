from django.shortcuts import render
from .game_logic import check_guess, choose_word

def wordle_home(request):
    rand_word = choose_word()

    print(f"rand word = {rand_word}")
    print("WORDLE VIEW WAS CALLED")

    if request.method == "POST":
        guess = request.POST.get("guess")
        print(guess)

        if guess == rand_word:
            print("you win, Congrats!")
        else:
            print("you didn't get it right")

    return render(request, "wordle/index.html")