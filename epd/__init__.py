"""
Waveshare E-Paper Display Library

A modernized version of the Waveshare e-paper library using python-periphery.
"""

__version__ = "0.1.0"
__author__ = "Waveshare Electronics (original), Modernized fork"

# Import commonly used display classes
try:
    from .epd4in2_V2 import EPD as EPD4in2_V2
    from .epd2in13_V2 import EPD as EPD2in13_V2
    from .epd2in9_V2 import EPD as EPD2in9_V2
    from .epd7in5_V2 import EPD as EPD7in5_V2
except ImportError:
    # Graceful fallback if specific modules aren't available
    pass

__all__ = [
    'EPD4in2_V2',
    'EPD2in13_V2', 
    'EPD2in9_V2',
    'EPD7in5_V2',
]
