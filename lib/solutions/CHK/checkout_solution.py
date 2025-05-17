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
        if count_a > 0:
            offer_qty, offer_price = discounts['A']
            total += (count_a // offer_qty) * offer_price + (count_a % offer_qty) * prices['A']

        count_b = counts.get('B', 0)
        if count_b > 0:
            offer_qty, offer_price = discounts['A']
            total += (count_b // offer_qty) * offer_price + (count_b % offer_qty) * prices['B']

        count_c = counts.get('C', 0)
        if count_c > 0:
            total += count_c * prices['C']

        count_d = counts.get('D', 0)
        if count_d > 0:
            total += count_d * prices['D']

        return total



