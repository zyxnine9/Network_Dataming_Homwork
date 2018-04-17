
# coding: utf-8

# In[1]:


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

# In[2]:

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
        
        files = self.__doc_index2path.values()
        for file in files:
            with open(file,'r') as f:
                self.__docs.append(f.read())
                
                
    def search_rank(self, query):
        tfidf = TfidfVectorizer(min_df=0, max_df=1.)
        docs = tfidf.fit_transform(self.__docs)
        query = tfidf.transform([query.lower()])
        cosine = cosine_similarity(query, docs)
        result = cosine.argsort().tolist()[0]
        result.reverse()
        print("The search rank is {}".format(result))
        self.__print_result(result)
        
        
    def __print_result(self, result):
        for doc_index in result:
            doc_path = self.__doc_index2path[str(doc_index)]
            with open(doc_path, 'r') as f:
                print("The file index is {} \n path is {}".format(doc_index, doc_path))
                print(f.read())
                print("===========================这是分割线======================")
                print()


# In[3]:


a = Vector_search()


# In[4]:


a.search_rank('sports news')

