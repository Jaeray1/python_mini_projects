import random
user = input("rock/paper/scissors: ").lower()
comp = random.choice(['rock','paper','scissors'])
print(f"Computer: {comp}")
if user==comp: print("Draw")
elif (user=='rock' and comp=='scissors') or (user=='paper' and comp=='rock') or (user=='scissors' and comp=='paper'):
    print("You Win!")
else: print("You Lose!")
