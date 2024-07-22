import pytest
from src.part_2_vending_machine import VendingMachine


@pytest.fixture(scope='function')
def machine():
    return VendingMachine()


@pytest.mark.describe('All Vending Machine Methods')
class TestVendingMachine:

    @pytest.mark.it('has valid credit attribute')
    def test_credit(self, machine):
        assert machine.credit == 0

    @pytest.mark.it('has expected stock attributes')
    def test_stock(self, machine):
        assert machine.stock['A'] == {}
        assert machine.stock['B'] == {}
        assert machine.stock['C'] == {}

    @pytest.mark.it('adds credit to initial amount')
    def test_add_credit(self, machine):
        machine.add_credit(75)
        assert machine.credit == 75
        new_machine = VendingMachine()
        new_machine.add_credit(62)
        assert new_machine.credit == 62

    @pytest.mark.it('accumulates credit')
    def test_accumulate_credit(self, machine):
        machine.add_credit(19)
        assert machine.credit == 19
        machine.add_credit(33)
        assert machine.credit == 52

    @pytest.mark.it('validates when there is sufficient credit for an item')
    def test_sufficient_credit(self, machine):
        machine.add_credit(36)
        assert machine.credit_checker(30)

    @pytest.mark.it('validates when there is insufficient credit for an item')
    def test_insufficient_credit(self, machine):
        machine.add_credit(36)
        assert not machine.credit_checker(44)

    def test(self):
        mars_bars = {'name': "mars_bar", 'price': 50, 'quantity': 6}
        sample_machine = VendingMachine()
        sample_machine.add_stock(mars_bars, "A")
        sample_machine.stock
        assert sample_machine.stock == {
          "A": {'name': 'mars_bar', 'price': 50, 'quantity': 6},
          "B": {},
          "C": {}
        }
        assert sample_machine.purchase_item('mars_bar') == 'Insufficient credit!'
        sample_machine.add_credit(100)
        assert sample_machine.purchase_item('mars_bar') == 'mars_bar'