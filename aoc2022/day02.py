game = []

with open("input02.txt","r") as input:

  for line in input:
    game.append((line[0],line[2]))

scores = []

for (they, you) in game:
  score = 0
  if you == "X":
    score += 1
  elif you == "Y":
    score += 2
  elif you == "Z":
    score += 3
  else:
    print("huh?")
  if (you == "X" and they == "C") or (you == "Y" and they == "A") or (you == "Z" and they == "B"):
    score += 6
  elif (you == "X" and they == "A") or (you == "Y" and they == "B") or (you == "Z" and they == "C"):
    score += 3
  scores.append(score)

new_scores = []

for (they, res) in game:
  score = 0
  if res == "Y":
    score += 3
  elif res == "Z":
    score += 6
  if (they == "A" and res == "X") or (they == "C" and res == "Y") or (they == "B" and res == "Z"):
    score += 3 # scissors
  elif (they == "B" and res == "X") or  (they == "A" and res == "Y") or (they == "C" and res == "Z"):
    score += 1 # rock
  else:
    score += 2 # paper

  new_scores.append(score)

def run_part1():

   print(sum(scores))

def run_part2():

   print(sum(new_scores))

run_part1()
run_part2()
