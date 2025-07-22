"""Response Patient segment (29) for NCPDP D.0"""

from .base import BaseSegment

class ResponsePatient(BaseSegment):
    """Response Patient segment - Contains response patient information"""
    
    @classmethod
    def field_id_to_symbol(cls):
        """Response Patient segment field mappings from Ruby implementation"""
        base_fields = super().field_id_to_symbol()
        response_patient_fields = {
            'CA': 'patient_first_name',
            'CB': 'patient_last_name',
            'C4': 'date_of_birth',
        }
        return {**base_fields, **response_patient_fields}

# Register the segment
BaseSegment.register_segment(ResponsePatient, '29')
