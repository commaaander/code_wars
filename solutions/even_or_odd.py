# Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")


def even_or_odd(number):
    return "Odd" if number % 2 else "Even"


if __name__ == "__main__":
    logging.info(even_or_odd(1))
    logging.info(even_or_odd(2))
    logging.info(even_or_odd(-1))
    logging.info(even_or_odd(-2))
    logging.info(even_or_odd(0))
