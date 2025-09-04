import pathlib
from knappy.app import validate_load


def main():
    json = pathlib.Path("./data/items.json").read_text()
    validate_load(json)


if __name__ == "__main__":
    main()
