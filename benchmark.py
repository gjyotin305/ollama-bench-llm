from ollama import Client
from typing import List
from tqdm import tqdm
import random
import json

class Benchmark(object):
    def __init__(
        self, 
        model: str, 
        created_at: str, 
        total_duration: str, 
        load_duration: str, 
        prompt_eval_count: str, 
        prompt_eval_duration: str, 
        eval_count: str
    ):
        self.model = model
        self.created_at = created_at
        self.total_duration = total_duration
        self.load_duration = load_duration
        self.prompt_eval_count = prompt_eval_count
        self.prompt_eval_duration = prompt_eval_duration
        self.eval_count = eval_count

    def to_dict(self):
        return self.__dict__

    def __str__(self):
        return f"Benchmark(model={self.model}, created_at={self.created_at}, total_duration={self.total_duration}, load_duration={self.load_duration}, prompt_eval_count={self.prompt_eval_count}, prompt_eval_duration={self.prompt_eval_duration}, eval_count={self.eval_count})"


def make_json(tests: List[Benchmark], name: str):
    json_object = [x.to_dict() for x in tests]
    with open(f"{name}.json", "w") as f:
        f.write(json.dumps(json_object, indent=2))
        f.close()

def run_tests(
    model_names: List[str],
    test_prompts: List[str],
    client: Client
) -> List[Benchmark]:
    result = []

    for model_name in model_names:
        print(f"Model: {model_name}")
        for prompt in tqdm(
            test_prompts, 
            desc="Benchmark", 
            leave=False, 
            position=0
        ):
            response = run_response(
                model_name=model_name,
                prompt=prompt,
                client=client
            )
            result.append(response)

    fname = f"bench_{random.randint(0,100)}"

    print(f"FILENAME IS {fname}")

    make_json(
        tests=result,
        name=fname
    )

    return len(result)

def run_response(
    model_name: str, 
    prompt: str,
    client: Client
) -> Benchmark:
    response = client.generate(
        model=model_name,
        prompt=prompt
    )

    response_object = Benchmark(
        model=response.model,
        created_at=response.created_at,
        total_duration=response.total_duration/10**6,
        load_duration=response.load_duration/10**6,
        prompt_eval_count=response.eval_count,
        prompt_eval_duration=response.eval_duration/10**6,
        eval_count=response.eval_count
    )

    return response_object
