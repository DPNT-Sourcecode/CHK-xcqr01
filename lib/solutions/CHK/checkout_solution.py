from collections import Counter

class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        prices = {
        'A': 50, 'B': 30, 'C': 20, 'D': 15,
        'E': 40, 'F': 10, 'G': 20, 'H': 10,
        'I': 35, 'J': 60, 'K': 70, 'L': 90,
        'M': 15, 'N': 40, 'O': 10, 'P': 50,
        'Q': 30, 'R': 50, 'S': 20, 'T': 20,
        'U': 40, 'V': 50, 'W': 20, 'X': 17,
        'Y': 20, 'Z': 21
        }

        discounts = {
        'A': [(5, 200), (3, 130)],
        'B': [(2, 45)],
        'H': [(10, 80), (5, 45)],
        'K': [(2, 120)],
        'P': [(5, 200)],
        'Q' : [(3, 80)],
        'V': [(3, 130), (2, 90)]
        }

        grouped_discount_skus = ['S', 'T', 'X', 'Y', 'Z']
        group_offer_prices = 45
        group_offer_count = 3

        total = 0

        for sku in skus:
            if sku not in prices:
                return -1

        counts = Counter(skus)

        # handle discounts for E -> 2E get one B free
        free_bs = counts.get('E', 0) // 2
        counts['B'] = max(0, counts.get('B', 0) - free_bs)

        # handle discounts for N -> 3N get one M free
        free_ms = counts.get('N', 0) // 3
        counts['M'] = max(0, counts.get('M', 0) - free_ms)

        # handle discounts for R -> 3Rs get one Q free
        free_qs = counts.get('R', 0) // 3
        counts['Q'] = max(0, counts.get('Q', 0) - free_qs)

        # handle discounts for F -> 2F get one F free
        count_f = counts.get('F', 0)
        free_fs = count_f // 3
        count_f_to_pay = count_f - free_fs
        counts['F'] = count_f_to_pay

        # handle discounts for U -> 3U get one U free
        count_u = counts.get('U', 0)
        free_us = count_u // 4
        count_u_to_pay = count_u - free_us
        counts['U'] = count_u_to_pay


        # handle discounts for grouped items S, T, X, Y, Z
        grouped_items = []
        for sku in grouped_discount_skus:
            count =

        for sku, price in prices.items():
            count = counts.get(sku, 0)

            if sku in discounts:
                for offer_qty, offer_price in sorted(discounts[sku], key=lambda x : x[0], reverse=True):
                    if count >= offer_qty:
                        num_offers = count // offer_qty
                        total += num_offers * offer_price
                        count %= offer_qty
                total += count * price
            else:
                total += count * price

        return total
