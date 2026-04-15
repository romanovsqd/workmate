import argparse


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--files", type=str, nargs="+", required=True)
    parser.add_argument("--report", type=str, required=True)
    args = parser.parse_args()


if __name__ == "__main__":
    main()
