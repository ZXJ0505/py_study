# 张晓静的绝作
# 时间：2022/3/4 16:08
s='hello,python'
print('-----isidentifier判断指定的字符串是不是合法的标识符-----')
print('1.',s.isidentifier())          #False
print('2.','hello'.isidentifier())    #True
print('3.','张三_'.isidentifier())     #True
print('4.','张三_123'.isidentifier())  #True

print('-----isspace判定指定的字符串是否全部由空白字符组成（回车、换行、水平制表符）-----')
print('5.','\t'.isspace())  #True

print('-----isalpha判断指定的字符串是否全部由字母组成-----')
print('6.','abc'.isalpha())   #True
print('7.','张三'.isalpha())   #True
print('8.','张三_1'.isalpha()) #False

print('-----isdecimal判断指定的字符串是否由十进制组成-----')
print('9.','123'.isdecimal())  #True
print('10.','123四'.isdecimal()) #False
print('11.','ⅡⅢⅣ'.isdecimal()) #False

print('-----isnumeric判断指定的字符串是否全部由数字组成-----')
print('12.','123'.isnumeric())   #True
print('13.','123四'.isnumeric()) #True
print('14.','ⅡⅢⅣ'.isnumeric()) #True

print('-----isalnum判断指定的字符串是否全部由字母和数字组成-----')
print('15.','abc1'.isalnum())   #True
print('16.','张三123'.isalnum()) #True
print('17.','abc!'.isalnum())   #False