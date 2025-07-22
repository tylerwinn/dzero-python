"""Clinical segment (13) for NCPDP D.0"""

from .base import BaseSegment

class Clinical(BaseSegment):
    """Clinical segment - Contains clinical information"""
    
    @classmethod
    def field_id_to_symbol(cls):
        """Clinical segment field mappings from Ruby implementation"""
        base_fields = super().field_id_to_symbol()
        clinical_fields = {
            'VE': 'diagnosis_code_count',
            'WE': 'diagnosis_code_qualifier',
            'DO': 'diagnosis_code',
            'XE': 'clinical_information_counter',
            'ZE': 'measurement_date',
            'H1': 'measurement_time',
            'H2': 'measurement_dimension',
            'H3': 'measurement_unit',
            'H4': 'measurement_value',
        }
        return {**base_fields, **clinical_fields}

# Register the segment
BaseSegment.register_segment(Clinical, '13')
