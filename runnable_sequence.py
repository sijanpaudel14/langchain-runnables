import os
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel
from dotenv import load_dotenv
load_dotenv()
os.system('clear')

model = GoogleGenerativeAI(
    model="gemini-2.0-flash",
)

parser = StrOutputParser()


prompt1 = PromptTemplate(
    input_variables=["topic"],
    template="Write a 100-word blog post about {topic}."
)

prompt2 = PromptTemplate(
    input_variables=["blog_post"],
    template="Generate a catchy title for the following blog post:\n{blog_post}"
)

chain  = RunnableSequence(prompt1, model, parser, prompt2, model, parser)

def run_runnable_sequence(topic):
    result = chain.invoke({"topic": topic})
    return result  

print("Welcome to the Blog Post Generator!")
result = run_runnable_sequence("Innovation in Technology")
print("\nGenerated Blog Post:")
print(result)
print("\nThank you for using the Blog Post Generator!")