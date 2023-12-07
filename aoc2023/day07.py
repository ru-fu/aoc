import sys

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

hands = []

with open(inputfile,"r") as input:

  for line in input:
    hand = line.strip().split()
    hands.append((hand[0],int(hand[1]),0,0))

def score(v,hands):

  for i,hand in enumerate(hands):
    count = {}
    hexval = ""
    for j,card in enumerate(hand[0]):
      if card in count:
        count[card] += 1
      else:
        count[card] = 1
      if card.isdigit():
        hexval += card
      else:
        if card == "T":
          hexval += "A"
        elif card == "J" and v == 1:
          hexval += "B"
        elif card == "J" and v == 2:
          hexval += "1"
        elif card == "Q":
          hexval += "C"
        elif card == "K":
          hexval += "D"
        elif card == "A":
          hexval += "E"

#    print(hexval)
    score = int(hexval,16)
#    print(score)
    counts = list(count.values())
    counts.sort()
    if counts == [5]:
      hands[i] = (hand[0], hand[1], 6, score)
    elif counts == [1, 4]:
      hands[i] = (hand[0], hand[1], 5, score)
      if v == 2 and "J" in count:
        hands[i] = (hand[0], hand[1], 6, score)
    elif counts == [2, 3]:
      hands[i] = (hand[0], hand[1], 4, score)
      if v == 2 and "J" in count:
        hands[i] = (hand[0], hand[1], 6, score)
    elif counts == [1, 1, 3]:
      hands[i] = (hand[0], hand[1], 3, score)
      if v == 2 and "J" in count:
        hands[i] = (hand[0], hand[1], 5, score)
    elif counts == [1, 2, 2]:
      hands[i] = (hand[0], hand[1], 2, score)
      if v == 2 and "J" in count:
        if count["J"] == 2:
          hands[i] = (hand[0], hand[1], 5, score)
        else:
          hands[i] = (hand[0], hand[1], 4, score)
    elif counts == [1, 1, 1, 2]:
      hands[i] = (hand[0], hand[1], 1, score)
      if v == 2 and "J" in count:
        hands[i] = (hand[0], hand[1], 3, score)
    else:
      hands[i] = (hand[0], hand[1], 0, score)
      if v == 2 and "J" in count:
        hands[i] = (hand[0], hand[1], 1, score)


def sort_hands(hand):
  return (hand[2],hand[3])

def run_part1():

  hands1 = list.copy(hands)
  score(1,hands1)

  print(hands1)
  hands1.sort(key=sort_hands)
  print(hands1)

  scores = []
  for i,hand in enumerate(hands1):
    scores.append((i+1) * hand[1])

  print(scores)
  print(sum(scores))

def run_part2():

  hands2 = list.copy(hands)
  score(2,hands2)

  print(hands2)
  hands2.sort(key=sort_hands)
  print(hands2)

  scores = []
  for i,hand in enumerate(hands2):
    scores.append((i+1) * hand[1])
  print(sum(scores))

run_part1()
run_part2()
