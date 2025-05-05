# 0x03. Log Parsing

## Description

This project is part of the ALX Software Engineering program and focuses on real-time data stream parsing using Python. The goal is to read and process lines from standard input (stdin), parse log entries, compute relevant metrics, and handle interruptions gracefully.

The script:
- Reads log lines from stdin one by one.
- Extracts status codes and file sizes from each line.
- Aggregates total file size and counts for specific HTTP status codes.
- Prints metrics every 10 lines and upon keyboard interruption (CTRL + C).

## Expected Log Format

Each line of input is expected to follow this format:

