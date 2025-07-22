"""Response Message segment (20) for NCPDP D.0"""

from .base import BaseSegment

class ResponseMessage(BaseSegment):
    """Response Message segment - Contains response message information"""
    
    @classmethod
    def field_id_to_symbol(cls):
        """Response Message segment field mappings from Ruby implementation"""
        base_fields = super().field_id_to_symbol()
        response_message_fields = {
            'F4': 'message',
        }
        return {**base_fields, **response_message_fields}

# Register the segment
BaseSegment.register_segment(ResponseMessage, '20')
