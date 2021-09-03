#!/usr/bin/env python3
import re
import subprocess
import random


def load_servers(fname="protonvpn.txt"):
    with open(fname, "r") as f:
        return [re.match("([\w-]+#\d+)", line).group(0) for line in f.readlines()]


def protonvpn_cli_connect():
    server = random.choice(load_servers())
    subprocess.run(["protonvpn-cli", "c", server])


if __name__ == "__main__":
    protonvpn_cli_connect()
