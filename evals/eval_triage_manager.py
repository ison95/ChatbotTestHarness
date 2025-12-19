def evaluate_response(response: str, invariant_type: str, invariant_var) -> bool:
    if invariant_type == "max_words":
        evaluation = max_words_evaluation(response, invariant_var)
        return evaluation
    else:
        raise RuntimeError(f"ERROR: Attempted to triage {invariant_type} but its triage hasn't been implemented yet in"
                           f"eval_triage_manager.py under evaluate_response function.")


def max_words_evaluation(response: str, invariant_var: int) -> bool:
    words_list = response.split()
    word_count = len(words_list)
    print(f"max word count is {invariant_var}")
    print(f"word count is {word_count}")
    if word_count <= invariant_var:
        return True
    return False
