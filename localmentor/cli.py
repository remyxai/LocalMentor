import argparse
from . import mentor 
from pprint import pprint

def format_and_print_output(output):
    OKGREEN = '\033[92m'  # Green
    ENDC = '\033[0m'     # End color formatting
    BOLD = '\033[1m'     # Bold text
    # Function to wrap text lines to a specified width
    def wrap_line(line, width):
        words = line.split()
        wrapped_lines = []
        current_line = []

        for word in words:
            # Check if adding the word would exceed the width
            if sum(len(w) for w in current_line) + len(word) + len(current_line) > width:
                wrapped_lines.append(' '.join(current_line))
                current_line = [word]
            else:
                current_line.append(word)

        if current_line:
            wrapped_lines.append(' '.join(current_line))

        return wrapped_lines
    

    # Splitting the output to extract the prompt and the response
    prompt_end_index = output.find("'") + 1
    prompt_end_index = output.find("'", prompt_end_index) + 1
    
    prompt = output[:prompt_end_index].strip()
    response = output[prompt_end_index:].strip()

    # Define the maximum line width (adjust as needed)
    max_line_width = 80

    # Printing the formatted output
    for paragraph in response.split('\n'):
        wrapped_paragraph = wrap_line(paragraph, max_line_width)
        for line in wrapped_paragraph:
            print(f"{BOLD}{OKGREEN}{line}{ENDC}")
        print()

def main():
    parser = argparse.ArgumentParser(description="LocalMentor CLI tool")

    subparsers_action = parser.add_subparsers(dest="action", help="Top-level actions")

    # Parser for 'ask' action
    ask_parser = subparsers_action.add_parser("ask", help="Ask a question")
    ask_parser.add_argument("--prompt", required=True, help="Prompt")
    ask_parser.add_argument("-nf", "--no-format", action="store_true", help="Skip formatting and pretty-print raw results")

    args = parser.parse_args()

    if args.action == "ask":
        results = mentor(args.prompt)
        if args.no_format:
            pprint(results)
        else:
            format_and_print_output(results)
    else:
        print("Invalid action")

if __name__ == "__main__":
    main()
