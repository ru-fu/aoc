#target_x1 = 20
#target_x2 = 30
#target_y1 = -10
#target_y2 = -5
target_x1 = 201
target_x2 = 230
target_y1 = -99
target_y2 = -65

class Probe:

    def __init__(self,x,y):
        self.x_pos = 0
        self.y_pos = 0
        self.x_vel = x
        self.y_vel = y
        self.highest = 0

    def __str__(self):
        return "Position: "+str(self.x_pos)+","+str(self.y_pos)+" Velocity: "+str(self.x_vel)+","+str(self.y_vel)+" Higest: "+str(self.highest)

    def move(self):
        self.x_pos += self.x_vel
        self.y_pos += self.y_vel
        if self.x_vel > 0:
            self.x_vel += -1
        elif self.x_vel < 0:
            self.x_vel += 1
        self.y_vel += -1
#        print(self)

    def launch(self):
        self.move()
        if self.y_pos > self.highest:
            self.highest = self.y_pos
        if self.x_pos > target_x2 or self.y_pos < target_y1:
            return 0
        if self.x_pos >= target_x1 and self.y_pos <= target_y2:
            return 1
        return self.launch()

    def max(self):
        return self.highest

highest = 0
count = 0

for x in range(target_x2+1):
    for y in range(target_y1,100):
        p = Probe(x,y)
        if p.launch():
            count += 1
           # print("x: "+str(x)+" y: "+str(y))
            if p.max() > highest:
                highest = p.max()

print(highest)
print(count)
