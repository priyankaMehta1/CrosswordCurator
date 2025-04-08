import argparse
from wikisearch import search_wiki

from pathlib import Path
root_dir = str(Path(__file__).resolve().parent.parent)

def write_output(word_set, unique_only):
    if unique_only:
        with open(root_dir + "/data/all_words.txt") as f:
            all_dictionary_words = set([w.strip() for w in f.readlines()])
        word_set = word_set - all_dictionary_words
        f.close()
    else:
        with open(root_dir + "/data/all_words.txt") as f:
            all_dictionary_words = set([w.strip() for w in f.readlines()])
        word_set |= all_dictionary_words
        f.close()

    with open(root_dir + "/data/out_words.txt", "w") as outfile:
        for word in word_set:
            outfile.write(word + "\n")
    outfile.close()

def main():
    """
    Main function that ties together the program's logic.
    """
    # Create ArgumentParser object, define arguments
    parser = argparse.ArgumentParser(description="A custom word list curator program for crosswords.")
    parser.add_argument(
        "source", 
        choices=["Wikipedia","Spotify"], 
        help="The source from which to scrape information."
    )
    parser.add_argument(
        "--page", 
        type=str, 
        help="The Wikipedia page to scrape."
    )
    parser.add_argument(
        "--unique", 
        action='store_true',
        help="Save only those words not found in a dictionary. If False, save all dictionary words along with any unique words found."
    )
    parser.add_argument(
        "--conn-file", 
        type=str, 
        help="File path containing Spotify Client ID and Secret."
    )
    parser.add_argument(
        "--outfile", 
        type=str, 
        default="words_out.txt", 
        help="File path to write the final word list to."
    )

    # Parse args, call helper functions accordingly
    args = parser.parse_args()
    if args.source=="Wikipedia":
        if not args.page:
            print(f"You must provide a page title when choosing Wikipedia as the source.")
            return
        word_set = search_wiki(args.page)

        # build in logic to return list with or without dictionary words
        write_output(word_set, args.unique)

        

# This ensures that the main() function only runs when the script is executed directly.
if __name__ == "__main__":
    main()