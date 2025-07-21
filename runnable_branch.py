import os
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableBranch, RunnablePassthrough, RunnableParallel, RunnableLambda
from dotenv import load_dotenv
load_dotenv()
os.system('clear')


model = GoogleGenerativeAI(
    model="gemini-2.0-flash",
)
parser = StrOutputParser()


prompt1 = PromptTemplate(
    template="Write a detailed report on the topic {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Summarize the following report in one paragraph:\n{report}",
    input_variables=["report"]
)

report_gen_chain = prompt1 | model | parser

branch_chain = RunnableBranch(
    # Condition to check if report is long
    (lambda x: len(x.split()) > 500, prompt2 | model | parser),
    RunnablePassthrough()  # If not long, just pass through the report
)

final_chain = report_gen_chain | branch_chain

result = final_chain.invoke(
    {"topic": "Climate Change and its Impact on Global Ecosystems"})
print(result)
