import os

os.makedirs('./result/', exist_ok=True)


def scanner(path):

    files = os.listdir(path)
    #用该函数，读取path目录下的所有的文件夹和文件的文件名，将结果存入 files 中

    files =  files[1:]

    pathes = []
    #申明一个数组储存文件路径

    for file in files:
        pathes.append(path+file)
        #储存文件路径

    return pathes


filePath = './inverted'

pathes = scanner(filePath)



with open ('./result/index.txt','w') as f:
    for key,value in enumerate(pathes):
        f.write("{}\t{}\n".format(key,value))



index = 0
result = {}

for file in pathes:
    with open(file,'r') as f:
        #读文件,去除文件中的数字，引号，句号，方括号
        text = f.read().replace(",","").replace("[","").replace("]","")        .replace("\"","").replace(".","").replace("0","").replace("1","")        .replace("2","").replace("3","").replace("4","").replace("5","")        .replace("6","").replace("7","").replace("8","").replace("9","")

        #把每个文本变成数组
        text = text.split(" ")

        #把结果存入 result
        for word in text:

            #统一大小写
            word = word.lower()

            #如果单词已经存在与result中，向对应的 list 中添加一个索引
            if word  in list(result.keys()):
                result[word].append(index)

            #如果单词不存在的话，建立一个 word-list 的键值对
            else:
                result[word] = [index]
            #一个单词读写完毕

    #一个文本文件读写完毕,index加一，读下一个文件
    index += 1


#结果写入result.txt文件中
with open('./result/result.txt','w') as r:
    for word in result:
        r.write('{}\t{}\n'.format(word,result[word]))
