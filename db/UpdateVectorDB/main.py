import document_intel
import embedding_data
import update_vector_db
import os
from dotenv import load_dotenv

load_dotenv()
# This script processes input data either as a document or text:
# - Stage 1: If a document is passed, it will use document intelligence to extract relevant data.
#   If only text is passed, it will bypass document intelligence and directly process the text.
# - Stage 2: Using the extracted data (from document or text), the script will generate embeddings
#   through the embedding model, which captures the meaning of the content for AI vector search.
# - Finally, the data and embeddings will be structured into a JSON format, which is then used
#   to update an AI search vector database for enhanced search and retrieval capabilities.


NEED_DOC_INTEL = True
document_path = "documents/Azure_whats_new.pdf"

def run_doc_intel(document_path):
    
    doc_intel_model = os.getenv("DOC_INTEL_MODEL")

    doc_intel_client = document_intel.create_client()
    normalized_content_array = document_intel.analyze_document(doc_intel_client, doc_intel_model, document_path)
    return normalized_content_array

def run_embedding_model(normalized_content_array):
    embedding_client = embedding_data.embedding_client()
    embedding_content_array = embedding_data.embedding_data(normalized_content_array, embedding_client)
    return embedding_content_array


def update_vector_with_content(data, embeddings):
    search_client = update_vector_db.vector_db_client()
    formatted_data = update_vector_db.format_data(data, embeddings)
    result = update_vector_db.upload_document(formatted_data, search_client)
    # print("Vector database updated with content and embeddings.")

def main():
    if NEED_DOC_INTEL == True:
        document_path = "documents/Azure_whats_new.pdf"
        normalized_content_array = run_doc_intel(document_path)
        embedding_content_array = run_embedding_model(normalized_content_array)
        update_vector_with_content(normalized_content_array, embedding_content_array)
        # update_vector_with_content(None,None)
main()