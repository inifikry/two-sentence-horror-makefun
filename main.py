"""Two-Sentence Horror entry: writes the story to /output/entry.txt."""

OUTPUT_PATH = "/output/entry.txt"

STORY = (
    "My smartwatch has logged my heart rate as zero every night this week, "
    "and each morning the app calls it a sensor error. "
    "Last night it stopped calling it an error."
)


def write_entry():
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(STORY)


def main():
    write_entry()


if __name__ == "__main__":
    main()
