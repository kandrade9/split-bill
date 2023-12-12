def split_bill(bill, tax, tip):
    """
    Calculates amount after splitting bill.
    :param bill: int
    :param tax: int
    :param tip: int
    :return: int
    """
    tax_amount = bill * (tax * .01)
    bill += tax_amount

    tip_amount = bill * (tip * .01)
    bill += tip_amount

    bill /= 2.0
    return bill

result = split_bill(100, 10, 10)
print(f"Result for each individual after splitting the bill: ${result:.2f}")


