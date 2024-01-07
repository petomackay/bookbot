from main import get_char_counts
from main import get_word_count
from main import get_sorted_char_counts

text = "This is a testing text."


def test_word_count():
    assert get_word_count(text) == 5


def test_char_counts():
    counts = get_char_counts(text)
    assert "T" not in counts
    assert "t" in counts
    assert counts["t"] == 5


def test_sorted_counts():
    sorted_counts = get_sorted_char_counts(get_char_counts(text))
    assert len(sorted_counts) == 11
    assert sorted_counts[0]["char"] == "t"
    assert sorted_counts[0]["count"] == 5
    assert sorted_counts[-1]["count"] == 1
