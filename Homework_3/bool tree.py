
# coding: utf-8

# In[1]:


class Bool_search(object):
    __doc_path = '../data/'
    __doc_index_path = '../result/index.txt'
    __word_index_path = '../result/result.txt'
    __doc_index2path = {}
    __word2index = {}
    
    def __init__(self):
        with open(self.__word_index_path) as f:
            line = f.readline()
            while(len(line) is not 0):
                infos = line.split('\t')
                indexs = infos[1].replace(",","").replace("[","").replace("]","").replace("\n","")
                self.__word2index[infos[0]] = indexs.split(" ")
                line = f.readline()
                
        with open(self.__doc_index_path) as f:
            line = f.readline()
            while(len(line) is not 0):
                infos = line.split('\t')
                self.__doc_index2path[infos[0]] = infos[1]
                line = f.readline()
            
    def search_single_keyword(self, keyword):
        return_list = []
        if keyword in self.__word2index.keys():
            return_list = list(set(self.__word2index[keyword]))
        return return_list
    
    
    def __construct_query_tree(self, query):
        elements = str(query).lower().split(" ")
        temp_node_list = []
        i = 0
        
        while(i < len(elements)):
            element = elements[i].replace(" ","")
            node = []
            if str(element) == 'and':
                node.append("AND")
                    
                #left node
                left_node = (temp_node_list.pop())
                node.append(left_node)
                
                #right node 
                i += 1
                right_node = []
                right_node.append(elements[i].replace(" ",""))
                right_node.append(None)
                right_node.append(None)
                node.append(right_node)
                
                
            else:
                node.append(element)
                node.append(None)
                node.append(None)
            
            i += 1
            
            temp_node_list.append(node)
        i = 0
        last_node = temp_node_list[i]
        i += 1
        while(i < len(temp_node_list)):
            current_node = temp_node_list[i]
            or_node = []
            or_node.append("OR")
            or_node.append(last_node)
            or_node.append(current_node)
            last_node = or_node
            i += 1
        return last_node
            
        
    def __search_with_binary_tree(self, root_node):
        result2return_list = []
        node_value = root_node[0]
        if node_value is "AND":
            left_child_result = self.__search_with_binary_tree(root_node[1])
            right_child_result = self.__search_with_binary_tree(root_node[2])
            
            for node in left_child_result:
                if node in right_child_result:
                    result2return_list.append(node)
                    
        elif node_value is "OR":
            left_child_result = self.__search_with_binary_tree(root_node[1])
            right_child_result = self.__search_with_binary_tree(root_node[2])
            
            for node in left_child_result:
                if node  not in result2return_list:
                    result2return_list.append(node)
                    
            for node in right_child_result:
                if node  not in result2return_list:
                    result2return_list.append(node)
                    
        else:
            return self.search_single_keyword(node_value)
        
        return result2return_list
    
    def query_result(self,query):
        query = query.lower()
        query = self.__construct_query_tree(query)
        query_result = self.__search_with_binary_tree(query)
        for doc in query_result:
            path = self.__doc_index2path[doc].replace("\n","")
            print("document is {}".format(doc))
            print("document's paht is {}".format(path))
            with open(path) as f:
                content = f.read()
                print(content)
            print("-------------------------------------------")
            
        


# In[2]:


test = Bool_search()


# In[3]:


test.query_result('exercise criteria and entertainment')

