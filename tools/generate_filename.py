#!/usr/bin/env python
import argparse


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("kata_name", type=str, help="The name of the kata.")
    args = parser.parse_args()

    kata_name = args.kata_name

    print(f"{kata_name.lower().replace(' ', '_')}.py")


if __name__ == "__main__":
    main()
