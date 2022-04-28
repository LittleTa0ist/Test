human=3
wild=3
boatnum=2 #船装人的个数
answer =[] #返回的结果
b=[[3,3,True]] #存储合法状态
#输出结果
def print_answer():
    for i in answer:
        for j in range(0,len(i)-1):
            if i[j][2]==True:
                print("%s个野人和%s个传教士过河"%(i[j][1]-i[j+1][1],i[j][0]-i[j+1][0]))
            else:
                print("%s个野人和%s个传教士回来" % (i[j+1][1]-i[j][1],i[j+1][0]-i[j][0]))
        print()
#判断当前状态是否合法
def yes(human ,wild ,boatAdr) :
    if wild < 0 or wild > 3 or human < 0 or human > 3:
        return False
    else:
        for i in range(0,len(b)):
            if b[i][0] ==human and b[i][1]==wild and b[i][2]==boatAdr:
                return False
    if (human == 0 or wild <= human) and ((3 - human) == 0 or (3 - wild) <= (3 - human)):
        return True
    else:
        return False
count =0
#深度优先搜索
def dfs(human ,wild ,boatAdr) :
        if human ==0 and wild==0 and boatAdr==False:
            answer.append(b[:])
            return

        if boatAdr == True:
            i = boatnum
            while i>0:
                for j in range(0,i+1):
                    if yes(human - j, wild-(i-j), not boatAdr):
                        b.append([human - j,wild-(i-j),not boatAdr])
                        dfs(human - j, wild-(i-j), not boatAdr)
                        b.pop()
                i=i-1
        else:
            i = boatnum
            while i > 0:
                for j in range(0, i + 1):
                    if yes(human + j, wild + (i - j), not boatAdr):
                        b.append([human + j, wild + (i - j), not boatAdr])
                        dfs(human + j, wild + (i - j), not boatAdr)
                        b.pop()
                i = i - 1
if __name__ == "__main__":
    dfs(human,wild,True)
    print_answer()