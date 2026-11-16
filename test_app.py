import pytest
from coffee_pos import calculate_total, main


def test_regular_customer_order():
    order = [("Americano", 2), ("Latte", 1)]  # 100 + 65 = 165
    result = calculate_total(order, is_member=False)
    assert result["subtotal"] == 165
    assert result["discount"] == 0.0
    assert result["total"] == 176.55


def test_member_discount_order():
    order = [("Mocha", 2)]  # 140 - 10% (14) = 126 + VAT 7% (8.82) = 134.82
    result = calculate_total(order, is_member=True)
    assert result["discount"] == 14.0
    assert result["total"] == 134.82


def test_invalid_menu_raises_error():
    with pytest.raises(KeyError):
        calculate_total([("Espresso", 1)])


def test_empty_order_raises_error():
    with pytest.raises(ValueError):
        calculate_total([])


def test_main_output(capsys):
    main()
    captured = capsys.readouterr()
    assert "SAU Coffee POS Receipt" in captured.out
    