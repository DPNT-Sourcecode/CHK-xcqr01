from collections import Counter

class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        prices = {
        'A': 50, 'B': 30, 'C': 20, 'D': 15,
        'E': 40, 'F': 10, 'G': 20, 'H': 10,
        'I': 35, 'J': 60, 'K': 70, 'L': 90,
        'M': 15, 'N': 40, 'O': 10, 'P': 50,
        'Q': 30, 'R': 50, 'S': 30, 'T': 20,
        'U': 40, 'V': 50, 'W': 20, 'X': 90,
        'Y': 10, 'Z': 50
        }

        discounts = {
        'A': [(5, 200), (3, 130)],
        'B': [(2, 45)],
        'H': [(10, 80), (5, 45)],
        'K': [(2, 150)],
        'P': [(5, 200)],
        'Q' : [(3, 80)],
        'V': [(3, 130), (2, 90)]
        }

        total = 0

        for sku in skus:
            if sku not in prices:
                return -1

        counts = Counter(skus)

        # handle discounts for E -> 2E get one B free
        free_bs = counts.get('E', 0) // 2
        counts['B'] = max(0, counts.get('B', 0) - free_bs)

        # handle discounts for F -> 2F get one F free
        count_f = counts.get('F', 0)
        free_fs = count_f // 3
        count_f_to_pay = count_f - free_fs
        total += count_f_to_pay * prices['F']

        count_a = counts.get('A', 0)
        for offer_qty, offer_price in sorted(discounts['A'], key=lambda x: x[0], reverse=True):
            total += (count_a // offer_qty) * offer_price
            count_a %= offer_qty
        total += count_a * prices['A']

        count_b = counts.get('B', 0)
        for offer_qty, offer_price in discounts['B']:
            total += (count_b // offer_qty) * offer_price
            count_b %= offer_qty
        total += count_b * prices['B']

        count_c = counts.get('C', 0)
        total += count_c * prices['C']

        count_d = counts.get('D', 0)
        total += count_d * prices['D']

        count_e = counts.get('E', 0)
        total += count_e * prices['E']

        return total





