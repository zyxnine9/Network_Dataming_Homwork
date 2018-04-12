# Vector Space Model

In this week, we need to transform the documents and query to vector.<br>

The same time, we  use tf-idf  to represent the weight in the vector.<br>

 This week, I don't follow the Mr.Wei's algorithm, I just use some python package.<br>

## Moduals

this week, I use  ***scikit-learn***  to  calculate the _TF-IDF_ and the _cosine_<br>

I'm not very sure what happen in those package, so I don't want to talk about them in details.<br>

Whereas, let me just explain something in the program. 

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os
```

## My Code 


```python
class Vector_search(object):
    __docs_path = '../data/'
    __doc_index_path = '../result/index.txt'
    __doc_index2path = {}
    __docs = []

    def __init__(self):
        with open(self.__doc_index_path) as f:
            line = f.readline()
            while(len(line) is not 0):
                infos = line.split('\t')
                self.__doc_index2path[infos[0]] = infos[1].replace('\n','')
                line = f.readline()
        #初始化 index2path
        
        files = self.__doc_index2path.values()
        for file in files:
            with open(file,'r') as f:
                self.__docs.append(f.read())
        #把文件读入__docs中
        
        
    def search_rank(self, query):
        tfidf = TfidfVectorizer(min_df=0, max_df=1.)
        
        docs = tfidf.fit_transform(self.__docs)
        #用那6个.txt文件构建由tf-idf赋予权重的向量
        
        query = tfidf.transform([query.lower()])
        #将查询也转化成tf-idf相关的向量
        
        cosine = cosine_similarity(query, docs)
        #求余弦
        
        result = cosine.argsort().tolist()[0]
        result.reverse()
        #结果排序后，cos值由大到小，然后转化成list
        
        print("The search rank is {}".format(result))
        self.__print_result(result)
        
    def __print_result(self, result):
        for doc_index in result:
            doc_path = self.__doc_index2path[str(doc_index)]
            with open(doc_path, 'r') as f:
                print("The file index is {} \n path is {}".format(doc_index, doc_path))
                print(f.read())
                print("=======================================================================")
                print()
```


```python
a = Vector_search()
```


```python
a.search_rank('sports news')
```

    The search rank is [3, 5, 4, 2, 1, 0]
    The file index is 3 
     path is ../data/sports3.txt
    Records are kept and updated for most sports at the highest levels, while failures and accomplishments are widely announced in sport news. Sports are most often played just for fun or for the simple fact that people need exercise to stay in good physical condition. However, professional sport is a major source of entertainment.
    =======================================================================
    
    The file index is 5 
     path is ../data/sports1.txt
    A sport is an organized, competitive, entertaining, and skillful activity requiring commitment, strategy, and fair play, in which a winner can be defined by objective means. It is governed by a set of rules or customs. Activities such as card games and board games, are classified as "mind sports" and some are recognized as Olympic sports[citation needed], requiring primarily mental skills and mental physical involvement. Non-competitive activities, for example as jogging or playing catch are usually classified as forms of recreation.
    =======================================================================
    
    The file index is 4 
     path is ../data/sports2.txt
    Physical events such as scoring goals or crossing a line first often define the result of a sport. However, the degree of skill and performance in some sports such as diving, dressage and figure skating is judged according to well-defined criteria. This is in contrast with other judged activities such as beauty pageants and body building, where skill does not have to be shown and the criteria are not as well defined.
    =======================================================================
    
    The file index is 2 
     path is ../data/math2.txt
    Through the use of abstraction and logical reasoning, mathematics evolved from counting, calculation, measurement, and the systematic study of the shapes and motions of physical objects. Practical mathematics has been a human activity for as far back as written records exist. Rigorous arguments first appeared in Greek mathematics, most notably in Euclid's Elements. Mathematics continued to develop, for example in China in 300 BC, in India in AD 100, and in the Muslim world in AD 800, until the Renaissance, when mathematical innovations interacting with new scientific discoveries led to a rapid increase in the rate of mathematical discovery that continues to the present day.[5]
    =======================================================================
    
    The file index is 1 
     path is ../data/math3.txt
    There is debate over whether mathematical objects such as numbers and points exist naturally or are human creations. The mathematician Benjamin Peirce called mathematics "the science that draws necessary conclusions".[6] Albert Einstein, on the other hand, stated that "as far as the laws of mathematics refer to reality, they are not certain; and as far as they are certain, they do not refer to reality."[7]
    =======================================================================
    
    The file index is 0 
     path is ../data/math1.txt
    Mathematics is the study of quantity, structure, space, and change. Mathematicians seek out patterns,[2][3] formulate new conjectures, and establish truth by rigorous deduction from appropriately chosen axioms and definitions.[4]
    =======================================================================
    
