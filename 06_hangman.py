import random
word = random.choice(["python","genai","coding","guvi"])
guessed = set()
tries = 6
while tries>0:
    display = "".join([c if c in guessed else "_" for c in word])
    print("Word:", display)
    if display==word: print("You Won!"); break
    g = input("Letter: ").lower()
    guessed.add(g)
    if g not in word:
        tries-=1
        print(f"Wrong, {tries} left")
else: print(f"Lost, word was {word}")
