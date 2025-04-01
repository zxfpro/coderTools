
import os
from pinecone import Pinecone
from pinecone import ServerlessSpec
from llama_index.vector_stores.pinecone import PineconeVectorStore
from llama_index.core import VectorStoreIndex, StorageContext
from reader import read_github_repo,read_github_issue


def get_storage_context(index="api-documents-index",space="pydantic"):
    pc = Pinecone(api_key=os.environ.get("pinecone_key"))
    vector_store = PineconeVectorStore(pinecone_index=pc.Index(index),namespace = space)
    return StorageContext.from_defaults(vector_store=vector_store)

def get_nodes_from_documents():
    return nodes

def get_index(nodes,storage_context):
    index = VectorStoreIndex(nodes, storage_context=storage_context)




def main(select = 1):
    if select == 1:#存储
        documents1 = read_github_repo(owner="pydantic",repo="pydantic")
        documents2 = read_github_issue(owner="pydantic",repo="pydantic")

        storage_context = get_storage_context(index="api-documents-index",space="pydantic")
        
        retriever = index.as_retriever(filters=filters)
        retriever.retrieve("What is inception about?")
        '''
        from llama_index.core.vector_stores import (
            MetadataFilter,
            MetadataFilters,
            FilterOperator,
        )

        filters = MetadataFilters(
            filters=[
                MetadataFilter(
                    key="theme", operator=FilterOperator.EQ, value="Fiction"
                ),
            ]
        )
        '''
    elif select == 2:# 读取
        pass

    else:
        print('error')


if __name__ == "__main__":
    main()