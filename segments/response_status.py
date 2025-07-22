"""Response Status segment (21) for NCPDP D.0"""

from .base import BaseSegment

class ResponseStatus(BaseSegment):
    """Response Status segment - Contains response status information"""
    
    @classmethod
    def field_id_to_symbol(cls):
        """Response Status segment field mappings from Ruby implementation"""
        base_fields = super().field_id_to_symbol()
        response_status_fields = {
            'AN': 'response_status',
            'F3': 'authorization_number',
            'FA': 'reject_count',
            'FB': 'reject_code',
            '4F': 'reject_field_occurrence_indicator',
            '5F': 'approved_message_code_count',
            '6F': 'approved_message_code',
            'UF': 'additional_message_information_count',
            'UH': 'additional_message_information_qualifier',
            'FQ': 'additional_message_information',
            'UG': 'additional_message_information_continuity',
            '7F': 'help_desk_phone_number_qualifier',
            '8F': 'help_desk_phone_number',
            'K5': 'transaction_reference_number',
            'A7': 'internal_control_number',
            'MA': 'url',
        }
        return {**base_fields, **response_status_fields}

# Register the segment
BaseSegment.register_segment(ResponseStatus, '21')
