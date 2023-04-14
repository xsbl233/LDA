import os
import glob
import jieba
import jieba.posseg as pseg


# 读入停用词
def Stop_Words_list(filepath):
    stopwords = [line.strip()
                 for line in open(filepath, 'r', encoding='gb18030', errors='ignore').readlines()]
    return stopwords


# 对句子进行分词
def seg_sentence(sentence):
    sentence_seged = pseg.cut(sentence.strip())
    outstr = []
    stop_flag = ['x', 'c', 'u', 'd', 'p', 't', 'uj', 'm', 'f', 'r']
    for word, flag in sentence_seged:
        if flag not in stop_flag and word not in stopwords:
            if word != '\t':
                outstr.append(word)
    return outstr


# 读取所有文件
B_path = 'train'  # 文件夹路径
txt = []
title = []
for t in range(1, 27):
    folder_path = B_path + '/' + str(t)
    cnt = 0
    print(folder_path)
    for file_name in glob.glob(os.path.join(folder_path, "*.txt")):
        cnt = cnt + 1
        # 读取文件内容
        with open(file_name, "r", encoding='gb18030', errors='ignore') as file:
            data = file.read()
            txt.append(data)
            title.append(file_name)
print(title)
# 读取停用词表
stopwords = Stop_Words_list('Chinese_from_dongxiexidian/stopwords.dat')

# 对目录下所有文本进行预处理，构建字典
corpus = []
for sentence in txt:
    corpus.append(seg_sentence(sentence))
print(corpus)

