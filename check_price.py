import palooza_wizard.chatgpt as chatgpt
import palooza_wizard.constants as ct
import palooza_wizard.utils as utils

run_cost = 0
files = utils.get_files_in_folder(ct.IMPORTANCE_OUTPUT_FOLDER)
for file in files: 
    with open(file, "r") as f:
        string = str(f.read())
    num_tokens = chatgpt.num_tokens_for_model(string)
    input_cost = chatgpt.estimated_input_usage_cost(num_tokens)
    run_cost += input_cost
print(f"Total run cost: {run_cost}")

#num_tokens = 10 ** 6
#training_cost = chatgpt.estimated_training_cost(num_tokens)
#print(training_cost)