
from hypothesis import given, strategies as st
from shopping_cart import cart_total, promo_percent, delivery_zone


@given(st.one_of(st.text(), st.none(), st.integers()))
def test_cart_total_no_crash(cart):
    cart_total(cart)


@given(st.one_of(st.text(), st.none(), st.integers()))
def test_promo_percent_no_crash(code):
    promo_percent(code)


@given(st.one_of(st.text(), st.none(), st.integers()))
def test_delivery_zone_no_crash(pincode):
    delivery_zone(pincode)
