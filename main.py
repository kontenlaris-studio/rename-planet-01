#!/usr/bin/env python3
"""Rename the Planet - make.fun entry.

One line, under 200 characters: a funny new name for a planet of our
solar system, plus the why, in the same breath.
"""
import os

LINE = 'Rename Neptune "The Last Email": 16-hour days, 165-year years, and it still has not replied to the sun since 1846.'
# Why it earns the name: Neptune's year really is ~165 Earth years and it
# was discovered in 1846, so a reply to the sun would take a lifetime.


def main():
    print(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
