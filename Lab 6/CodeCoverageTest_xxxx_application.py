
import pytest

from shopping_cart import item_total, cart_discount, shipping_fee


# Tests for item_total()

def test_item_total_food():
    assert item_total("food", 100, 2) == 210


def test_item_total_electronics():
    assert item_total("electronics", 100, 1) == 118


def test_item_total_clothing():
    assert item_total("clothing", 100, 1) == 112


def test_item_total_bulk_discount():
    assert item_total("food", 100, 10) == 945


def test_item_total_unknown_category():
    with pytest.raises(ValueError, match="unknown category"):
        item_total("toys", 100, 1)


def test_item_total_negative_price():
    with pytest.raises(ValueError, match="invalid price or quantity"):
        item_total("food", -10, 1)


def test_item_total_zero_quantity():
    with pytest.raises(ValueError, match="invalid price or quantity"):
        item_total("food", 100, 0)


# Tests for cart_discount()

def test_cart_discount_high_value_prime_coupon():
    assert cart_discount(5000, True, "FLAT10") == 1100


def test_cart_discount_medium_value():
    assert cart_discount(2000, False, "NONE") == 200


def test_cart_discount_low_value():
    assert cart_discount(500, False, "NONE") == 0


def test_cart_discount_prime_member():
    assert cart_discount(500, True, "NONE") == 100


def test_cart_discount_coupon_below_minimum():
    assert cart_discount(500, False, "FLAT10") == 0


def test_cart_discount_coupon_not_matching():
    assert cart_discount(1500, False, "SAVE10") == 0


def test_cart_discount_coupon_applied():
    assert cart_discount(1500, False, "FLAT10") == 150


# Tests for shipping_fee()

def test_shipping_free_for_prime():
    assert shipping_fee(100, True, False) == 0


def test_shipping_free_for_high_cart_value():
    assert shipping_fee(500, False, False) == 0


def test_shipping_fee_for_low_cart_value():
    assert shipping_fee(100, False, False) == 40


def test_express_shipping_non_prime():
    assert shipping_fee(100, False, True) == 140


def test_express_shipping_prime():
    assert shipping_fee(100, True, True) == 50


def test_express_shipping_high_cart_non_prime():
    assert shipping_fee(1000, False, True) == 100
