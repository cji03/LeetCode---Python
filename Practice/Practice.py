# 1.判断string是否是回文
import re
def is_palindrome(s):
  s = re.findall(r'[a-z]', s.lower())
  return s == s[::-1]

s='Rise to vote, sir.'
print is_palindrome(s)

# 2.文件读写
poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!
'''
# 打开文件以编辑（'w'riting）
with open('poem.txt', 'w') as f:
# 向文件中编写文本
  f.write(poem)
# with结束后会自动关闭文件

# 如果没有特别指定，
# 将假定启用默认的阅读（'r'ead）模式
with open('poem.txt', 'r') as f:
  for line in f:
    print line

# 3. a, b = <some expression> 的用法会将表达式的结果解释为具有两个值的一个元组
# 交换两个变量的最快方法
a, b = 5, 8
a, b = b, a

# 4. 排序
l = [8,2,50,3]
l.sort() #直接修改原列表
ll=sorted(l) #返回新列表，原列表不变
# 对dict排序
a={1:4,2:3,3:2}
b=sorted(a) #按key排序
c=sorted(a.values()) #按value排序
# 对多维列表排序
student_tuples = [('john', 'A', 15),('jane', 'B', 12),('dave', 'B', 10)]
sorted(student_tuples, key = lambda student: student[0]) # 对姓名排序
sorted(student_tuples, key = lambda student: student[2])  # 年龄排序

# 5.反转string
#切片 最佳方法
a='xydz'
print(a[::-1])
# reversed() 次佳方法
b=''.join(reversed(a))

# 6.求100内素数，数本身内否被平方根后的数list整除。
b=[0, 1]
for i in xrange(2,101):
  for x in xrange(2,int(i**0.5)+1):
    if i % x == 0:
      break
  else:
    b.append(i)

#7. 求中位数
L=[5,4,6,3,8,2,7,1]
def get_median(L):
  L.sort()
  if(len(L)%2==0):
    return (L[len(L)//2-1]+L[len(L)//2])/2.0
  else:
    return L[len(L)//2]
# Method 2 按位取反
def get_median2(data):
  data.sort()
  half = len(data) // 2
  return (data[half] + data[~half]) / 2 #按位取反

# 8.最大公约数问题
#辗转相除法
a,b=1000,24

def gcd(x , y):
  return x if y == 0 else gcd(y, x%y)
#非递归
def gcd2(x, y):
  while y:
    x, y = y, x%y
  return x

#辗转相除法+更相减损术+移位运算
def gcd3(x, y):
  if x==y: return x
  if x<y: 
    return gcd3(y,x)
  else: 
    if (not x&1) and (not y&1):
      return gcd3(x>>1,y>>1)<<1
    elif x&1 and (not y&1):
      return gcd3(x,y>>1)
    elif (not x&1) and y&1:
      return gcd3(x>>1,y)
    else:
      return gcd3(y, x-y)

# 最小公倍数（最小公倍数=两整数的乘积÷最大公约数）
def lcm(x,y):
  return x*y//gcd3(x,y)

# 10. 9位数转换人民币金额
n=200067000
def Cyuan(a):
  s=str(abs(a))
  if len(s)>9: return 'Invalid Number'
  M=[u'零',u'壹',u'贰',u'叁',u'肆',u'伍',u'陆',u'柒',u'捌',u'玖']
  N=['',u'圆',u'拾',u'佰',u'仟',u'万',u'拾',u'佰',u'仟',u'亿',u'零']
  O={u'零仟':u'零',u'零佰':u'零',u'零拾':u'零',u'零零零':u'零',u'零零':u'零',u'零万':u'万',u'零圆':u'圆',u'亿万':u'亿'}
  r=('' if a>=0 else u'负')
  for i in range(0,len(s)):
    r=r+M[int(s[i])]+N[len(s)-i]
  for i in O:
    r=r.replace(i,O[i]) # 暴力替换
  return r

# Python成员运算符 if..in..
a='lislejloveljslf'
print('LOVE' if 'love' in a.lower() else 'SINGLE')

#11.斐波那契数列（Fibonacci sequence）
def fib(n):
  a,b = 1,1
  for i in range(n-1):
    a,b = b,a+b
  return a
# 输出了第n个斐波那契数列
print fib(2)

# 12.对n进行分解质因数
n=90
def divid(n):
  m=[]
  for i in xrange(2, n+1):
    while n!=i:
      if n%i==0:
        m.append(i)
        n=n/i
      else:
        break
    else:
      m.append(i)
      break
  return m
