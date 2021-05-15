# with open('text_file') as file: # Python会在当前程序文件所在目录查找并打开text_file文件
#     contents = file.read() # read()读取全部内容 并将其作为一个长字符串存储在变量中
#     print(contents)
'''
关键字with在不再需要访问文件后将其关闭
你只管打开文件，并在需要时使用它，Python自会在合适的时候将其关闭
'''

# file_name = 'text_file'
# lines = []
# with open(file_name) as file:
#     # for line in file: # 逐行读取
#     #     print(line.rstrip()) # 行尾有换行符，print函数也会加一个换行符，需要消除空白行

#     lines = file.readlines() # 创建一个包含文件各行内容的列表
# for line in lines:
#     print(line.rstrip())

# 读取文件时，Python将其中的所有文本都解读为字符串。

# filename = 'programming.txt'
# with open(filename, 'w') as file_object: 
#     file_object.write("I love programming.\n")
'''
文件打开模式
'w' 写入模式
'r' 读取模式 （默认值）
'a' 附加模式
'r+' 读写模式

如果要写入的文件不存在，Python将自动创建它。
以写入模式打开文件时要小心，因为如果指定的文件已经存在，Python将在返回文件对象前清空该文件。
Python只能将字符串写入文本文件，如果需要将数值数据写入，需要先转换为字符串。
write()不会在文本末尾添加换行符，如果需要可自己添加至字符串末尾。
'''

# with open(filename, 'a') as file_object:
#     file_object.write("I also love finding meaning in large datasets.")

# try:
#     print(5/0)
# except ZeroDivisionError: # except代码块
#     print("You can't divide by zero!")
# # 抛出异常后，Python将查找匹配的except代码块。

# try:
#     pass # 执行操作
# except:
#     pass # 异常逻辑
# else:
#     pass # 正常逻辑

# filename = '65331-0.txt'
# try:
#     with open(filename) as file_object:
#         contents = file_object.read()
# except FileNotFoundError:
#     print("File Not Found!")
# else:
#     words = contents.split() # split()会根据字符串创建一个单词列表，默认以空格为分隔符
#     print("The file " + filename + " has about " + str(len(words)) + " words.")


import json

# numbers = [2, 3, 5, 8, 13, 21]

filename = 'numbers.json'
# with open(filename, 'a') as f_obj:
#     json.dump(numbers, f_obj) # Serialize obj as a JSON formatted stream to file.

with open(filename) as f_obj:
    numbers = json.load(f_obj)
print(numbers)

