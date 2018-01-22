from elasticsearch import Elasticsearch
'''
Created on 2018年1月22日

@author: niushuai
'''

if __name__ == '__main__':
    ''' ES操作测试 '''
    es = Elasticsearch()
    # 创建索引，索引的名字是my-index,如果已经存在了，就返回个400，
    # 这个索引可以现在创建，也可以在后面插入数据的时候再临时创建
    print(es.indices.create(index='my-index', body="插入数据的内容"))
