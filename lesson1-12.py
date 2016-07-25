# coding:utf-8
#解决文件中存在中文的问题，而且必须放在源文件第一行，否则会报错。
print "Guess a number!"
from random import randint
#from 文件名 import 模块名
name = raw_input(u'请输入您的名字:')
scores = {}
f = open('game.txt')
lines = f.readlines()

for l in lines:
    s = l.split() #每一行就是一个成绩
    scores[s[0]] = s[1:] #每一行第一个是名字，其它的都是成绩。

score = scores.get(name)
if score is None:
    score = [0,0,0]  #如果没找到，就初始化一个空的数据。

game_times = int(score[0])
min_times = int(score[1])
total_times = int(score[2])
#以上读取记录数据,并显示
if game_times>0:
    avg_times = float(total_times)/game_times
else:
    avg_times = 0
print u'你已经玩了多少轮%d，最快猜出的使用的次数是%d,平均%.2f次猜出答案'%(game_times,min_times,avg_times)
#真正业务部分
times = 0
number = randint(5,100)
print number
bingo = False
while(bingo==False):
    times+=1
    answer = input("please input a number!")
    if answer>number:
        print "%d is too big" % answer
    if answer<number:
        print "%d too small!" % answer
    if answer==number:
        print"bingo!,%d is the right answer!" %answer
        bingo = True
#如果是第一次玩，或者本次的轮数比最小轮数还少，就记录本次成绩为最小轮数：
if game_times==0 or times<min_times:
    min_times = times
total_times+=times
game_times+=1

scores[name] = [str(game_times), str(min_times), str(total_times)]
result = ''

for n in scores:
   line = n + ' ' + ' '.join(scores[n]) + '\n'
   result += line

f = open('game.txt','w')
f.write(result)
f.close()
