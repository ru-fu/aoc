class Number:

  def __init__(self, value):
    self.value = int(value)
    self.prev = None
    self.nxt = None

  def __str__(self):
    return str(self.value)

  def set_prev(self, number):
    self.prev = number

  def set_nxt(self, number):
    self.nxt = number

  def remove(self):
#    print("removing "+str(self)+" (previous: "+str(self.prev)+", next: "+str(self.nxt)+")")
    self.prev.nxt = self.nxt
    self.nxt.prev = self.prev
    self.nxt = None
    self.prev = None


  def insert_after(self,number):
#    print("inserting "+str(self)+" (new previous: "+str(number)+", new next: "+str(number.nxt)+")")
    self.nxt = number.nxt
    self.prev = number
    number.nxt.prev = self
    number.nxt = self

def find_next(start,num):
  res = start
  if num >= 0:
    for i in range(num):
      res = res.nxt
  else:
    for i in range(-num):
      res = res.prev
  return res

def print_ll(sequence,length):

  find = [x for x in sequence if x.value == 0]
  start = find[0]

  collect = ""
  for i in range(length):
    collect += str(start.value)+", "
    start = start.nxt

  print(collect[:-2])

with open("input20.txt","r") as input:

  sequence = []

  for line in input:
    no = Number(line.strip())
    sequence.append(no)

for i,no in enumerate(sequence):
  if i > 0:
    no.set_prev(sequence[i-1])
  else:
    no.set_prev(sequence[-1])
  if i < len(sequence)-1:
    no.set_nxt(sequence[i+1])
  else:
    no.set_nxt(sequence[0])

def run_part1():

  print_ll(sequence,7)

  for no in sequence:
    start = no.prev
    no.remove()
    this = find_next(start,(no.value % (len(sequence) - 1)))
#    if no.value < 0:
#      this = this.prev
#    if not this.value == no.value:
#      no.remove()
#      print("remove "+str(no))
    no.set_nxt(this)
#      print_ll(sequence,7)
#    print("insert "+str(no)+" after: "+str(this))
    no.insert_after(this)
#    print_ll(sequence,7)


#    for x in sequence:
#      print(str(x)+" --- "+str(x.prev)+" --- "+str(x.nxt))

  find = [x for x in sequence if x.value == 0]
  nxt = find[0]
  for i in range(3000):
    nxt = nxt.nxt
    if i == 999:
      thousand = nxt.value
    elif i == 1999:
      twothousand = nxt.value
    elif i == 2999:
      threethousand = nxt.value

  print(thousand)
  print(twothousand)
  print(threethousand)
  print(sum([thousand,twothousand,threethousand]))

def run_part2():

  for i in range(10):
    for no in sequence:
      start = no.prev
      no.remove()
      this = find_next(start,((no.value * 811589153) % (len(sequence) - 1)))
      no.set_nxt(this)
      no.insert_after(this)

  find = [x for x in sequence if x.value == 0]
  nxt = find[0]
  for i in range(3000):
    nxt = nxt.nxt
    if i == 999:
      thousand = nxt.value * 811589153
    elif i == 1999:
      twothousand = nxt.value * 811589153
    elif i == 2999:
      threethousand = nxt.value * 811589153

  print(thousand)
  print(twothousand)
  print(threethousand)
  print(sum([thousand,twothousand,threethousand]))

#run_part1()
run_part2()
