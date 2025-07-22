"""Prescriber segment (03) for NCPDP D.0"""

from .base import BaseSegment

class Prescriber(BaseSegment):
    """Prescriber segment - Contains prescriber information"""
    
    @classmethod
    def field_id_to_symbol(cls):
        """Prescriber segment field mappings from Ruby implementation"""
        base_fields = super().field_id_to_symbol()
        prescriber_fields = {
            'EZ': 'prescriber_id_qualifier',
            'DB': 'prescriber_id',
            'DR': 'prescriber_last_name',
            'PM': 'prescriber_phone_number',
            '2E': 'primary_care_provider_id_qualifier',
            'DL': 'primary_care_provider_id',
            '4E': 'primary_care_provider_last_name',
            '2J': 'prescriber_first_name',
            '2K': 'prescriber_street_address',
            '2M': 'prescriber_city_address',
            '2N': 'prescriber_state_province_address',
            '2P': 'prescriber_zip_postal_zone',
        }
        return {**base_fields, **prescriber_fields}

# Register the segment
BaseSegment.register_segment(Prescriber, '03')
