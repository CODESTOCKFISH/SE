"""Tests focused on achieving high statement/line coverage for movie_tickets.py."""
import pytest

from movie_tickets import ticket_price, group_discount, snack_combo


def test_ticket_price_regular_afternoon_weekday():
    assert ticket_price("regular", 25, 15, False) == 150


def test_ticket_price_unknown_seat():
    with pytest.raises(ValueError, match="unknown seat"):
        ticket_price("balcony", 25, 15, False)


def test_ticket_price_invalid_time_below_range():
    with pytest.raises(ValueError, match="invalid show time"):
        ticket_price("regular", 25, -1, False)


def test_ticket_price_invalid_time_above_range():
    with pytest.raises(ValueError, match="invalid show time"):
        ticket_price("regular", 25, 24, False)


def test_ticket_price_morning_child_weekend():
    assert ticket_price("premium", 2, 10, True) == 0


def test_ticket_price_evening_senior_weekend():
    # (400 + 30 + 40) // 2 = 235
    assert ticket_price("recliner", 60, 20, True) == 235


def test_ticket_price_child_age_boundary():
    assert ticket_price("regular", 3, 14, False) == 75


def test_ticket_price_young_customer_discount():
    assert ticket_price("premium", 12, 14, False) == 125


def test_group_discount_invalid_ticket_count():
    with pytest.raises(ValueError, match="no tickets"):
        group_discount(0, False)


def test_group_discount_large_student_group():
    assert group_discount(10, True) == 20


def test_group_discount_medium_non_student_group():
    assert group_discount(5, False) == 10


def test_group_discount_small_student_group_no_discount():
    assert group_discount(2, True) == 0


def test_snack_combo_small_without_coupon():
    assert snack_combo("small", False) == 120


def test_snack_combo_medium_with_coupon():
    assert snack_combo("medium", True) == 130


def test_snack_combo_large_without_coupon():
    assert snack_combo("large", False) == 250
