# 下过象棋的人都知道，马只能走'日'字形（包括旋转90°的日），现在想象一下，给你一个n行m列网格棋盘，
# 棋盘的左下角有一匹马，请你计算至少需要几步可以将它移动到棋盘的右上角，若无法走到，则输出-1.
# 如n=1，m=2,则至少需要1步；若n=1，m=3,则输出-1。

def bfs(n,m):
  vs, vd = [0,0,0], [n,m]
  Q = []
  visited=[[0]*(m+1) for i in xrange(n+1)]  # 生成一个map，m行，n列
  visited[0][0] = 1
  dx=[1,1,2,2,-1,-1,-2,-2]
  dy=[2,-2,1,-1,2,-2,1,-1]
  Q.append(vs)
  while Q:
    vn=Q.pop(0)
    if [vn[0],vn[1]] == vd:
      return vn[2]
    for (x,y) in zip(dx,dy):
      vnx=vn[0]+x
      vny=vn[1]+y
      index=vn[2]+1
      if 0<=vnx<=n and 0<=vny<=m and visited[vnx][vny] != 1:
        visited[vnx][vny] = 1
        Q.append([vnx, vny, index])
  else:
    return -1
print bfs(n,m)


# 首先我们需要一个队列Q存储待访问的点，一个map记录访问过的点visited[maxL][maxH]，起始点为vs=[0,0,0]0,1两点记录坐标，2点记录index步长, 结束点为vd=[n,m], Q.append(vs), 把起始点丢进队列里。
# 马走日，创建两个list列出x和y可走的方向dx=[1,1,2,2,-1,-1,-2,-2], dy=[2,-2,1,-1,2,-2,1,-1]
# while Q: 只要有未访问的点，就执行循环。
# vn=Q.pop(0), 取出队列第一个点并抛掉, if [vn[0],vn[1]] == vd: return vn[2] 如果发现此点就是想要的点，直接返回index步长，得到结果。
# 如果不是结果，就寻找与此节点相邻的未访问的点：
#   for (x,y) in zip(dx,dy): #我这边用了zip打包dx，dy。也可以直接就写成二维
#     vnx=vn[0]+x  # for循环出所有可能的下一个节点
#     vny=vn[1]+y
#     index=vn[2]+1 # 步长为vn的步长+1，就是上一个节点的index+1
#     if 0<=vnx<=n and 0<=vny<=m and visited[vnx][vny] != 1: # 判断是否超出边界，是否已经访问过
#       visited[vnx][vny] = 1  # 标记节点已访问，并插入队列Q
#       Q.append([vnx, vny, index])
# 最后检索完毕没有找到结果，return -1
# 方法仅供参考，虽然过了你那个题目的测试。
