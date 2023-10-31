import palooza_wizard.chatgpt.constants as ct
from typing import List 

def get_available_models() -> List[str]:
    return list(ct.PRICING.keys())

def validate_model(model: str) -> bool:
    return model in ct.PRICING.keys()

def estimated_training_cost(num_tokens: int, model: str = "GPT-3.5-Turbo") -> float:
    assert validate_model(model), "Invalid model"
    num_tokens_per_cost = ct.PRICING[model]["num_tokens"]
    training_cost = ct.PRICING[model]["training"]
    return (num_tokens / num_tokens_per_cost) * training_cost

def estimated_input_usage_cost(num_tokens: int, model: str = "GPT-3.5-Turbo") -> float:
    assert validate_model(model), "Invalid model"
    num_tokens_per_cost = ct.PRICING[model]["num_tokens"]
    input_cost = ct.PRICING[model]["input_usage"]
    return (num_tokens / num_tokens_per_cost) * input_cost

def estimated_output_usage_cost(num_tokens: int,  model: str = "GPT-3.5-Turbo") -> float:
    assert validate_model(model), "Invalid model"
    num_tokens_per_cost = ct.PRICING[model]["num_tokens"]
    output_cost = ct.PRICING[model]["output_usage"]
    return (num_tokens / num_tokens_per_cost) * output_cost

