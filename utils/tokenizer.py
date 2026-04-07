import tiktoken

tokenizer = tiktoken.get_encoding("cl100k_base")

def tokenize_name(name):
    tokens = tokenizer.encode(name)
    token_strings = [tokenizer.decode([t]) for t in tokens]
    return tokens, token_strings

def compute_tgdi(name, tokens):
    chars = len(name.replace(" ", ""))
    return len(tokens) / max(chars, 1)

def estimate_cost(tokens, price_per_1k=0.03):
    return (len(tokens) / 1000) * price_per_1k