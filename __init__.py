"""
DZero Python - NCPDP Telecommunications Standard Version D.0 Message Parser and Serializer

A robust and easy-to-use Python implementation of the NCPDP D.0 standard for parsing
and serializing pharmacy telecommunications messages.

Features:
- Complete field mapping for all 26 D.0 Segment types
- Parse D.0 Requests or Responses with ease
- Build D.0 Requests or Responses programmatically  
- Supports multiple transaction groups
- Serialize messages to JSON and back to D.0 format
"""

from .constants import Constants
from . import segments
from .transmissions import Request, Response
from . import utils

__version__ = "1.0.0"
__all__ = [
    "Constants",
    "Request", 
    "Response",
    "segments",
    "utils"
]
