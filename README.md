# ollama-bench-llm
Ollama Benchmarking 

## Setup:

```bash
python -m venv bench
source ./bench/bin/activate
```

### Dependencies:
```
pip install -r requirements.txt
```

## How to Run

Single Query Execution
```bash
python main.py --model_name <model_name> --base_url <url> --test_query <test_query>
```

Multiple Queries Execution:
```bash
python main.py --model_name <model_name> --base_url <url> --test_file <file_path_txt>
```

Sample format for test_file is given in `sample.txt` in the repository.

