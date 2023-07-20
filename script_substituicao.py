#python regex_replace_script.py <regex> <replacement> <filepath>
import re
import argparse

def regex_replace(regex, replacement, filepath):
    try:
        with open(filepath, 'r') as file:
            content = file.read()

        modified_content = re.sub(regex, replacement, content)

        with open(filepath, 'w') as file:
            file.write(modified_content)

        print(f"Substitution successful in {filepath}!")
        file.close()
    except FileNotFoundError:
        print(f"Error: File not found - {filepath}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Regex Replace Script")
    parser.add_argument("regex", help="Regular expression pattern to search for")
    parser.add_argument("replacement", help="Replacement text for matches")
    parser.add_argument("filepath", help="Path to the file where to perform the substitution")

    args = parser.parse_args()

    regex_replace(args.regex, args.replacement, args.filepath)
