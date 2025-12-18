import json


# TODO: Create a function that takes in a test case's contents: ID, Prompt, Invariant. Should return the output.
def response_from_chatbot(self, test_case_id: str, prompt: str, invariant: str, chatbot="CHATGPT") -> str:
    # TODO: Create another file that interfaces with ChatGPT's API
    return


# TODO: Create a function that takes in an output string and determines whether it is "correct".
def evaluate_response_from_chatbot(self, response: str) -> bool:
    # TODO: Maybe create an invariant file that triages to the pertinent check(s)?
    return


# Determines the test cases to run and creates a dict for:
# {Test Case ID : Result Evaluation}
def run_test_cases(self, test_case_dict: dict) -> dict:
    results_dict = {}
    for t in test_case_dict:
        resp = response_from_chatbot(t["id"], t["prompt"], t["invariant"])
        resp_eval = evaluate_response_from_chatbot(resp)
        results_dict[t["id"]] = resp_eval
    return results_dict


# Fetches JSON data for test cases
def test_case_setup(self, json_file_name: str) -> dict:
    with open(json_file_name, "r") as file:
        data = json.load(file)
    return data


# TODO: Create a function that's responsible for storing the results of the run
def create_results_file(results_dict: dict):
    return


if __name__ == "__main__":
    fetched_tests = test_case_setup("prompts.json")
    eval_results = run_test_cases(fetched_tests)