import sys

def main():
    price = float(sys.argv[1])

    if len(sys.argv) == 2:
        more5 = (price * 105) / 100
        more10 = (price * 110) / 100
        more15 = (price * 115) / 100
        more20 = (price * 120) / 100
        less5 = (price * 95) / 100
        less10 = (price * 90) / 100
        less15 = (price * 85) / 100
        less20 = (price * 80) / 100

        print(
            '+5% -', str(more5), '\n' \
            + '+10% -', str(more10), '\n' \
            + '+15% -', str(more15), '\n' \
            + '+20% -', str(more20), '\n' \
            + '-5% -', str(less5), '\n' \
            + '-10% -', str(less10), '\n' \
            + '-15% -', str(less15), '\n' \
            + '-20% -', str(less20), '\n'
        )

    if len(sys.argv) == 3:
        secondPrice = float(sys.argv[2])
        result = 100 - ((secondPrice * 100) / price)
        print('Difference between', price, 'and', secondPrice, 'is', result, '%')

main()