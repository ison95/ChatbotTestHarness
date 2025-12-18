import openai_manager


# GENERAL TRIAGE
def triage_response_from_bot(bot_name: str, model_name: str, prompt: str) -> str:
    if bot_name == "openai":
        triage_response_from_openai_models(model_name, prompt)
    else:
        raise RuntimeError(f"ERROR: Attempted to triage {bot_name}, but its triage hasn't been implemented yet in"
                           f"chat_model_triage_manager.py under the triage_response_from_bot function.")


# OPENAI MODELS
def triage_response_from_openai_models(model_name: str, prompt: str):
    if model_name == "gpt-5-nano":
        model_client = openai_manager.setup()
        model_response = openai_mmanager.prompt_openai(model_client, prompt)
        return model_response
    else:
        raise RuntimeError(f"ERROR: Attempted to triage {model_name}, but its triage hasn't been implemented yet in "
                           f"chat_model_triage_manager.py under the triage_response_from_openai_models function.")
