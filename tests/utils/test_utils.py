import os
import uuid

import pytest
from freezegun import freeze_time

from utils.utils import is_it_wednesday, load_quotes


@pytest.fixture
def setup_quote_file():
    temp_path = "/tmp/" + str(uuid.uuid4())
    with open(temp_path, "w") as temp_file:
        temp_file.write("- Text: quote number one\n  Attribution: author\n")
        temp_file.write("- Text: quote number two\n  Attribution: author two\n")
    yield temp_path
    os.remove(temp_path)


def test_load_quotes(setup_quote_file):
    """
    Check that quotes get loaded
    """

    quotes = load_quotes(setup_quote_file)
    expected_list = [
        {"quote": "quote number one", "attribution": "author"},
        {"quote": "quote number two", "attribution": "author two"},
    ]
    assert quotes == expected_list


def test_load_quotes_missing_and_empty_attribution():
    temp_path = "/tmp/" + str(uuid.uuid4())
    try:
        with open(temp_path, "w") as temp_file:
            temp_file.write("- Text: quote with missing attribution\n")
            temp_file.write("- Text: quote with empty attribution\n  Attribution:\n")
            temp_file.write("- Text: quote with attribution\n  Attribution: Someone\n")

        quotes = load_quotes(temp_path)
        assert quotes == [
            {"quote": "quote with missing attribution", "attribution": ""},
            {"quote": "quote with empty attribution", "attribution": ""},
            {"quote": "quote with attribution", "attribution": "Someone"},
        ]
    finally:
        os.remove(temp_path)


@freeze_time("2024-08-21")
def test_is_it_wednesday_positive():
    assert is_it_wednesday() is True


@freeze_time("2024-08-23")
def test_is_it_wednesday_negative():
    assert is_it_wednesday() is False


@freeze_time("2024-08-23")
def test_is_it_wednesday_fake():
    assert is_it_wednesday(fake_wednesday=True) is True


@freeze_time("2024-08-23")
def test_is_it_wednesday_fake_env():
    os.environ["FAKE_WEDNESDAY"] = "something"
    assert is_it_wednesday() is True
