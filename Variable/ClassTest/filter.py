mylist = [1, 2, 3, -10, -5, 3, -1]
import math
# list = (math.sqrt(n) for n in mylist if n > 0)  # 生成器表达式
list = [math.sqrt(n) for n in mylist if n > 0]   # 列表推导
print(list)
python

