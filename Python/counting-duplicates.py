def duplicate_count(text):
    # Your code goes here

    duplicate = 0
    unique_letters = set(text.lower())
    for letter in unique_letters:
        if text.lower().count(letter)>1:
            duplicate+=1
    
    return duplicate