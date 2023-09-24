# Smart Study

This repository is part of the competition HackMty, where the goal is to create a project to make an efficient and quick generstive AI result, being a search engine.

![HackMty](https://aistudio.blob.core.windows.net/random/AzureOpenAIKeys.png?sp=r&st=2023-09-23T21:32:41Z&se=2023-09-27T05:32:41Z&spr=https&sv=2022-11-02&sr=b&sig=LYMJH13tFL%2BKxf2Ku7pcrgvGAr4lPqFJ5xnwo8WqbxY%3D](https://www.google.com/url?sa=i&url=https%3A%2F%2Fhackmty.com%2F&psig=AOvVaw0cWkGM-bd5kr1G9qSvkjAT&ust=1695597390427000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCLiB-9LuwYEDFQAAAAAdAAAAABAE)https://www.google.com/url?sa=i&url=https%3A%2F%2Fhackmty.com%2F&psig=AOvVaw0cWkGM-bd5kr1G9qSvkjAT&ust=1695597390427000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCLiB-9LuwYEDFQAAAAAdAAAAABAE)

![MLH](https://aistudio.blob.core.windows.net/random/AzureOpenAIKeys.png?sp=r&st=2023-09-23T21:32:41Z&se=2023-09-27T05:32:41Z&spr=https&sv=2022-11-02&sr=b&sig=LYMJH13tFL%2BKxf2Ku7pcrgvGAr4lPqFJ5xnwo8WqbxY%3D](https://www.google.com/url?sa=i&url=https%3A%2F%2Fhackmty.com%2F&psig=AOvVaw0cWkGM-bd5kr1G9qSvkjAT&ust=1695597390427000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCLiB-9LuwYEDFQAAAAAdAAAAABAE)https://www.google.com/url?sa=i&url=https%3A%2F%2Fhackmty.com%2F&psig=AOvVaw0cWkGM-bd5kr1G9qSvkjAT&ust=1695597390427000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCLiB-9LuwYEDFQAAAAAdAAAAABAE](https://www.google.com/url?sa=i&url=https%3A%2F%2Fmlh.io%2F&psig=AOvVaw1bO1aKY3vk758MyfmWfqGX&ust=1695597488397000&source=images&cd=vfe&opi=89978449&ved=0CBAQjRxqFwoTCJi5zoHvwYEDFQAAAAAdAAAAABAE)https://www.google.com/url?sa=i&url=https%3A%2F%2Fmlh.io%2F&psig=AOvVaw1bO1aKY3vk758MyfmWfqGX&ust=1695597488397000&source=images&cd=vfe&opi=89978449&ved=0CBAQjRxqFwoTCJi5zoHvwYEDFQAAAAAdAAAAABAE)

This project is done to resolve the issue of searching for an scientific paper, articule or report into a big pile with large amounts of documents. Where we only want to obtain information in a certain report that we are looking for.
To save up time and energy, this projects has as input one or several article files and a prompt for what is being looked for. Giving as an output the required file and section where the request is obtained from.

## Previous configurations

### Installing the libraries

The script works with the following versions:
- python `3.11.5`
- tensorflow `2.13.0`
- python-dotenv `1.0.0`

To install the necessary libraries, run the following code in a Python executer
``` CMD Commands
pip install python-dotenv
```

To view the version of your libraries, run the following:
``` CMD Commands
pip show python-dotenv
```

### FRIDA & Pinecone.io

This project uses the FRIDA SDK by Softek and Pinecone.io as a Long-Term Memory method for AI. To obtain the necessary information, do the following:

#### FRIDA

Execute in your Python instance:
``` CMD Commands
pip install git+https://github.com/Fridaplatform/SofttekLLMSDK.git
```
For more information please consult the offical repo https://github.com/Fridaplatform/SofttekLLMSDK

#### Pinecone.io

Create a Pinecone.io account if necessary and create an Index and API Key, these will be used in the env variables further on.

### Environmental variables

The `.env` file needs to have the following environmental variables for the script to work properly:
- `OPENAI_API_KEY`: API Key you use for OpenAI access
- `OPENAI_API_BASE`: Base page for the API
- `OPENAI_CHAT_MODEL_NAME`: GPT model instance being used
- `OPENAI_EMBEDDINGS_MODEL_NAME`: Model name for OpenAI embeddings
- `PINECONE_API_KEY`: Generated Pinecone API Key
- `PINECONE_ENVIRONMENT`: Provided Environment for Pinecone, generated with Index
- `PINECONE_INDEX_NAME`: Generated Index name for Pinecone
