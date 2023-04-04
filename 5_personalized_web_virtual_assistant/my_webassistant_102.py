# Code adapted from https://github.com/AIAdvantage/chatgpt-api-youtube
# To see how to create a virtual environment, check https://python.land/virtual-environments/virtualenv 
# python -m venv my-envi, and the next steps, see https://stackoverflow.com/a/74825209
# For error of installation due to privileges, see https://stackoverflow.com/questions/66322049/could-not-install-packages-due-to-an-oserror-winerror-2-no-such-file-or-direc
# For gitignore, see https://github.com/github/gitignore/blob/main/Python.gitignore
# If VS Code shows issues about execution policies, you may need to change the execution policies settings in the powershell, see https://www.sharepointdiary.com/2014/03/fix-for-powershell-script-cannot-be-loaded-because-running-scripts-is-disabled-on-this-system.html


import os
import my_api_keys
import openai # open ai documentation at https://platform.openai.com/docs/introduction/overview
#import gradio

from llama_index import (
    GPTKeywordTableIndex,
    SimpleDirectoryReader,
    LLMPredictor,
    ServiceContext, 
    download_loader, 
    PromptHelper
)

# documentation of langchain at https://github.com/hwchase17/langchain
from langchain import OpenAI

os.environ['OPENAI_API_KEY'] = my_api_keys.my_open_ai_key


## Working with llama_index = playing around with data augmentation

# Step 1: load the new data
# documentation of llama_index at https://gpt-index.readthedocs.io/en/latest/
# data loaders at https://llamahub.ai/
#from llama_index import download_loader, GPTSimpleVectorIndex

SimpleDirectoryReader = download_loader("SimpleDirectoryReader")
# Take all the files in the data folder, see https://llamahub.ai/l/file
loader = SimpleDirectoryReader('data', recursive=True, exclude_hidden=True)
documents = loader.load_data()

# Step 2: Build a CUSTOM llm index: code adapted from https://github.com/wombyz/custom-knowledge-chatbot/tree/main/custom-knowledge-chatbot
# Official documentation: https://gpt-index.readthedocs.io/en/latest/how_to/customization/custom_llms.html

# define prompt helper
# set maximum input size
max_input_size = 2048
# set number of output tokens
num_output = 256
# set maximum chunk overlap
max_chunk_overlap = 20
prompt_helper = PromptHelper(max_input_size, num_output, max_chunk_overlap)


# define LLM
llm_predictor = LLMPredictor(llm=OpenAI(temperature=0, model_name="text-davinci-002"))
service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor, prompt_helper=prompt_helper)

# build index
custom_index = GPTKeywordTableIndex.from_documents(documents, service_context=service_context)

#Step 3: reuse the custom index to get some answers

# get response from query
response = custom_index.query("What did the author do after his time at Y Combinator?")
print(response)

'''
SimpleDirectoryReader = download_loader("SimpleDirectoryReader")
# Take all the files in the data folder, see https://llamahub.ai/l/file
loader = SimpleDirectoryReader('data', recursive=True, exclude_hidden=True)
documents = loader.load_data()


# Step 2: Build a CUSTOM llm index: code from https://github.com/wombyz/custom-knowledge-chatbot/tree/main/custom-knowledge-chatbot
from llama_index import LLMPredictor, GPTSimpleVectorIndex, PromptHelper
from langchain.llms import OpenAI

# define LLM
llm_predictor = LLMPredictor(llm=OpenAI(temperature=0.1, model_name="text-davinci-002")) # alternative model: gpt-3.5-turbo	

# define prompt helper
# set maximum input size
max_input_size = 4096
# set number of output tokens
num_output = 256
# set maximum chunk overlap
max_chunk_overlap = 20

prompt_helper = PromptHelper(max_input_size, num_output, max_chunk_overlap)

custom_LLM_index = GPTSimpleVectorIndex.from_documents(
    documents, llm_predictor=llm_predictor, prompt_helper=prompt_helper
)

index = GPTKeywordTableIndex.from_documents(documents, service_context=service_context)

#Step 3: reuse the custom index to get some answers
response = custom_LLM_index.query("What do you think of Facebook's LLaMa?")
print(response)

'''

'''
messages = [{"role": "system", "content": "You are an assistant that specializes in geographic question answering"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Digital Geo Question Answering")

demo.launch(share=True) # you may need to customize your firewall settings for this to work 
#demo.launch()
'''