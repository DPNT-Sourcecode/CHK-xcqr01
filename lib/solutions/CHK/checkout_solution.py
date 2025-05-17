
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

