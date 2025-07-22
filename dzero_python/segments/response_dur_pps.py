"""Response DUR/PPS segment (24) for NCPDP D.0"""

from .base import BaseSegment

class ResponseDurPps(BaseSegment):
    """Response DUR/PPS segment - Contains response drug utilization review information"""
    
    @classmethod
    def field_id_to_symbol(cls):
        """Response DUR/PPS segment field mappings from Ruby implementation"""
        base_fields = super().field_id_to_symbol()
        response_dur_pps_fields = {
            'J6': 'dur_pps_response_code_counter',
            'E4': 'reason_for_service_code',
            'FS': 'clinical_significance_code',
            'FT': 'other_pharmacy_indicator',
            'FV': 'quantity_of_previous_fill',
            'FU': 'previous_date_of_fill',
            'FW': 'database_indicator',
            'FX': 'other_prescriber_indicator',
            'FY': 'dur_free_text_message',
            'NS': 'dur_additional_text',
        }
        return {**base_fields, **response_dur_pps_fields}

# Register the segment
BaseSegment.register_segment(ResponseDurPps, '24')
