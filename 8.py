#注释前打井号
#len函数只用于 求字符串长度
#在字符串中，空格和标点符号也算字符数
s = "汪苏泷大帅哥"
print(len(s))
#通过索引获取字符串中单个字符
print(s[2])#计算机从0开始计算，因此字符串中第三个字是2所在位置
print(s[0])
print(s[len(s)-2])#字符串长度6，减2为4所以输出第五个字帅

#定义布尔类型的变量
a1 = True
a2 = False

#定义空值类型
b1 = None #首字母要大写同布尔类型

#用type函数输出变量类型
print(type(a1))
print(type(b1))
print(type(s))