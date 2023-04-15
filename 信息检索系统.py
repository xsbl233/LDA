import os
import glob
import jieba
import jieba.posseg as pseg
from gensim import models, similarities, corpora


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


def get_text(file_name):
    with open(file_name, "r", encoding='gb18030', errors='ignore') as file:
        ret = file.read()
    return ret


# 测试文本相似度计算
def semblance(text, corpus):
    # 对测试文本分词
    dic_text_list = seg_sentence(text)
    # print(dic_text_list)
    # 制作测试文本的词袋
    doc_text_vec = dictionary.doc2bow(dic_text_list)
    # print(doc_text_vec)

    # 获取语料库每个文档中每个词的tfidf值，即用tfidf模型训练语料库
    tfidf = models.TfidfModel(corpus)

    # 对稀疏向量建立索引
    index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=len(dictionary.keys()))
    sim = index[tfidf[doc_text_vec]]  # 相当于sim = index.get_similarities(tfidf[doc_text_vec])
    # print(sim)
    # print(len(sim))
    # 按照相似度来排序
    sim_sorted = sorted(enumerate(sim, 1), key=lambda x: -x[1])  # enumerate(x, 1) 代表从1开始设立索引
    # 相当于sorted(enumerate(sim), key=lambda x: x[1], reverse=True
    # print(sim_sorted[0])
    # print(sim_sorted[0:10])
    print(title[sim_sorted[0][0]])
    file_name_ans = title[sim_sorted[0][0]]
    print("查询:", text)
    print("得到文件", file_name_ans)
    print(get_text(file_name_ans))


# 读取所有文件
B_path = 'train'  # 文件夹路径
txt = []
title = []
for t in range(1, 27):
    folder_path = B_path + '/' + str(t)
    cnt = 0
    print(folder_path)
    for file_name in glob.glob(os.path.join(folder_path, "*.txt")):
        # 读取文件内容
        data = get_text(file_name)
        txt.append(data)
        file_name_tmp = folder_path + '/' + str(t) + ' (' + str(cnt) + ').txt'
        title.append(file_name_tmp)
        cnt = cnt + 1
# 读取停用词表
stopwords = Stop_Words_list('Chinese_from_dongxiexidian/stopwords.dat')

# 对目录下所有文本进行预处理
txt_list = []
for sentence in txt:
    txt_list.append(seg_sentence(sentence))
# print(txt_list)
# 制作词典
dictionary = corpora.Dictionary(txt_list)

# print(dictionary)  # 建立词袋模型,生成词向量
corpus = [dictionary.doc2bow(text) for text in txt_list]  # 语料库
# print(corpus)

text_file_name = 'test.txt'
pp = get_text(text_file_name)
# print(pp)
sp = pp.split('\n')
# print(sp)
for now in sp:
    semblance(now, corpus)
