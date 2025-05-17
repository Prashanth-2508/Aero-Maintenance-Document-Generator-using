from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# Assume local LLaMA model is downloaded (use HF model like meta-llama/Llama-2-7b-chat-hf)

model_id = "TheBloke/Llama-2-7B-Chat-GGML"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)
pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, max_new_tokens=512)

def generate_from_context(query, context):
    prompt = f"Context: {context}\n\nQuery: {query}\n\nAnswer:"
    output = pipe(prompt)[0]["generated_text"]
    return output.split("Answer:")[-1].strip()
