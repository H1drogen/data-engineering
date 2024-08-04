from src.seconds_to_time_string import seconds_to_time_string


def test_sentence_to_time_returns_string_with_time_in_seconds_singular():
    seconds = 1
    assert seconds_to_time_string(seconds) == "1 second"

def test_sentence_to_time_returns_string_with_time_in_seconds_pluralised():
    seconds = 2
    assert seconds_to_time_string(seconds) == "2 seconds"

def test_sentence_to_time_returns_string_with_time_in_minutes():
    seconds = 60
    assert seconds_to_time_string(seconds) == "1 minute"

def test_sentence_to_time_returns_string_with_time_in_minutes_and_seconds():
    seconds = 61
    assert seconds_to_time_string(seconds) == "1 minute 1 second"

def test_sentence_to_time_returns_string_with_time_in_minutes_and_seconds_pluralised():
    seconds = 122
    assert seconds_to_time_string(seconds) == "2 minutes 2 seconds"

def test_sentence_to_time_returns_string_with_time_in_hours():
    seconds = 3600
    assert seconds_to_time_string(seconds) == "1 hour"

def test_sentence_to_time_returns_string_with_time_in_hours_minutes_and_seconds():
    seconds = 3661
    assert seconds_to_time_string(seconds) == "1 hour 1 minute 1 second"

def test_sentence_to_time_returns_string_with_time_in_hours_minutes_and_seconds_pluralised():
    seconds = (2 * 3600) + (2 * 60) + 2
    assert seconds_to_time_string(seconds) == "2 hours 2 minutes 2 seconds"

def test_sentence_to_time_returns_string_with_time_in_days():
    seconds = 86400
    assert seconds_to_time_string(seconds) == "1 day"

def test_sentence_to_time_returns_string_with_time_in_days_hours_minutes_and_seconds():
    seconds = 90061
    assert seconds_to_time_string(seconds) == "1 day 1 hour 1 minute 1 second"




