"""Facility segment (15) for NCPDP D.0"""

from .base import BaseSegment

class Facility(BaseSegment):
    """Facility segment - Contains facility information"""
    
    @classmethod
    def field_id_to_symbol(cls):
        """Facility segment field mappings from Ruby implementation"""
        base_fields = super().field_id_to_symbol()
        facility_fields = {
            '8C': 'facility_id',
            '3Q': 'facility_name',
            '3U': 'facility_street_address',
            '5J': 'facility_city_address',
            '3V': 'facility_state_province_address',
            '6D': 'facility_zip_postal_zone',
        }
        return {**base_fields, **facility_fields}

# Register the segment
BaseSegment.register_segment(Facility, '15')
