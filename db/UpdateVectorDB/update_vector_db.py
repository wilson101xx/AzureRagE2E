import os
import json
import uuid
from dotenv import load_dotenv
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential

load_dotenv()


def vector_db_client() -> SearchClient:
    try:
        azure_ai_search_endpoint = os.getenv("AI_SEARCH_ENDPOINT")
        azure_ai_search_key = os.getenv("AI_SEARCH_KEY")
        azure_ai_search_index = os.getenv("BASE_NAME")
        azure_ai_search_index = azure_ai_search_index + "-index-vector"
    except KeyError as e:
        print(f"Missing key: {e}")

    search_client = SearchClient(endpoint=azure_ai_search_endpoint,
                                index_name=azure_ai_search_index,
                                credential=AzureKeyCredential(azure_ai_search_key))
    return search_client

def format_data(data, embeddings) -> list:
    

    formatted_data = []
    for i in range(len(data)):
        formatted_data.append({
            "id": str(uuid.uuid4()),
            "content": data[i],
            "Content_vector": embeddings[i]
        })
    return formatted_data


def upload_document(formatted_data_array: list,search_client: SearchClient):
    for i in formatted_data_array:
        result = search_client.upload_documents(documents=[i])
    
    return result