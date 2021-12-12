class Instr:

    def __init__(self,line):
         (cmd,num) = line.rstrip("\n").split()
         self.cmd = cmd
         self.num = int(num)
         self.empty = False

    def __str__(self):
        return self.cmd+" "+str(self.num)

    def thecmd(self):
        return self.cmd

    def thenum(self):
        return self.num

    def updatecmd(self,cmd):
        self.cmd = cmd

    def makeempty(self):
        self.empty = True

    def makenotempty(self):
        self.empty = False

commands = []

with open("input8.txt","r") as input:
    for line in input:
        commands.append(Instr(line))

#for x in commands:
#    print(x)

def run(start,cmds):
    global acc, success

    if start >= len(cmds):
        success = 1
        return

    cmd = cmds[start].thecmd()
    num = cmds[start].thenum()
    empty = cmds[start].empty

#    print(cmd+" "+str(num))

    cmds[start].makeempty()

    if empty:
        return
    elif cmd == "nop":
        run(start+1,cmds)
    elif cmd == "acc":
        acc += num
        run(start+1,cmds)
    elif cmd == "jmp":
        run(start+num,cmds)

#acc = 0
#run(0,commands)
#print(acc)


def testreplace(fr,to):

    global commands, acc, success

    for x in [el for el in commands if el.thecmd() == fr]:
        acc = 0
        success = 0

        for cmd in commands:
            cmd.makenotempty()

        x.updatecmd(to)

#            print("newrun")
#            for c in commands:
#                print(c)

        run(0,commands)

        if success:
            print("Success!")
            print(acc)
            break
        else:
            x.updatecmd(fr)


acc = 0
success = 0

testreplace("jmp","nop")
testreplace("nop","jmp")
