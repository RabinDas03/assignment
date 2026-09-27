def last_character(text):
    print("Last character:", text[-1])

text = input("Enter text: ")

last_character(text)

#Approach 2 — Loop

def last_character_loop(text):
    last = ""
    for ch in text:
        last = ch
    print("Last character:", last)

text = input("Enter text: ")
last_character_loop(text)
