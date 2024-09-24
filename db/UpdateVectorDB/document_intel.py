import os
import re
import logging
from dotenv import load_dotenv
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
from typing import Optional


# Load environment variables
load_dotenv()
logging.basicConfig(level=logging.INFO)

MODEL_ID = "prebuilt-layout"

def create_client():
    try:
        endpoint =os.getenv("DOC_INTEL_ENDPOINT")
        key = os.getenv("DOC_INTEL_KEY")
    except KeyError as e:
        print(f"Missing key: {e}")
    try:
        return DocumentAnalysisClient(endpoint, AzureKeyCredential(key))
    except Exception as e:
        logging.error(f"Failed to create DocumentAnalysisClient: {e}")
        raise


def extract_page_text(page) -> str:
    content = ''
    try:
        content = '\n'.join([line.content for line in page.lines])
    except Exception as e:
        logging.error(f"Error extracting text from page: {e}")
    return content


def normalize_text(s, sep_token=" \n "):
    s = re.sub(r'\s+', ' ', s).strip()  # Replace multiple spaces with a single space
    s = re.sub(r". ,", "", s)  # Remove incorrect space before commas
    s = s.replace("..", ".")
    s = s.replace(". .", ".")
    s = s.strip()
    return s


def analyze_document(client: DocumentAnalysisClient, doc_intel_model: str, file_path: str) -> None:
    normalized_content_array = []
    try:
        with open(file_path, "rb") as document:
            poller = client.begin_analyze_document(model_id=doc_intel_model, document=document)
            result = poller.result()
            
            for page_num, page in enumerate(result.pages, start=1):
                content = extract_page_text(page)
                normalized_content = normalize_text(content)
                normalized_content_array.append(normalized_content)
                # logging.info(f"Page {page_num} content:\n{normalized_content}\n")
            return normalized_content_array
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
    except Exception as e:
        logging.error(f"Error analyzing document: {e}")



if __name__ == "__main__":

    client = create_client()

    file_path = "documents/Azure_whats_new.pdf"
    
    normalized_content_array = analyze_document(client, MODEL_ID, file_path)
