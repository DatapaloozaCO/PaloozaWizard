import tiktoken

def num_tokens_with_encoding(string: str, encoding_name: str = "cl100k_base") -> int:
    """This function computes the number of tokens in a string
    #https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb
    """
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

def num_tokens_for_model(string: str, model_name: str = "gpt-4") -> int:
    """This function computers the number of token in a string for a specific model name
    #https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb
    """
    encoding = tiktoken.encoding_for_model(model_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens