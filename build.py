#!/usr/bin/env python3
"""
Simple build script that prints the flavor.
Usage: python build.py <flavor>
"""
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python build.py <flavor>")
        sys.exit(1)
    
    flavor = sys.argv[1]
    print(f"Building flavor: {flavor}")

if __name__ == "__main__":
    main()
