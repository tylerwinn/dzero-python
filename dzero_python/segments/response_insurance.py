"""Response Insurance segment (25) for NCPDP D.0"""

from .base import BaseSegment

class ResponseInsurance(BaseSegment):
    """Response Insurance segment - Contains response insurance information"""
    
    @classmethod
    def field_id_to_symbol(cls):
        """Response Insurance segment field mappings from Ruby implementation"""
        base_fields = super().field_id_to_symbol()
        response_insurance_fields = {
            'C1': 'group_id',
            'FO': 'plan_id',
            '2F': 'network_reimbursement_id',
            'J7': 'payer_id_qualifier',
            'J8': 'payer_id',
            'N5': 'medicaid_id_number',
            'N6': 'medicaid_agency_number',
            'C2': 'cardholder_id',
        }
        return {**base_fields, **response_insurance_fields}

# Register the segment
BaseSegment.register_segment(ResponseInsurance, '25')
