
import pytest

from shopping_cart import item_total, cart_discount, shipping_fee


# item_total tests

def test_food_category():
    assert item_total("food", 100, 1) == 105


def test_electronics_category():
    assert item_total("electronics", 100, 1) == 118


def test_clothing_category():
    assert item_total("clothing", 100, 1) == 112


def test_bulk_quantity_discount():
    assert item_total("food", 100, 10) == 945


def test_unknown_category():
    with pytest.raises(ValueError, match="unknown category"):
        item_total("toys", 100, 1)


def test_negative_price():
    with pytest.raises(ValueError, match="invalid price or quantity"):
        item_total("food", -1, 1)


def test_zero_quantity():
    with pytest.raises(ValueError, match="invalid price or quantity"):
        item_total("food", 100, 0)


# cart_discount tests

def test_high_cart_value():
    assert cart_discount(5000, False, "NONE") == 500


def test_medium_cart_value():
    assert cart_discount(2000, False, "NONE") == 200


def test_low_cart_value():
    assert cart_discount(1999, False, "NONE") == 0


def test_prime_discount():
    assert cart_discount(500, True, "NONE") == 100


def test_coupon_applied():
    assert cart_discount(1000, False, "FLAT10") == 100


def test_coupon_below_threshold():
    assert cart_discount(999, False, "FLAT10") == 0


def test_other_coupon():
    assert cart_discount(1500, False, "SAVE10") == 0


# shipping_fee tests

def test_prime_standard_shipping():
    assert shipping_fee(100, True, False) == 0


def test_non_prime_free_shipping_threshold():
    assert shipping_fee(500, False, False) == 0


def test_non_prime_paid_shipping():
    assert shipping_fee(499, False, False) == 40


def test_non_prime_express_shipping():
    assert shipping_fee(100, False, True) == 140


def test_prime_express_shipping():
    assert shipping_fee(100, True, True) == 50


def test_high_value_express_shipping():
    assert shipping_fee(1000, False, True) == 100
