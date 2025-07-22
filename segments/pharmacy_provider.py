"""Pharmacy Provider segment (02) for NCPDP D.0"""

from .base import BaseSegment

class PharmacyProvider(BaseSegment):
    """Pharmacy Provider segment - Contains pharmacy provider information"""
    
    @classmethod
    def field_id_to_symbol(cls):
        """Pharmacy Provider segment field mappings from Ruby implementation"""
        base_fields = super().field_id_to_symbol()
        pharmacy_provider_fields = {
            'EY': 'provider_id_qualifier',
            'E9': 'provider_id',
        }
        return {**base_fields, **pharmacy_provider_fields}

# Register the segment
BaseSegment.register_segment(PharmacyProvider, '02')
