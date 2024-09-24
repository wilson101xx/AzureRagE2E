import os
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

def embedding_client():

    try:
        embedding_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT_EMBEDDING")
        embedding_key = os.getenv("AZURE_OPENAI_KEY_EMBEDDING")
        embedding_api_version = os.getenv("EMBEDDING_API_VERSION")    
    except KeyError as e:
        print(f"Missing key: {e}")

    embedding_client = AzureOpenAI(
        azure_endpoint=embedding_endpoint,
        api_key=embedding_key,
        api_version=embedding_api_version
    )
    return embedding_client

def embedding_data(data, embedding_client: AzureOpenAI):

    embedding_model = os.getenv("AI_SEARCH_EMBEDDING_MODEL")

    embedded_content_array = []

    for i in data:
        embedded_content = embedding_client.embeddings.create(
            input = i,
            model = embedding_model
        ).data[0].embedding
        embedded_content_array.append(embedded_content)
    return embedded_content_array

