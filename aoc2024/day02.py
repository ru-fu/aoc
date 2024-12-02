import sys

inputfile = ""

if len(sys.argv) == 2:
  inputfile = sys.argv[1] + ".txt"
else:
  inputfile = "input" + sys.argv[0][3:5] + ".txt"

reports = []
  
with open(inputfile,"r") as input:

  for line in input:
    linelist = line.rstrip().split(" ")
    reports.append([int(x) for x in linelist])

safe = []
    
def run_part1():

  incs = []
  decs = []

  for report in reports:
    copy = report.copy()
    copy.sort()
    if report == copy:
      incs.append(report)
    copy.sort(reverse=True)
    if report == copy:
      decs.append(report)

  for report in incs:
    ok = check(report)
    if ok:
      safe.append(report)

  for report in decs:
    ok = check(report)
    if ok:
      safe.append(report)
      
#  print(incs)
#  print(decs)
#  print(safe)
  print(len(safe))

def run_part2():

  safe2 = []

  for report in reports:
    if report in safe:
      safe2.append(report)
    elif check2(report):
      safe2.append(report)

  #print(safe2)
  print(len(safe2))


def check(report):
    prev = None
     
    for num in report:
      if prev == None:
        prev = num
      else:
        diff = abs(num - prev)
        if diff > 0 and diff < 4:
          prev = num
        else:
          return 0
        
    return 1

def check2(report):
  for i in range(len(report)):
    dropped = report.copy()
    dropped.pop(i)

    copy = dropped.copy()
    copy.sort()
    if dropped == copy and check(dropped):
      return 1
    else:
      copy.sort(reverse=True)
      if dropped == copy and check(dropped):
        return 1

  return 0

run_part1()
run_part2()
