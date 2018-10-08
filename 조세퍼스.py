input_list = input().split()

input_list = [int(i) for i in input_list]

#테이블에 앉은 사람의 수
N = input_list[0]
#M번째 사람마다 죽이기 !
M = input_list[1]


josephus_permutation =[]
table = [i for i in range(1,N+1)]
length = len(table)

while len(table) != 0 :

    if length == 0:
        break

    if length < M:
        M = M % length

    for i in range(length):


        if i == M-1 :
            josephus_permutation.append(table[M-1])
            table.remove(table[M-1])
            # 테이블의 마지막 숫자를 지우면 빠져나가기 !
            if len(table) == 0:
                break

            if M-1 == 0:
                M +=1
                for i in range(M-1):
                    table.append(table[0])
                    table.remove(table[0])
                M -=1
            else:
                for i in range(M-1):
                    table.append(table[0])
                    table.remove(table[0])
            length -= 1
            break



print("<",end="")
for i in range(len(josephus_permutation)-1):
    print(josephus_permutation[i],end=", ")
print(josephus_permutation[-1],end='')


print(">")
