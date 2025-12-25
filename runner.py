import os
import datetime
import json
from chatbots import chat_model_triage_manager
from evals import eval_triage_manager

# GLOBAL VARS
DEFAULT_RUNS_PER_TEST = 2


# Fetches JSON data for test cases
def test_case_setup(json_file_name: str) -> dict:
    with open(json_file_name, "r") as file:
        data = json.load(file)
    return data


# Determines the test cases to run and creates a result dict.
# Format: {Test Case ID : pass rate}
def run_test_cases(test_case_dict: dict) -> dict:
    results_dict = {}
    for t in test_case_dict:
        result = process_one_test_case(t)
        results_dict[t["id"]] = result
    return results_dict


def process_one_test_case(test_case: dict) -> dict:
    passed_runs = 0
    failed_runs = 0
    num_runs = max(DEFAULT_RUNS_PER_TEST, test_case.get("num_of_runs_override", DEFAULT_RUNS_PER_TEST))

    for _ in range(num_runs):
        resp = response_from_chatbot(test_case["bot"], test_case["model"], test_case["prompt"])
        resp_eval = evaluate_response_from_chatbot(resp, test_case["invariant_type"],
                                                   test_case[test_case["invariant_type"]])
        if resp_eval:
            passed_runs += 1
        else:
            failed_runs += 1

    pass_rate = round(((passed_runs / num_runs) * 100), 1)
    results = {"bot": test_case["bot"],
               "model": test_case["model"],
               "passes": passed_runs,
               "fails": failed_runs,
               "pass_rate": pass_rate}
    return results


def create_results_file(results_dict: dict, test_filename: str) -> None:
    os.makedirs("results", exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
    filename = f"results/{test_filename}_{timestamp}.json"
    output = {
        "run_timestamp": timestamp,
        "results": results_dict
    }

    with open(filename, "w") as file:
        json.dump(output, file, indent=2)
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
    fetched_test_case_filename = "max_char_test_cases"
    fetched_tests = test_case_setup(f"test_cases/{fetched_test_case_filename}.json")
    eval_results = run_test_cases(fetched_tests)
    create_results_file(eval_results, fetched_test_case_filename)
