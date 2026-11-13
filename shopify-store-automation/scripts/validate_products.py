#!/usr/bin/env python3
"""validate_products.py — validate a Shopify product CSV before import.

Part of the shopify-store-automation Claude skill.
See shopify-store-automation/SKILL.md, Step 3, for the full workflow.

What it does:
  Checks a product-catalog CSV (see templates/product-catalog.csv) and
  reports every problem it finds, one line per problem:
    - required columns are present
    - no row is missing Handle, Title, Variant Price, or Status
    - Handle is unique across rows (duplicates break the import)
    - Variant Price is a number greater than 0
    - Variant Compare At Price, when given, is a number and is higher
      than Variant Price (a compare-at price must be above the price)
    - Variant Inventory Qty, when given, is a whole number of 0 or more
    - Image Src, when given, looks like an http(s) URL
    - Status, when given, is one of: active, draft, archived
    - Published, when given, is TRUE or FALSE

  Prints PASS when there are no problems, FAIL with the problem list
  otherwise. Exits 0 on PASS, 1 on FAIL. Do not import a CSV that fails.

Usage:
  python3 validate_products.py <products.csv>

  Example:
    python3 validate_products.py ../templates/product-catalog.csv

Requirements: Python 3, standard library only. No credentials, no network.
"""

import csv
import sys
from urllib.parse import urlparse

REQUIRED_COLUMNS = [
    "Handle",
    "Title",
    "Variant Price",
    "Status",
]

VALID_STATUSES = {"active", "draft", "archived"}


def is_number(value):
    """True when value parses as a number."""
    try:
        float(value)
        return True
    except (TypeError, ValueError):
        return False


def is_whole_number(value):
    """True when value parses as a whole number of 0 or more."""
    try:
        return int(value) >= 0 and float(value) == int(value)
    except (TypeError, ValueError):
        return False


def looks_like_url(value):
    """True when value looks like an http(s) URL."""
    parsed = urlparse(value.strip())
    return parsed.scheme in ("http", "https") and bool(parsed.netloc)


def validate(path):
    """Validate the CSV at path. Returns a list of problem strings."""
    problems = []

    try:
        with open(path, newline="", encoding="utf-8-sig") as handle:
            reader = csv.DictReader(handle)
            if reader.fieldnames is None:
                return ["File has no header row."]
            columns = [name.strip() for name in reader.fieldnames if name]
            rows = list(reader)
    except FileNotFoundError:
        return ["File not found: %s" % path]
    except (OSError, csv.Error) as exc:
        return ["Could not read %s: %s" % (path, exc)]

    missing = [col for col in REQUIRED_COLUMNS if col not in columns]
    for col in missing:
        problems.append("Missing required column: %s" % col)
    if missing:
        return problems  # Cannot check rows without the required columns.

    if not rows:
        return ["File has a header row but no product rows."]

    seen_handles = {}
    for index, row in enumerate(rows, start=2):  # Row 1 is the header.
        label = "Row %d" % index
        handle = (row.get("Handle") or "").strip()
        title = (row.get("Title") or "").strip()
        price = (row.get("Variant Price") or "").strip()
        compare_at = (row.get("Variant Compare At Price") or "").strip()
        qty = (row.get("Variant Inventory Qty") or "").strip()
        image = (row.get("Image Src") or "").strip()
        status = (row.get("Status") or "").strip()
        published = (row.get("Published") or "").strip()

        if not handle:
            problems.append("%s: Handle is empty." % label)
        elif handle in seen_handles:
            problems.append(
                "%s: duplicate Handle %r (first used on row %d)."
                % (label, handle, seen_handles[handle])
            )
        else:
            seen_handles[handle] = index

        if not title:
            problems.append("%s: Title is empty." % label)

        if not price:
            problems.append("%s: Variant Price is empty." % label)
        elif not is_number(price):
            problems.append(
                "%s: Variant Price %r is not a number." % (label, price)
            )
        elif float(price) <= 0:
            problems.append(
                "%s: Variant Price %r must be greater than 0." % (label, price)
            )

        if compare_at:
            if not is_number(compare_at):
                problems.append(
                    "%s: Variant Compare At Price %r is not a number."
                    % (label, compare_at)
                )
            elif is_number(price) and float(compare_at) <= float(price):
                problems.append(
                    "%s: Variant Compare At Price %r must be higher than "
                    "Variant Price %r." % (label, compare_at, price)
                )

        if qty and not is_whole_number(qty):
            problems.append(
                "%s: Variant Inventory Qty %r must be a whole number of 0 "
                "or more." % (label, qty)
            )

        if image and not looks_like_url(image):
            problems.append(
                "%s: Image Src %r does not look like an http(s) URL."
                % (label, image)
            )

        if status and status.lower() not in VALID_STATUSES:
            problems.append(
                "%s: Status %r must be one of: active, draft, archived."
                % (label, status)
            )

        if published and published.upper() not in ("TRUE", "FALSE"):
            problems.append(
                "%s: Published %r must be TRUE or FALSE." % (label, published)
            )

    return problems


def main(argv):
    if len(argv) != 2:
        print("Usage: %s <products.csv>" % argv[0], file=sys.stderr)
        return 2

    path = argv[1]
    problems = validate(path)

    if problems:
        print("FAIL: %d problem(s) in %s" % (len(problems), path))
        for problem in problems:
            print("  - %s" % problem)
        print("Fix every problem above, then run the validator again.")
        print("Do not import a CSV that fails validation.")
        return 1

    print("PASS: %s is ready to import." % path)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
