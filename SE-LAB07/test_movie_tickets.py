
from hypothesis import given, strategies as st
from movie_tickets import parse_seat, total_price, average_rating


@given(st.text() | st.none())
def test_parse_seat_no_crash(s):
    try:
        result = parse_seat(s)
    except ValueError:
        return

    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[1], int)


@given(st.text() | st.none())
def test_total_price_no_crash(s):
    try:
        result = total_price(s)
    except ValueError:
        return

    assert isinstance(result, float)


@given(st.text() | st.none())
def test_average_rating_no_crash(s):
    try:
        result = average_rating(s)
    except ValueError:
        return

    assert isinstance(result, float)


def test_valid_inputs():
    assert parse_seat("H12") == ("H", 12)
    assert total_price("150,250,400") == 944.0
    assert average_rating("4 5 3") == 4.0
