import os

ENTRY = "My fridge locks at midnight, treating the leftovers like residents and me like a trespasser."


def write_entry():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8", newline="") as entry_file:
        entry_file.write(ENTRY)


def main():
    write_entry()


if __name__ == "__main__":
    main()
