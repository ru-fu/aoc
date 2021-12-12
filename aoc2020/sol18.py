import re

class n:
  def __init__(self,value):
    self.value = value
  def __mul__(self,other):
    return n(self.value * other.value)
  def __pow__(self,other):
    return n(self.value + other.value)
  def __matmul__(self,other):
    return n(self.value + other.value)
  def __repr__(self):
    return f'n({self.value})'

def apply1(st):
  v = re.sub(r'(\d+)', r'n(\1)', st).replace('+','@')
  res = eval(v).value
  print(res)
  return res

def apply2(st):
  v = re.sub(r'(\d+)', r'n(\1)', st).replace('+','**')
  return eval(v).value

with open('test.txt') as file:
  print(sum(apply1(s) for s in file if s))
#with open('day18.txt') as file:
#  print(sum(apply2(s) for s in file if s))
