"""
Text Processor Module
=====================
Handles text preprocessing, cleaning, and normalization for NLP analysis.
"""

import re
import string
from typing import List


# Common English stop words (avoiding external dependency on NLTK for portability)
STOP_WORDS = {
    "a", "an", "the", "and", "or", "but", "in", "on", "at", "to", "for",
    "of", "with", "by", "from", "is", "am", "are", "was", "were", "be",
    "been", "being", "have", "has", "had", "do", "does", "did", "will",
    "would", "could", "should", "may", "might", "shall", "can", "need",
    "dare", "ought", "used", "it", "its", "i", "me", "my", "we", "our",
    "you", "your", "he", "him", "his", "she", "her", "they", "them",
    "their", "this", "that", "these", "those", "what", "which", "who",
    "whom", "how", "when", "where", "why", "not", "no", "nor", "if",
    "then", "else", "so", "than", "too", "very", "just", "about", "above",
    "after", "again", "all", "also", "any", "because", "before", "between",
    "both", "each", "few", "further", "here", "into", "more", "most",
    "other", "out", "over", "own", "same", "some", "such", "there",
    "through", "under", "until", "up", "while", "down", "during", "only",
    "as", "once", "etc", "eg", "ie", "vs", "via",
}


def clean_text(text: str) -> str:
    """
    Clean and normalize raw text.

    Steps:
        1. Convert to lowercase.
        2. Remove URLs.
        3. Remove email addresses.
        4. Remove phone numbers.
        5. Remove special characters (keep alphanumerics, spaces, hyphens, plus, hash).
        6. Normalize whitespace.

    Args:
        text: Raw text string.

    Returns:
        Cleaned text string.
    """
    if not text:
        return ""

    text = text.lower()
    text = re.sub(r"https?://\S+|www\.\S+", " ", text)
    text = re.sub(r"\S+@\S+\.\S+", " ", text)
    text = re.sub(r"[\+]?[\d\s\-\(\)]{7,15}", " ", text)
    text = re.sub(r"[^\w\s\-\+\#\.]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()

    return text


def remove_stop_words(text: str) -> str:
    """
    Remove common English stop words from text.

    Args:
        text: Input text string.

    Returns:
        Text with stop words removed.
    """
    if not text:
        return ""

    words = text.split()
    filtered = [w for w in words if w.lower() not in STOP_WORDS]
    return " ".join(filtered)


def tokenize(text: str) -> List[str]:
    """
    Tokenize text into a list of words.

    Args:
        text: Input text string.

    Returns:
        List of word tokens.
    """
    if not text:
        return []

    return text.split()


def preprocess_text(text: str, remove_stops: bool = True) -> str:
    """
    Full preprocessing pipeline: clean, optionally remove stop words.

    Args:
        text: Raw text string.
        remove_stops: Whether to remove stop words.

    Returns:
        Preprocessed text string.
    """
    text = clean_text(text)
    if remove_stops:
        text = remove_stop_words(text)
    return text


def extract_sentences(text: str) -> List[str]:
    """
    Split text into sentences.

    Args:
        text: Input text string.

    Returns:
        List of sentences.
    """
    if not text:
        return []

    sentences = re.split(r"[.!?\n]+", text)
    return [s.strip() for s in sentences if s.strip()]


def get_word_frequency(text: str) -> dict:
    """
    Calculate word frequency in text.

    Args:
        text: Input text string (should be preprocessed).

    Returns:
        Dictionary mapping words to their frequencies.
    """
    if not text:
        return {}

    words = tokenize(text)
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq
