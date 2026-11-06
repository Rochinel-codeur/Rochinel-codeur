#!/usr/bin/env python3
"""Rebuild original RochDev editorial assets from the shared composition system."""
try:
    from .artwork import main
except ImportError:
    from artwork import main

if __name__ == "__main__":
    main()
