#!/usr/bin/env python3

import argparse
import asyncio
from bleak import BleakScanner


class Scan(object):
    def __init__(self, services=None, timeout=5.0):
        self.services = services
        self.timeout = timeout

    async def _discover(self):
        return await BleakScanner.discover(
            timeout=self.timeout,
            service_uuids=self.services)

    # Returns a list of "<address> <name>" strings
    def scan(self):
        devices = asyncio.run(self._discover())
        return ["{} {}".format(d.address, d.name) for d in devices]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--services",
        metavar="<uuid>",
        nargs="*",
        help="UUIDs of one or more services to filter for",
    )

    args = parser.parse_args()

    for line in Scan(args.services).scan():
        print(line)
