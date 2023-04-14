import os
import glob
import jieba

# 读取所有文件
B_path = 'train'  # 文件夹路径
txt = []
for t in range(1,27):
    folder_path = B_path + '/' + str(t)
    cnt = 0
    print(folder_path)
    for file_name in glob.glob(os.path.join(folder_path, "*.txt")):
        cnt = cnt + 1
        # 读取文件内容
        with open(file_name, "r", encoding='gb18030', errors='ignore') as file:
            data = file.read()
            txt.append(data)

stopwords = []
fstop = open('stop')
