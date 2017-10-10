import random,math
import csv
with open('training.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for i in range(100):
                try:
                        x = random.randint(150,350)
                        y = random.randint(100,200)
                        w= random.randint(200,400)
                        h=w*10.25/5
                        d=w*10.25/320
                        dire=math.atan(float(y+120)/(x-160))
                        print (x,y,w,h,d,dire)
                        spamwriter.writerow([x,y,w,h,d,dire])
                except:
                        continue

