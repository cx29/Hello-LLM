from unittest import case

frusts = ['Apple', 'orange', 'banana']

print(frusts)

print(len(frusts))

frusts.append('bob')
print(frusts)

frusts.insert(2, 'abc')
print(frusts)

tuple1 = (1, 2, 3, 4)

print(len(tuple1))

# 这样定义是定义的1这个数， 不是定义的Tuple
tuple2 = (1)
print(tuple2)
# 这样才是定义只有一个元素的tuple
tuple3 = (1,)
print(tuple3)

# tuple 指向不变， 可以理解为指针指向的地址不变，但是这个地址的内容是可变的
tuple4 = (1, frusts)  # 比如说第二个元素指向的是frusts的list， 但是frusts内中的元素是可变的
print(tuple4)
frusts.remove('banana')
print(tuple4)

score = 'B'
if score == 'A':
    print('A')
elif score == 'B':
    print('B')
elif score == 'C':
    print('C')
else:
    print('invalid')

# 模式匹配(switch)
match score:
    case 'A':
        print('A')
    case 'B':
        print('B')
    case 'C':
        print('C')
    case _:
        print('invalid')

# 模式匹配 多条件
age = 13
match age:
    case x if x < 10:
        print('age is less than 10')
    case 10:
        print('age is equal to 10')
    case 11 | 12 | 13:
        print('age is greater than or equal to 13')
    case _:
        print('invalid')

# 模式匹配可以匹配list列表
args = ['gcc', 'Hello.c', 'world.c']
match args:
    case ['gcc']:
        print('gcc: missing source file(s).')
    case ['gcc', file1, *files]:
        print('gcc compile: ' + file1 + ', ' + ', '.join(files))
    case ['clean']:
        print('clean')
    case _:
        print('invalid')

print(ord('A'))

# 带有b的表示类型为bytes
print('ABC'.encode('ascii'))
# 如果中文用ascii编码进行转换的话会报错，因为中文的编码范围超过ascii的编码范围
print('中文'.encode('utf-8'))

# 判断key是否在字典中
d = {'Tom': 123, 'Jerry': 456}
print('Tom' in d)

# 使用get方法，设置若是没有获取到则返回设置的默认值
res = d.get('Toms', -1)
print(res)


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum += n
    return sum


# 若函数的参数为可变参数，需要传入list等列表时可以也加一个*
s=[1,2,3,4]
print(calc(*s))

# 关键字参数， 没有**的代表必须参数，带有**代表非必需
def person(name, age, **kw):
    print('name:', name,'age:', age,'kw:', kw)

person('Tom',31)

# 切片，快速获取指定范围的内容
arr=[1,2,3,4]
print(arr[0:2])

# 通过enumerate将list变成索引-元素对,同时迭代索引和元素本身
for i,value in enumerate(arr):
    print(i,value)
