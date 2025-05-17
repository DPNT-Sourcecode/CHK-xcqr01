from collections import Counter

class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        prices = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
        }

        discounts = {
        'A': (3, 130),
        'B': (2, 45),}

        for sku in skus:
            if sku not in prices:
                return -1

        counts = Counter(skus)

        total = 0

        count_a = counts.get('A', 0)
        if count_a >= 3:
            offer_qty, offer_price = discounts['A']
            total += (count_a // offer_qty) * offer_price + ()
#             total += (count_a, 130)
#             count_a = count_a % 3


