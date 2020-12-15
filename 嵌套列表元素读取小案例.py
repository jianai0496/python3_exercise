a= [[1,3,2,6,7,8],[7,3,4],[8,4,2]]
for i in range(len(a)):
    print(a[i],end='---\n')
    for j in range(len(a[i])):
        print("中的元素有{}".format(a[i][j]))