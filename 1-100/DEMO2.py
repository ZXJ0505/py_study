# 张晓静的绝作
# 时间：2022/3/1 21:20
# 转义字符
print('hello\nworld')  # \n 换行
print('hello\tworld')  # \t 空格
print('helloooo\tworld')  # \t=3个字符
print('hello\rworld')  # \r回车 会覆盖掉第一个
print('hello\bworld')  # \b 退一个格，将o退没了】

print('http:\\\\www.baidu.com')
print("老师说:\"大家好\"")

# 不希望字符串中的转义字符起作用，就在前面加上r或者R
print(r'hello\nworld')
# 注意事项，最后一个字符不能是\，可以是\\
# print(r'hello\nworld\')
# print(r'hello\nworld\')


name = '马丽亚'
print(name)
print('标识',id(name))
print('类型',type(name))
print('值',name)