"""Coupon segment (09) for NCPDP D.0"""

from .base import BaseSegment

class Coupon(BaseSegment):
    """Coupon segment - Contains coupon information"""
    
    @classmethod
    def field_id_to_symbol(cls):
        """Coupon segment field mappings from Ruby implementation"""
        base_fields = super().field_id_to_symbol()
        coupon_fields = {
            'KE': 'coupon_type',
            'ME': 'coupon_number',
            'NE': 'coupon_value_amount',
        }
        return {**base_fields, **coupon_fields}

# Register the segment
BaseSegment.register_segment(Coupon, '09')
