import json


def fetch_data_from_filepaths(run_filepath_1: str, run_filepath_2: str) -> (dict, dict):
    with open(run_filepath_1, "r") as file:
        run_1_data = json.load(file)

    with open(run_filepath_2, "r") as file:
        run_2_data = json.load(file)

    return run_1_data, run_2_data


def compare_run_data(run_1_data: dict, run_2_data: dict) -> dict:
    comparison_results = {}
    run_1_all_results = run_1_data.get("results")
    run_2_all_results = run_2_data.get("results")

    # None Check
    if run_1_all_results is None or run_2_all_results is None:
        return None

    for test_case_id, test_case_1_results in run_1_all_results.items():
        test_case_2_results = run_2_all_results.get(test_case_id)

        # None check
        if test_case_id is None or test_case_2_results is None:
            continue

        # Comparison
        if test_case_1_results.get("pass_rate") == test_case_2_results.get("pass_rate"):
            comparison_results[test_case_id] = f"pass rate is unchanged ({test_case_1_results.get('pass_rate')}%)."
        elif test_case_1_results["pass_rate"] > test_case_2_results.get("pass_rate"):
            comparison_results[test_case_id] = f"pass rate has decreased " \
                                                       f"({test_case_1_results.get('pass_rate')}% -> " \
                                                       f"{test_case_2_results.get('pass_rate')}%)."
        elif test_case_1_results.get("pass_rate") < test_case_2_results.get("pass_rate"):
            comparison_results[test_case_id] = f"pass rate has increased " \
                                                       f"({test_case_1_results.get('pass_rate')}% -> " \
                                                       f"{test_case_2_results.get('pass_rate')}%)."

    return comparison_results

    # Data Format: {
    #   "run_timestamp": "2025-12-22T16-44-20",
    #   "results": {
    #     "openai_max100char_test1": {
    #       "bot": "openai",
    #       "model": "gpt-5-nano",
    #       "passes": 2,
    #       "fails": 0,
    #       "pass_rate": 100.0
    #     }
    #   }
    # }


if __name__ == "__main__":
    filepath1 = input("Drag and drop the first report here: ")
    filepath2 = input("Drag and drop the second report here: ")
    run1, run2 = fetch_data_from_filepaths(filepath1, filepath2)
    comparison = compare_run_data(run1, run2)
    print(comparison)
