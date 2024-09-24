# AzureRagE2E: End-to-End Retrieval-Augmented Generation (RAG) with Azure

This repository demonstrates an end-to-end Retrieval-Augmented Generation (RAG) solution using Azure services, including Azure Cognitive Search, Azure OpenAI, and Document Intelligence. The solution extracts data from documents, processes them using embeddings, and updates a vector database for enhanced AI-powered search capabilities.

## Features

- **Document Intelligence**: Extracts structured data from documents using Azure's Document Intelligence service.
- **Data Embeddings**: Converts text data into high-dimensional vector embeddings using Azure OpenAI for efficient AI search.
- **Vector Search**: Leverages Azure Cognitive Search with vector capabilities for fast and accurate information retrieval.
- **RAG with Azure**: Combines retrieval-augmented generation with Azure OpenAI to provide AI-driven responses.

## Requirments needed

- **Azure AI Search**: This is where your vector database will be
- **OpenAI**:  Deployment of AI model
- **Document Intelligence (Optional)**


## Environment Variables

### Base

| Variable Name | Description                                      |
|---------------|--------------------------------------------------|
| `BASE_NAME`   | The name of the vector database you want to make |

### Database Environments

| Variable Name        | Description                     |
|----------------------|---------------------------------|
| `AI_SEARCH_ENDPOINT` | The Azure AI Search endpoint    |
| `AI_SEARCH_KEY`      | The Azure AI Search resource key|

### Embedding Model Endpoints

| Variable Name                    | Description                                                                                                 |
|----------------------------------|-------------------------------------------------------------------------------------------------------------|
| `AZURE_OPENAI_ENDPOINT_EMBEDDING` | Azure OpenAI endpoint where your embedding model is located                                                 |
| `AI_SEARCH_EMBEDDING_MODEL`      | The name of your embedding model. For example, dimensions are 1536, so I recommend `text-embedding-ada-002`   |
| `AZURE_OPENAI_KEY_EMBEDDING`     | Azure OpenAI key                                                                                             |
| `EMBEDDING_API_VERSION`          | Embedding API version (e.g., `"2023-05-15"`)                                                                |

### Document Intelligence

| Variable Name      | Description          |
|--------------------|----------------------|
| `DOC_INTEL_ENDPOINT` | Doc Intel endpoint  |
| `DOC_INTEL_KEY`      | Doc Intel Key       |
| `DOC_INTEL_MODEL`    | Doc Intel Model     |

### Azure AI

| Variable Name           | Description                             |
|-------------------------|-----------------------------------------|
| `AZURE_OPENAI_4O`       | Azure OpenAI 4o model deployment name    |
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI endpoint                    |
| `AZURE_OPENAI_KEY`      | Azure OpenAI Key                         |
