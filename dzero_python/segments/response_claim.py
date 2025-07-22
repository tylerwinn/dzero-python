"""Response Claim segment (22) for NCPDP D.0"""

from .base import BaseSegment

class ResponseClaim(BaseSegment):
    """Response Claim segment - Contains response claim information"""
    
    @classmethod
    def field_id_to_symbol(cls):
        """Response Claim segment field mappings from Ruby implementation"""
        base_fields = super().field_id_to_symbol()
        response_claim_fields = {
            'EM': 'prescription_reference_number_qualifier',
            'D2': 'prescription_reference_number',
            '9F': 'preferred_product_count',
            'AP': 'preferred_product_id_qualifier',
            'AR': 'preferred_product_id',
            'AS': 'preferred_product_incentive',
            'AT': 'preferred_product_cost_share_incentive',
            'AU': 'preferred_product_description',
            'N4': 'medicade_icn',
        }
        return {**base_fields, **response_claim_fields}

# Register the segment
BaseSegment.register_segment(ResponseClaim, '22')
