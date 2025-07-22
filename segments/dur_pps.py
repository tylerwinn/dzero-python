"""DUR/PPS segment (08) for NCPDP D.0"""

from .base import BaseSegment

class DurPps(BaseSegment):
    """DUR/PPS segment - Contains drug utilization review and prospective pricing system information"""
    
    @classmethod
    def field_id_to_symbol(cls):
        """DUR/PPS segment field mappings from Ruby implementation"""
        base_fields = super().field_id_to_symbol()
        dur_pps_fields = {
            '7E': 'dur_pps_code_counter',
            'E4': 'reason_for_service_code',
            'E5': 'professional_service_code',
            'E6': 'result_of_service_code',
            '8E': 'dur_pps_level_of_effort',
            'J9': 'dur_co_agent_id_qualifier',
            'H6': 'dur_co_agent_id',
        }
        return {**base_fields, **dur_pps_fields}

# Register the segment
BaseSegment.register_segment(DurPps, '08')
