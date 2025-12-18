import json
import chat_model_triage_manager


# TODO: Create a function that takes in a test case's contents: ID, Prompt, Invariant. Should return the output.
def response_from_chatbot(bot: str, model: str, prompt: str) -> str:
    model_response = chat_model_triage_manager.triage_response_from_bot(bot, model, prompt)
    return model_response


# TODO: Create a function that takes in an output string and determines whether it is "correct".
def evaluate_response_from_chatbot(response: str, invariant_type: str, *invariant_vars) -> bool:
    # TODO: Maybe create an invariant file that triages to the pertinent check(s)?
    return


# Determines the test cases to run and creates a dict for:
# {Test Case ID : Result Evaluation}
def run_test_cases(test_case_dict: dict) -> dict:
    results_dict = {}
    for t in test_case_dict:
        resp = response_from_chatbot(t["prompt"], t["bot"], t["model"])
        resp_eval = evaluate_response_from_chatbot(resp, t["invariant_type"], t[t["invariant_type"]])
        results_dict[t["id"]] = resp_eval
    return results_dict


# Fetches JSON data for test cases
def test_case_setup(json_file_name: str) -> dict:
    with open(json_file_name, "r") as file:
        data = json.load(file)
    return data


# TODO: Create a function that's responsible for storing the results of the run
def create_results_file(results_dict: dict):
    return


if __name__ == "__main__":
    fetched_tests = test_case_setup("prompts.json")
    eval_results = run_test_cases(fetched_tests)
    print(eval_results)

