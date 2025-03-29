"""Python interface to IGRF (International Geomagnetic Reference Field)."""

import numpy as np
from .igrf_module import *  # Import all functions from the compiled module

# You can add more user-friendly wrapper functions here
def calculate_magnetic_field(lat, lon, alt, date):
    """
    Calculate magnetic field components at a given location and date.

    Parameters:
    -----------
    lat : float
        Latitude in degrees (positive north)
    lon : float
        Longitude in degrees (positive east)
    alt : float
        Altitude in kilometers above sea level
    date : float
        Decimal year (e.g., 2023.5 for July 1, 2023)

    Returns:
    --------
    dict
        Dictionary containing magnetic field components
    """
    # This is just an example - modify to match your actual Fortran function
    # Assuming your Fortran module has a function called 'igrf'
    x, y, z, f = igrf(date, alt, lat, lon)

    return {
        'north': x,
        'east': y,
        'down': z,
        'total': f
    }

__version__ = '0.1.0'