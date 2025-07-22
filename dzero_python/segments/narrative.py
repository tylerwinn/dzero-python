"""Narrative segment (16) for NCPDP D.0"""

from .base import BaseSegment

class Narrative(BaseSegment):
    """Narrative segment - Contains narrative information"""
    
    @classmethod
    def field_id_to_symbol(cls):
        """Narrative segment field mappings from Ruby implementation"""
        base_fields = super().field_id_to_symbol()
        narrative_fields = {
            'BM': 'narrative_message',
        }
        return {**base_fields, **narrative_fields}

# Register the segment
BaseSegment.register_segment(Narrative, '16')
