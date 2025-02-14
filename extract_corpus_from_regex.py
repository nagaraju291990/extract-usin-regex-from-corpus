import re
import sys

def load_file(file_path):
    """Load content from a file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read().split("\n")

def match_regex(corpus_lines, regex_patterns):
    """Match regex patterns against the corpus and print results."""
    matches = {}
    
    for regex in regex_patterns:
        # regex = regex.strip()
        if(regex.startswith("#")):
            continue
        original_regex = regex
        regex = re.sub(r'#.*','',regex)
        pattern = re.compile(regex)
        matches[original_regex] = [line.strip() for line in corpus_lines if pattern.search(line.strip())]
    
    return matches

def main():
    corpus_file = sys.argv[1]  # Text corpus file
    regex_file = sys.argv[2]  # File containing regex patterns
    
    corpus_lines = load_file(corpus_file)
    regex_patterns = load_file(regex_file)
    
    results = match_regex(corpus_lines, regex_patterns)
    
    for regex, matched_lines in results.items():
        print(f"Regex: |{regex}|")
        if matched_lines:
            for line in matched_lines:
                print(f"{regex}\t{line}")
        else:
            print("  No matches found.")
        print("-" * 50)



if __name__ == "__main__":
    main()
