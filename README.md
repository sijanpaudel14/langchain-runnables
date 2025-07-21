# LangChain Runnables Learning Project

This repository contains practical examples demonstrating the core concepts of **LangChain Runnables** - a powerful framework for building composable AI applications with Google's Gemini AI model.

## 📚 What You'll Learn

This project covers the fundamental building blocks of LangChain's Runnable interface:

- **RunnableSequence**: Chain operations sequentially
- **RunnableParallel**: Execute multiple operations concurrently
- **RunnablePassthrough**: Pass data through without modification
- **RunnableLambda**: Apply custom transformations
- **RunnableBranch**: Conditional execution based on data

## 🛠️ Prerequisites

Before running these examples, ensure you have:

1. **Python 3.8+** installed
2. **Google AI API Key** (for Gemini model access)
3. Required dependencies (see Installation section)

## 📦 Installation

1. Clone this repository:

```bash
git clone <repository-url>
cd langchain-runnables
```

2. Install required packages:

```bash
pip install langchain-google-genai langchain-core python-dotenv
```

3. Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

## 🔍 Project Structure

```
langchain-runnables/
├── runnable_sequence.py      # Sequential chain execution
├── runnable_parallel.py      # Parallel execution examples
├── runnable_passthrough.py   # Data passthrough patterns
├── runnable_lambda.py        # Custom transformations
├── runnable_branch.py        # Conditional logic
├── .env                      # Environment variables
└── README.md                 # This file
```

## 📖 Examples Overview

### 1. RunnableSequence (`runnable_sequence.py`)

**Concept**: Execute operations in a sequential chain where the output of one step becomes the input of the next.

**Use Case**: Blog Post Generator

- Generate a blog post about a topic
- Create a catchy title for the generated post

**Key Learning**: How to chain multiple prompts and models together in a pipeline.

```python
chain = RunnableSequence(prompt1, model, parser, prompt2, model, parser)
```

### 2. RunnableParallel (`runnable_parallel.py`)

**Concept**: Execute multiple operations simultaneously on the same input data.

**Use Case**: Social Media Content Generator

- Generate a Twitter post with hashtags and emojis
- Generate a professional LinkedIn post
- Both generated simultaneously from the same topic

**Key Learning**: How to create multiple content variations efficiently.

```python
parallel_chain = RunnableParallel({
    "tweet": RunnableSequence(prompt1, model, parser),
    "linkedin_post": RunnableSequence(prompt2, model, parser)
})
```

### 3. RunnablePassthrough (`runnable_passthrough.py`)

**Concept**: Pass data through without modification while enabling parallel processing.

**Use Case**: Blog Post with Metadata

- Generate blog post content
- Pass the content through while generating a title
- Return both original content and generated title

**Key Learning**: How to maintain original data while adding computed values.

```python
parallel_chain = RunnableParallel({
    'blog_post': RunnablePassthrough(),
    'title': RunnableSequence(prompt2, model, parser)
})
```

### 4. RunnableLambda (`runnable_lambda.py`)

**Concept**: Apply custom transformations and calculations within the chain.

**Use Case**: Content Analytics

- Generate blog post and title
- Calculate word counts for both
- Apply custom lambda functions for metrics

**Key Learning**: How to integrate custom Python functions into LangChain pipelines.

```python
blog_word_count_chain = RunnableSequence(
    topic_gen_chain,
    RunnableLambda(lambda x: len(x.split()))
)
```

### 5. RunnableBranch (`runnable_branch.py`)

**Concept**: Implement conditional logic to execute different paths based on data characteristics.

**Use Case**: Smart Report Processor

- Generate a detailed report
- If report is long (>500 words): automatically summarize
- If report is short: pass through unchanged

**Key Learning**: How to implement dynamic behavior based on content analysis.

```python
branch_chain = RunnableBranch(
    (lambda x: len(x.split()) > 500, prompt2 | model | parser),
    RunnablePassthrough()
)
```

## 🚀 Running the Examples

Each file can be run independently:

```bash
python runnable_sequence.py
python runnable_parallel.py
python runnable_passthrough.py
python runnable_lambda.py
python runnable_branch.py
```

## 🎯 Key Concepts Mastered

### 1. **Composability**

- Learned how to combine simple components into complex workflows
- Understanding of the pipe operator (`|`) for chaining

### 2. **Parallelization**

- Efficient concurrent execution of independent operations
- Resource optimization through parallel processing

### 3. **Data Flow Management**

- Controlling how data moves through processing pipelines
- Maintaining and transforming data at different stages

### 4. **Conditional Logic**

- Implementing smart decision-making in AI workflows
- Dynamic behavior based on content characteristics

### 5. **Custom Transformations**

- Integrating custom Python logic into LangChain pipelines
- Extending functionality with lambda functions

## 🔧 Advanced Features Explored

- **Graph Visualization**: Using `get_graph().print_ascii()` to visualize chain structure
- **Error Handling**: Understanding how errors propagate through chains
- **Performance Optimization**: Balancing sequential vs parallel execution
- **Memory Management**: Efficient data passing between components

## 💡 Best Practices Learned

1. **Start Simple**: Begin with basic sequences before adding complexity
2. **Parallel When Possible**: Use RunnableParallel for independent operations
3. **Pass Data Efficiently**: Use RunnablePassthrough to avoid unnecessary recomputation
4. **Add Logic Thoughtfully**: Use RunnableBranch for meaningful conditional execution
5. **Transform Strategically**: Apply RunnableLambda for specific data manipulations

## 🔮 Next Steps

To further enhance your LangChain Runnables knowledge:

1. **Error Handling**: Implement robust error handling and retry logic
2. **Streaming**: Explore streaming responses for real-time applications
3. **Memory Integration**: Add conversation memory for stateful applications
4. **Custom Runnables**: Create custom Runnable classes for specialized use cases
5. **Production Deployment**: Scale these patterns for production environments

## 📝 Notes

- All examples use Google's Gemini 2.0 Flash model
- Environment variables are loaded from `.env` file
- Each script clears the terminal for clean output display
- Code is structured for educational clarity and easy modification

## 🤝 Contributing

Feel free to extend these examples or add new Runnable patterns to enhance the learning experience!

---

**Happy Learning with LangChain Runnables! 🎉**
