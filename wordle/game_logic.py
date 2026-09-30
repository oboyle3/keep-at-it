import random
avail_words = ["apple", "house", "plant", "chair", "table", "water", "green", "black", "white", "world", "light", "sound", "music", "river", "ocean", "beach", "cloud", "storm", "grass", "stone", "bread", "money", "phone", "train", "plane", "truck", "horse", "sheep", "tiger", "eagle", "mouse", "snake", "grape", "peach", "lemon", "berry", "pizza", "pasta", "sugar", "sweet", "happy", "smile", "laugh", "dream", "sleep", "think", "learn", "write", "read", "study"]


def choose_word():
    return random.choice(avail_words)


def check_guess(guess, answer):
    if guess == answer:
        print("nice  its the same")
    else:
        print("bad not the same")

def check_user_input_length(guess):
    length = len(guess)
    if length != 5:
        print("check_user_input_length VIOLATION    must be 5 letters")
        return False
    else:
        print("check_user_input_length PASSED")
        return True
    

def check_whats_missing(guess,ans):
    common = set(guess) & set(ans)
    print(f"fyi i am calling check_whats_missing :::  {sorted(list(common))}")
    return common