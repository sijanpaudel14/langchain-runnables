import os
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough
from dotenv import load_dotenv
load_dotenv()
os.system('clear')

model = GoogleGenerativeAI(
    model="gemini-2.0-flash",
)
parser = StrOutputParser()

prompt1 = PromptTemplate(
    input_variables=["topic"],
    template="Write a 100-word blog post about {topic}.without title"
)

prompt2 = PromptTemplate(
    input_variables=["blog_post"],
    template="Generate one catchy title for the following blog post without giving any unnecessary explanation:\n{blog_post}"
)
topic_gen_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel({
    'blog_post': RunnablePassthrough(),
    'title': RunnableSequence(prompt2, model, parser)
})
final_chain = RunnableSequence(topic_gen_chain, parallel_chain)

result = final_chain.invoke({"topic": "Innovation in Technology"})
print(result)

final_chain.get_graph().print_ascii()