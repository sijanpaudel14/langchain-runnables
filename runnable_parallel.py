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

prompt1 = PromptTemplate(
    input_variables=["topic"],
    template = 'Generate a tweet about {topic}. Use hashtags and emojis.'
) 
prompt2 = PromptTemplate(
    input_variables=["topic"],
    template = 'Generate a LinkedIn post about {topic}. Use a professional tone.'
)

parser = StrOutputParser()

parallel_chain = RunnableParallel(
    {
        "tweet": RunnableSequence(prompt1, model, parser),
        "linkedin_post": RunnableSequence(prompt2, model, parser)
    }
)

result = parallel_chain.invoke({"topic": "Innovation in Technology"})
print(result['tweet'])
print("\nGenerated LinkedIn Post:")
print(result['linkedin_post'])
print("\nThank you for using the Social Media Post Generator!")
