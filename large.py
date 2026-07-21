from transformers import pipeline

llm = pipeline(
    "text-generation",
    model="gpt2"
)

result = llm(
    "What is Artificial Intelligence?",
    max_new_tokens=100
)

print(result[0]["generated_text"])