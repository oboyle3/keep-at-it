from django.shortcuts import render
from .game_logic import check_guess, choose_word, check_user_input_length, check_whats_missing,letters_in_correst_postion_check

def wordle_home(request):
    if "wordle_ans" not in request.session:
        print("sxxxxxxxxxxxxxxxxxxxxxxxx")
        request.session["wordle_ans"] = choose_word()
    rand_word = request.session["wordle_ans"]
    print(f"WORDLE VIEW WAS CALLED  random wordle ans = {rand_word}")
    message_to_user = ""  #avoid being returned every time
    message_of_correct_letter = ""#avoid being returned every time
    message_of_user_win = ""
    # count_user_tries = 0
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
                message_of_user_win = "you win, Congrats!"
            else:
                print("you didn't get it right")
                #check if there are any simlar letters
                print(f"check what miss {check_whats_missing(guess,rand_word)}")
                message_of_correct_letter = check_whats_missing(guess, rand_word)

                print(f"correct letters: {message_of_correct_letter}")
                print(f"message_of_correct_letter - {message_of_correct_letter}")
                letters_in = letters_in_correst_postion_check(guess,rand_word)

    return render(
    request,
    "wordle/index.html",
    {
        "message_to_user": message_to_user,
        "message_of_correct_letter":message_of_correct_letter,
        "message_of_user_win": message_of_user_win,
        "letters_in": letters_in,
        
        }
)
