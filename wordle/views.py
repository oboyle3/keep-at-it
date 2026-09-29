from django.shortcuts import render
from .game_logic import check_guess, choose_word, check_user_input_length

def wordle_home(request):
    if "wordle_ans" not in request.session:
        print("sxxxxxxxxxxxxxxxxxxxxxxxx")
        request.session["wordle_ans"] = choose_word()
    rand_word = request.session["wordle_ans"]
    print(f"WORDLE VIEW WAS CALLED  random wordle ans = {rand_word}")
    message_to_user = ""  #avoid being returned every time
    if request.method == "POST":
        guess = request.POST.get("guess")
        print(f"guess = {guess}")
        check_len = check_user_input_length(guess)
        #send message to user if not 5 letters
        
        if not check_len:
            message_to_user = "Cmon man, must be 5 letters"
        print(check_len)
        if check_len:
            if guess == rand_word:
                print("you win, Congrats!")
            else:
                print("you didn't get it right")

    return render(
    request,
    "wordle/index.html",
    {"message_to_user": message_to_user}
)
