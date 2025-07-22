"""Utility modules for DZero Python"""

from .fixed_width import parse_fixed_width, to_fixed_width
from .rejection_codes import RejectionCodes
from .validator import Validator

FixedWidth = type('FixedWidth', (), {
    'parse_fixed_width': staticmethod(parse_fixed_width),
    'to_fixed_width': staticmethod(to_fixed_width)
})

__all__ = ["FixedWidth", "RejectionCodes", "Validator", "parse_fixed_width", "to_fixed_width"]
