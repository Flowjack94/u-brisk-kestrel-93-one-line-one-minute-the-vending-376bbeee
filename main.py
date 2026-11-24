"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes a single pickup line, spoken by a vending machine to a passing
human, to /output/entry.txt and prints it to stdout.
"""

from pathlib import Path

ENTRY = "Hey, gorgeous \u2014 I hum all day, but my coils only spin for you. Press B4 and I will drop something sweet. Exact change not required."


def validate_entry(text: str) -> str:
    """Validate the entry line: single line, 1-200 chars, no control chars."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    for ch in text:
        code = ord(ch)
        if code < 0x20 or code == 0x7F or 0x80 <= code <= 0x9F:
            raise ValueError("entry must not contain control characters (incl. C1)")
        if code == 0xFFFD:
            raise ValueError("entry must not contain U+FFFD replacement characters")
        if 0xD800 <= code <= 0xDFFF:
            raise ValueError("entry must not contain lone surrogates")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return text


def main() -> None:
    line = validate_entry(ENTRY)
    print(line)
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
