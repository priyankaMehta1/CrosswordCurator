import wikipedia
import string
import re

def search_wiki(page_name):
    """
    Returns the given Wikipedia page's content

    Args:
        page_name (string): The Wikipedia page to scrape.

    Returns:
        file_name: The location where the content was written.

    Raises:
        DisambiguationError: If the title is associated with multiple pages.
    """
    search_query = f"{page_name}"
    try:
        # Search Wikipedia
        result = wikipedia.search(search_query, results=1)
        if result:
            # Fetch Wikipedia page and content
            content = wikipedia.page(result[0]).content
            return extract_content(content)
        else:
            return "Page not found on Wikipedia."
    # If multiple pages found, raise Disambiguation Error
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Disambiguation error: {e.options}"

def remove_punctuation(text):
    """
    Removes punctuation from a string.

    Args:
    text: The string to remove punctuation from.

    Returns:
    The string with punctuation removed.
    """
    # Manual fixes for hyphenated words
    text = text.replace("-", " ")
    text = text.replace("—", " ")
    text = text.replace("–", " ")
    text = text.replace("/", " ")

    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)

def remove_digits(text):
    """
    Removes digits from a string.

    Args:
    text: The string to remove digits from.

    Returns:
    The string with digits removed.
    """
    return re.sub(r"\d", "", text)

def remove_short_words(text_list):
    """
    Removes words fewer than 3 characters from a list.

    Args:
    text: The list to remove words from.

    Returns:
    The list with short words removed.
    """
    return [word for word in text_list if len(word)>2]

def clean_content(text):
    """
    Removes invalid crossword characters from a string.

    Args:
    text: The string to remove invalid characters from.

    Returns:
    The string with invalid characters removed.
    """
    text = remove_punctuation(text)
    text = remove_digits(text)
    return text

def extract_content(content):
    """
    Extracts the given Wikipedia page's content

    Args:
        content (string): Wikipedia page content.

    Returns:
        all_words: Unique words in the Wikipedia page.
    """
    all_lines = list(map(clean_content, content.lower().splitlines()))
    all_words = [word.strip() for line in all_lines for word in line.split(" ")]
    all_words = remove_short_words(all_words)
    return set(all_words)