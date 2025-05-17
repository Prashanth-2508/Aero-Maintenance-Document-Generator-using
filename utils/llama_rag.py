from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"
model_id = "TheBloke/Llama-2-7B-Chat-GGUF"  # or use Llama-3
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.float16, device_map="auto")

generator = pipeline("text-generation", model=model, tokenizer=tokenizer, max_new_tokens=512)

def generate_from_context(query, retrieved_context):
    prompt = f"""
You are an aerospace maintenance assistant.

Based on the following context, answer the user's query.

Context:
{retrieved_context}

Query:
{query}

Response:
"""
    result = generator(prompt)[0]['generated_text']
    return result.replace(prompt, '').strip()

