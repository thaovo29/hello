test = int(input())
input()
for _ in range(test):
    tree = dict()
    treeName = []
    cnt = 0
    while True:
        try :
            s = input()
            if s == '':
                break
        except EOFError:
            break
        cnt += 1
        if s not in tree:
            tree[s] = 1
            treeName.append(s)
        else:
            tree[s] += 1
    treeName.sort()
    for i in tree:
        print( i + " {:.4f}".format((tree[i] / cnt) * 100))
    print()
