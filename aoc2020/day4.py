
with open("input4.txt","r") as input:

  passport = ""
  passports = []

  for line in input:

    if line.strip():

      passport = passport + " " + line.strip()

    else:

      passports.append(passport)
      passport = ""

if passport != "":
  passports.append(passport)

def verify(dictionary, strict=False):

  required = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]

  for check in required:

    if not check in dictionary:

      print("missing " + check)
      return False

  if strict:

    if not ((1919 < int(dictionary["byr"]) < 2003) and (dictionary["byr"].isdigit()) and (len(dictionary["byr"]) == 4)):
      print("failing byr")
      return False

    if not ((2009 < int(dictionary["iyr"]) < 2021) and (dictionary["iyr"].isdigit()) and (len(dictionary["iyr"]) == 4)):
      print("failing iyr")
      return False

    if not ((2019 < int(dictionary["eyr"]) < 2031) and (dictionary["eyr"].isdigit()) and (len(dictionary["eyr"]) == 4)):
      print("failing eyr")
      return False

    if not (dictionary["hgt"].endswith("cm") or dictionary["hgt"].endswith("in")):
      print("failing hgt")
      return False

    if dictionary["hgt"].endswith("cm") and not 149 < int(dictionary["hgt"].replace("cm","")) < 194:
      print("failing hgt number")
      return False

    if dictionary["hgt"].endswith("in") and not 58 < int(dictionary["hgt"].replace("in","")) < 77:
      print("failing hgt number")
      return False

    if not ( dictionary["hcl"].startswith("#") and dictionary["hcl"].count("#") == 1 and dictionary["hcl"].replace("#","").isalnum() and len(dictionary["hcl"]) == 7):
      print("failing hcl")
      return False

    if not dictionary["ecl"] in ["amb","blu","brn","gry","grn","hzl","oth"]:
      print("failing ecl")
      return False

    if not (dictionary["pid"].isdigit() and len(dictionary["pid"]) == 9):
      print("failing pid")
      return False

  return True

valid = 0

for x in passports:

  dict = {}

  for entry in x.split():

    [key,value] = entry.split(":")
    dict[key] = value

  if verify(dict,True):
    valid += 1
  else:
    print(dict)


print(valid)
