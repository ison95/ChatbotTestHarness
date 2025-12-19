import json
from chatbots import chat_model_triage_manager
from evals import eval_triage_manager


# Fetches JSON data for test cases
def test_case_setup(json_file_name: str) -> dict:
    with open(json_file_name, "r") as file:
        data = json.load(file)
    return data


# Determines the test cases to run and creates a dict for:
# {Test Case ID : Result Evaluation}
def run_test_cases(test_case_dict: dict) -> dict:
    results_dict = {}
    for t in test_case_dict:
        resp = response_from_chatbot(t["bot"], t["model"], t["prompt"])
        resp_eval = evaluate_response_from_chatbot(resp, t["invariant_type"], t[t["invariant_type"]])
        results_dict[t["id"]] = resp_eval
    return results_dict


# TODO: Create a function that's responsible for storing the results of the run
def create_results_file(results_dict: dict):
    return


# Receives output from specified bot
def response_from_chatbot(bot: str, model: str, prompt: str) -> str:
    model_response = chat_model_triage_manager.triage_response_from_bot(bot, model, prompt)
    return model_response


# Receives bot response and determines whether it is "correct" by specified invariance
def evaluate_response_from_chatbot(response: str, invariant_type: str, invariant_var) -> bool:
    resp_eval = eval_triage_manager.evaluate_response(response, invariant_type, invariant_var)
    return resp_eval


if __name__ == "__main__":
    fetched_tests = test_case_setup("test_cases/max_char_test_cases.json")
    eval_results = run_test_cases(fetched_tests)
    passed = sum(eval_results.values())
    total = len(eval_results)
    print(eval_results)
    print(f"Summary: {passed}/{total} tests passed")

