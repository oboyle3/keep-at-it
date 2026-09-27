from django.shortcuts import render
from .game_logic import check_guess
#.\venv\Scripts\Activate.ps1
def wordle_home(request):
    if request.method == "POST":
        guess = request.POST.get("guess")
        print(guess)
        result = check_guess(guess, "beach")
        print(result)
    return render(request, "wordle/index.html")