#!/usr/bin/env python
# coding: utf-8

# In[6]:


import os
os.environ["GOOGLE_API_KEY"] = "your_api_key_here"


# In[11]:


pip install langchain-openai


# In[16]:


pip install langchain-openai


# In[22]:


import os
import openai

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
openai.api_key = os.environ['OPENAI_API_KEY']


from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser

prompt = ChatPromptTemplate.from_template(
   "Tell me about {topic} in the style of {style}"
)
model = ChatOpenAI()
output_parser = StrOutputParser()
model = ChatOpenAI()
output_parser = StrOutputParser()

chain = prompt | model | output_parser

chain.invoke({ "topic": "the moon",
    "style": "a short poem"})


# In[ ]:




