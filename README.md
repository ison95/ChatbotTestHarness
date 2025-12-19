<h2>README.md (V1) </h2>
<h3> AI Chatbot Test Harness (V1) </h3>
This project is a lightweight, dataset-driven testing harness for evaluating the behavioral reliability of large language model (LLM) chatbots. It focuses on validating response invariants (e.g. maximum word count) rather than exact outputs, reflecting the non-deterministic nature of generative AI systems.

The goal of this project is to explore practical testing strategies for AI systems using a traditional QA mindset: constraint validation, edge-case detection, and repeatable evaluation.

<h3> Key Features </h3>

* Dataset-driven test cases defined in JSON
* Pluggable chatbot routing (currently OpenAI)
* Invariant-based evaluation (e.g. max word count)
* Clean separation between:
  * Chatbot triage
  * Model interaction
  * Response evaluation
* Designed to be extended with additional invariants, models, and metrics

<h3> Why This Exists </h3>

Unlike traditional software, AI chatbot responses are probabilistic and may vary between runs. This project demonstrates how to test such systems by asserting behavioral constraints instead of exact outputs.

Examples of tested behaviors include:
* Response length limits
* Format compliance
* Stability across repeated runs (future work)


<h3> ⚙️ Setup </h3>

1. Create a virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate

2. Install dependencies
```
pip install -r requirements.txt
```

3. Configure environment variables
   * Create a .env file based on the provided example: 
```
OPENAI_API_KEY=your_api_key_here
```

Note: The .env file is intentionally excluded from version control.

<h3> ▶️ Running the Tests </h3>
Run the runner script:

```
python runner.py
```
Example output:
```
max words is 100
word count is 83
max words is 100
word count is 78
{'openai_max100char_test1': True, 'openai_max100char_test2': True}
Summary: 2/2 tests passed
```

🔍 Example Test Case
```
{
  "id": "openai_100char_test1",
  "bot": "openai",
  "model": "gpt-5-nano",
  "prompt": "Summarize the plot of Hamlet in under 100 words.",
  "invariant_type": "max_words",
  "max_words": 100
}
```

Each test case specifies:
* The chatbot provider
* The model to use
* The prompt
* The behavioral invariant to evaluate

<h3> 🚧 Current Limitations (V1) </h3>

* Single invariant type (max words)
* Single chatbot provider (OpenAI)
* No result persistence or historical comparison
* No statistical aggregation across runs

These are intentional to keep V1 minimal and focused.

<h3> Future Enhancements (Planned) </h3>

* Additional invariants (format, refusal handling, factual consistency)
* Repeated runs and pass-rate analysis 
* Bias and edge-case testing 
* Multi-provider comparisons (e.g. Gemini, Claude)
* Result persistence and trend analysis