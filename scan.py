#!/usr/bin/env python3

import argparse
import asyncio
from bleak import BleakScanner

async def main(args):
    services = []
    devices = await BleakScanner.discover(
        service_uuids=args.services,
        cb=dict(use_bdaddr=True))
    for d in devices:
        print(f"{d.address} {d.name}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--services",
        metavar="<uuid>",
        nargs="*",
        help="UUIDs of one or more services to filter for",
    )

    args = parser.parse_args()

    asyncio.run(main(args))