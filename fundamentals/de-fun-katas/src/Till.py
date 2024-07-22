def till_addition(till):
    denominations = {
        '1p': 0.01,
        '2p': 0.02,
        '5p': 0.05,
        '10p': 0.10,
        '20p': 0.20,
        '50p': 0.50,
        '£1': 1.00,
        '£2': 2.00,
        '£5': 5.00,
        '£10': 10.00,
        '£20': 20.00,
        '£50': 50.00
    }

    total = 0
    for denomination, quantity in till.items():
        total += quantity * denominations[denomination]
    return f"£{total}"

till = {
    '1p': 100,
    '2p': 50,
    '5p': 20,
    '10p': 10,
    '20p': 5,
    '50p': 2,
    '£1': 1,
    '£2': 0,
    '£5': 0,
    '£10': 0,
    '£20': 0,
    '£50': 0
}

print(till_addition(till))