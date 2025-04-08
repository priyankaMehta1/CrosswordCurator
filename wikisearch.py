import wikipedia

# Function to search for raga associated with the song on Wikipedia
def search_wiki(song_name):
    # Query Wikipedia for the song
    search_query = f"{song_name}"
    try:
        # Search in Wikipedia
        result = wikipedia.search(search_query, results=1)
        if result:
            # Fetch the Wikipedia page about the song
            page = wikipedia.page(result[0])
            content = page.content
            return extract_content(content)
        else:
            return "Page not found on Wikipedia."
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Disambiguation error: {e.options}"

# Helper function to extract raga from the page content
def extract_content(content):
    all_lines = content.lower().splitlines()
    all_words = set([k for line in all_lines for k in line])
    return all_words

    ## should make sure to remove common dictionary words here if requested

# Main driver code
if __name__ == "__main__":
    wiki_page = input("Enter the name of the Wikipedia page: ")
    word_set = search_wiki(wiki_page)
    print(f"Word set found on Wikipedia page: '{wiki_page}': {word_set}")