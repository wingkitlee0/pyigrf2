"""Python interface to IGRF (International Geomagnetic Reference Field)."""

from ._igrf import igrf14syn  # Import all functions from the compiled module

__all__ = ["igrf14syn"]