import argparse
from . import mentor 
from pprint import pprint

def main():
    parser = argparse.ArgumentParser(description="LocalMentor CLI tool")

    subparsers_action = parser.add_subparsers(dest="action", help="Top-level actions")

    # Parser for 'ask' action
    do_parser = subparsers_action.add_parser("ask", help="Ask a question")
    do_parser.add_argument("--prompt", required=True, help="Prompt")

    args = parser.parse_args()

    if args.action == "ask":
        results = mentor(args.prompt)
        pprint(results)
    else:
        print("Invalid action")

if __name__ == "__main__":
    main()
