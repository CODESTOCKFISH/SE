
def parse_seat(seat):
    if not isinstance(seat, str):
        raise ValueError("Seat number must be a string")

    seat = seat.strip()

    if len(seat) < 2:
        raise ValueError("Invalid seat number")

    if not seat[0].isalpha() or not seat[1:].isdigit():
        raise ValueError("Seat must contain a row letter followed by a number")

    return seat[0].upper(), int(seat[1:])


def total_price(prices_csv):
    if not isinstance(prices_csv, str):
        raise ValueError("Prices must be provided as a string")

    if not prices_csv.strip():
        raise ValueError("Price list cannot be empty")

    try:
        prices = [int(p.strip()) for p in prices_csv.split(',')]
    except ValueError:
        raise ValueError("Prices must contain valid integers")

    return round(sum(prices) * 1.18, 2)


def average_rating(ratings):
    if not isinstance(ratings, str):
        raise ValueError("Ratings must be provided as a string")

    if not ratings.strip():
        raise ValueError("Ratings cannot be empty")

    try:
        values = [int(r) for r in ratings.split()]
    except ValueError:
        raise ValueError("Ratings must contain valid integers")

    return round(sum(values) / len(values), 1)


def main():
    print("==== Running parse_seat ====")
    user_input = input("Enter a seat number (e.g. H12): ")
    result = parse_seat(user_input)
    print("Row and Seat:", result)

    print("\n==== Running total_price ====")
    user_input = input("Enter ticket prices as CSV (e.g. 150,250,400): ")
    result = total_price(user_input)
    print("Total with GST:", result)

    print("\n==== Running average_rating ====")
    user_input = input("Enter ratings separated by spaces (e.g. 4 5 3): ")
    result = average_rating(user_input)
    print("Average Rating:", result)


if __name__ == "__main__":
    main()
