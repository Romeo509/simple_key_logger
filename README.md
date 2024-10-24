# Simple Key Logger

## Description
**Simple Key Logger** is a basic Python-based keylogger designed for educational and personal use. It captures keystrokes, stores them in a text file, and logs special keys like `Enter`, `Backspace`, and `Escape` as well. Additionally, if the user is inactive for 30 seconds, it automatically starts logging from a new line once they type again.

This keylogger was built with the `pynput` library and emphasizes responsible usage.

## Features
- Records all keystrokes, including special characters (e.g., `[enter]`, `[back]`, `[esc]`).
- Preserves case sensitivity (capital and lowercase letters).
- Moves to the next line if the user is inactive for more than 30 seconds.
- Ignores arrow keys (up, down, left, right).
- Stores logs in a plain text file (`keylog.txt`) in the same directory.

## Installation

To install the necessary dependencies, follow these steps:

```bash
pip install pynput
