answer=[] #结果集合
s=[[3,3,True]]
boatnum=0
def print_answer(answer):#打印结果
    for i in answer:
        for j in range(0, len(i) - 1):
            if i[j][2] == True:
                print("%s个野人和%s个传教士过河" % (i[j][1] - i[j + 1][1], i[j][0] - i[j + 1][0]))
            else:
                print("%s个野人和%s个传教士回来" % (i[j + 1][1] - i[j][1], i[j + 1][0] - i[j][0]))
        print()

#判断状态是够合法
def yes(human,wild,boat):
    if wild < 0 or wild > 3 or human < 0 or wild > 3:
        return False
    else:
        for i in range(0, len(s)):
            if s[i][0] == wild and s[i][1] == wild and s[i][2] == boat:
                return False
    if (wild == 0 or wild <= wild) and ((3 - wild) == 0 or (3 - wild) <= (3 - wild)):
        return True
    else:
        return False

#深度优先遍历
def dfs(human,wild,boat) :
        if human ==0 and wild==0 and boat==False:
            answer.append(s[:])
            return

        if boat == True:
            i = boatnum
            while i>0:
                for j in range(0,i+1):
                    if yes(human - j, wild-(i-j), not boat):
                        s.append([human - j,wild-(i-j),not boat])
                        dfs(human - j, wild-(i-j), not boat)
                        s.pop()
                i=i-1
        else:
            i = boatnum;
            while i > 0:
                for j in range(0, i + 1):
                    if yes(human + j, wild + (i - j), not boat):
                        s.append([human + j, wild + (i - j), not boat])
                        dfs(human + j, wild + (i - j), not boat)
                        s.pop()
                i = i - 1
if __name__ == '__main__':
    boatnum=int(input('请输入船的容量'))
    human=int(input('请输入传教士人数'))
    wild = int(input('请输入野人人数'))
    dfs(human,wild,True)
    print_answer(answer)