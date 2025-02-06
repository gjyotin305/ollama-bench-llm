import pyfiglet
from termcolor import colored
from ollama import Client
from benchmark import run_tests
import argparse
import sys
import logging

def print_banner():
    ascii_banner = pyfiglet.figlet_format("OllamaBench", font="slant")
    color_banner = colored(ascii_banner, "red", attrs=["bold", "dark"])
    color_owner = colored("by github.com/gjyotin305", "red", attrs=["bold", "dark"])
    print(colored("=" * 60, "red", attrs=["dark", 'bold']))
    print(color_banner)
    print(color_owner)
    print(colored("=" * 60, "red", attrs=["dark", 'bold']))

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)]
    )

def main():
    print_banner()
    setup_logging()

    parser = argparse.ArgumentParser(
        description="OllamaBench: CLI Tool for Benchmarking Ollama Models",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    parser.add_argument("--model_name", type=str, help="Name of the model to benchmark")
    parser.add_argument("--base_url", type=str, help="Base URL of the Ollama server")
    parser.add_argument("--test_query", type=str, help="Test query to evaluate the model")

    args = parser.parse_args()
    
    logging.info(f"Connecting to Ollama server at {args.base_url}")
    
    try:
        client = Client(host=args.base_url)
        logging.info(f"Running benchmark for model: {args.model_name}")
        results = run_tests(
            model_names=[args.model_name], 
            test_prompts=[args.test_query],
            client=client
        )
        logging.info(f"RESULTS ARE {results}")
        
    except Exception as e:
        logging.error(f"Error during benchmarking: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
