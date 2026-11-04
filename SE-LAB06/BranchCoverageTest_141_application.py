"""Tests designed to exercise both outcomes of each decision branch."""
import pytest

from movie_tickets import ticket_price, group_discount, snack_combo


# ticket_price: valid/invalid seat and both invalid-time boundaries.
def test_ticket_price_invalid_seat_branch():
    with pytest.raises(ValueError, match="unknown seat"):
        ticket_price("vip", 30, 15, False)


def test_ticket_price_valid_seat_branch():
    assert ticket_price("regular", 30, 15, False) == 150


def test_ticket_price_time_below_zero_branch():
    with pytest.raises(ValueError, match="invalid show time"):
        ticket_price("regular", 30, -1, False)


def test_ticket_price_time_above_23_branch():
    with pytest.raises(ValueError, match="invalid show time"):
        ticket_price("regular", 30, 24, False)


def test_ticket_price_valid_time_branch():
    assert ticket_price("regular", 30, 15, False) == 150


# show_hour < 12: true and false; show_hour >= 18: true and false.
def test_ticket_price_morning_branch():
    assert ticket_price("regular", 30, 11, False) == 100


def test_ticket_price_non_morning_evening_branch():
    assert ticket_price("regular", 30, 12, False) == 150


def test_ticket_price_evening_branch():
    assert ticket_price("regular", 30, 18, False) == 180


def test_ticket_price_non_evening_branch():
    assert ticket_price("regular", 30, 17, False) == 150


# Weekend surcharge: true and false.
def test_ticket_price_weekend_branch():
    assert ticket_price("regular", 30, 15, True) == 190


def test_ticket_price_weekday_branch():
    assert ticket_price("regular", 30, 15, False) == 150


# Age branches: under 3, 3 or older; age <= 12 and age >= 60.
def test_ticket_price_under_three_branch():
    assert ticket_price("regular", 2, 15, False) == 0


def test_ticket_price_age_three_branch():
    assert ticket_price("regular", 3, 15, False) == 75


def test_ticket_price_age_twelve_discount_branch():
    assert ticket_price("regular", 12, 15, False) == 75


def test_ticket_price_age_above_twelve_under_sixty_branch():
    assert ticket_price("regular", 13, 15, False) == 150


def test_ticket_price_age_sixty_discount_branch():
    assert ticket_price("regular", 60, 15, False) == 75


# group_discount: invalid, >=10, >=5, <5, student condition true/false.
def test_group_discount_no_tickets_branch():
    with pytest.raises(ValueError, match="no tickets"):
        group_discount(0, False)


def test_group_discount_ten_or_more_branch():
    assert group_discount(10, False) == 15


def test_group_discount_five_to_nine_branch():
    assert group_discount(5, False) == 10


def test_group_discount_below_five_branch():
    assert group_discount(4, False) == 0


def test_group_discount_student_with_discount_branch():
    assert group_discount(5, True) == 15


def test_group_discount_non_student_branch():
    assert group_discount(5, False) == 10


def test_group_discount_student_without_existing_discount_branch():
    assert group_discount(4, True) == 0


# snack_combo: small, medium, other; coupon true and false.
def test_snack_combo_small_branch():
    assert snack_combo("small", False) == 120


def test_snack_combo_medium_branch():
    assert snack_combo("medium", False) == 180


def test_snack_combo_other_size_branch():
    assert snack_combo("large", False) == 250


def test_snack_combo_coupon_branch():
    assert snack_combo("small", True) == 70


def test_snack_combo_no_coupon_branch():
    assert snack_combo("small", False) == 120
