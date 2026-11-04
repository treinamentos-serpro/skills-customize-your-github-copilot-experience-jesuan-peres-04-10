def count_words(text: str) -> int:
    """Return the number of whitespace-separated words in text."""
    return len(text.split())


def is_palindrome(text: str) -> bool:
    """Check whether text reads the same backward, ignoring case and whitespace."""
    normalized = "".join(text.lower().split())
    return normalized == normalized[::-1]