#!/usr/bin/python3
"""Reads from standard input and computes metrics.

After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""
import sys
import signal


def print_metrics(total_size, status_codes):
    """Prints metrics based on the computed statistics.

    Args:
        total_size (int): Total file size.
        status_codes (dict): Dictionary containing
        the count of each status code.
    """
    print("File size: {:d}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{:d}: {:d}".format(code, status_codes[code]))


def signal_handler(sig, frame):
    """Signal handler for KeyboardInterrupt (CTRL + C).

    Args:
        sig: Signal number
        frame: Current stack frame
    """
    print_metrics(total_size, status_codes)
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

line_count = 0
total_size = 0
status_codes = {}

try:
    for line in sys.stdin:
        tokens = line.split()
        if len(tokens) >= 9:
            status_code = int(tokens[-2])
            file_size = int(tokens[-1])
            total_size += file_size

            if status_code in status_codes:
                status_codes[status_code] += 1
            else:
                status_codes[status_code] = 1

        line_count += 1

        if line_count % 10 == 0:
            print_metrics(total_size, status_codes)

except KeyboardInterrupt:
    print_metrics(total_size, status_codes)
    sys.exit(0)
