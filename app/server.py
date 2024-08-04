from fastapi import FastAPI
import uvicorn
# from langchain_core.messages import AIMessage
# from langchain.prompts import ChatPromptTemplate
# from langchain.chat_models import ChatAnthropic, ChatOpenAI
from langchain_ollama import ChatOllama
# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langserve import add_routes
from fastapi.middleware.cors import CORSMiddleware
# from dotenv import dotenv_values

# pip install --trusted-host=pypi.org --trusted-host=files.pythonhosted.org --user pip-system-certs

app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple api server using Langchain's Runnable interfaces",
)

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

# Get Environment Variables
# processenv = dotenv_values('.env')
# HUGGINGFACEHUB_API_TOKEN = processenv['HUGGINGFACEHUB_API_TOKEN']

# model = HuggingFaceEndpoint(
#     huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN,
#     repo_id="mistralai/Mistral-7B-Instruct-v0.2",
#     task="text-generation",
#     max_new_tokens=1024,
#     # temperature=0.5,
#     do_sample=False,
#     # repetition_penalty=1.03,
# )

# model = ChatHuggingFace(llm=llm)

model = ChatOllama(
    model="llama3.1", # or whatever model you want to use
    temperature=0,
)

# messages = [
#     (
#         "system",
#         "You are a helpful assistant that translates English to French. Translate the user sentence.",
#     ),
#     ("human", "I love programming."),
# ]
# ai_msg = model.invoke(messages)
# print(ai_msg)

# prompt = ChatPromptTemplate(
#     [
#         (
#             "system",
#             "You are a helpful young lady assistant.",
#         ),
#         ("human", "{input}"),
#     ]
# )

# chain = prompt | model

# llm_chain = prompt | model

# Add routes
# add_routes(
#     app,
#     ChatOpenAI(model="gpt-3.5-turbo-0125"),
#     path="/openai",
# )

# add_routes(
#     app,
#     ChatAnthropic(model="claude-3-haiku-20240307"),
#     path="/anthropic",
# )

add_routes(
    app,
    model,
    path="/ollama",
)

# model = ChatAnthropic(model="claude-3-haiku-20240307")
# prompt = ChatPromptTemplate.from_template("tell me a joke about {topic}")
# add_routes(
#     app,
#     prompt | model,
#     path="/joke",
# )

if __name__ == "__main__":
    # uvicorn.run(app, host="127.0.0.1", port=8000)
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True) # for Development
    # For LangServe Playground, enter
    # http://127.0.0.1:8000/ollama/playground/