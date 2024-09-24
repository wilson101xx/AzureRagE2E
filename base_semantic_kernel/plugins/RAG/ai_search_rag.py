from __future__ import annotations
import os
import requests
import json
from openai import AzureOpenAI
from semantic_kernel.functions.kernel_function_decorator import kernel_function
from dotenv import load_dotenv

load_dotenv()


class AIandDataRAG:
    """This Plugin is used to have a conversation with GPT along with using data from Azure Search so using RAG
    Methods: ChatWithAIandDataRAG(usermessage: str): Accepts the message from the user and returns the response from GPT-4 model"""

    @kernel_function(
        description="This model is used to facilitate conversations with GPT, retrieving data from Azure AI Search, about product parts. This approach is known as Retrieval-Augmented Generation (RAG).",
        name="ChatWithAIandDataRAG"
    )


    def ChatWithAIandDataRAG(self, message:str):

        print("We are in function call")

        endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
        endpoint_key = os.getenv("AZURE_OPENAI_KEY")
        deployment = os.getenv("AZURE_OPENAI_4O")
        search_endpoint = os.getenv("AI_SEARCH_ENDPOINT")
        search_key = os.getenv("AI_SEARCH_KEY")
        embedding_model = os.getenv("AI_SEARCH_EMBEDDING_MODEL")
        index = os.getenv("BASE_NAME")

        index = index + "-index-vector"

        client = AzureOpenAI(
            azure_endpoint=endpoint,
            api_key=endpoint_key,
            api_version="2024-05-01-preview",
        )


        completion = client.chat.completions.create(
            model=deployment,
            messages= [
            {
                "role": "system",
                "content": """You are a helpful ai chatbot that does a rag search and provides infomation"""
            },
            {
                "role": "user",
                "content": message
            }
        ],
            max_tokens=800,
            temperature=0,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None,
            stream=False
        ,
            extra_body={
            "data_sources": [{
                "type": "azure_search",
                "parameters": {
                    "endpoint": f"{search_endpoint}",
                    "index_name": f"{index}",
                    "semantic_configuration": "my-semantic-config",
                    "query_type": "vector_semantic_hybrid",
                    "fields_mapping": {
                    "content_fields_separator": "\n",
                    "content_fields": [
                        "content"
                    ],
                    "filepath_field": None,
                    "title_field": None,
                    "url_field": None,
                    "vector_fields": [
                        "Content_vector"
                    ]
                    },
                    "in_scope": True,
                    "role_information": "You are an AI assistant that helps people find information.",
                    "filter": None,
                    "strictness": 3,
                    "top_n_documents": 5,
                    "authentication": {
                    "type": "api_key",
                    "key": f"{search_key}"
                    },
                    "embedding_dependency": {
                    "type": "deployment_name",
                    "deployment_name": f"{embedding_model}"
                    }
                }
                }]
            })

        answer = completion.choices[0].message.content
        # print(type(answer))
        return answer

if __name__ == "__main__":
    ai = AIandDataRAG()
    message = "What is new in azure"
    response = ai.ChatWithAIandDataRAG(message)
    print(response)