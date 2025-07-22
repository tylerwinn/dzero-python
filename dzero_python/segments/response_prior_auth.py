"""Response Prior Authorization segment (26) for NCPDP D.0"""

from .base import BaseSegment

class ResponsePriorAuth(BaseSegment):
    """Response Prior Authorization segment - Contains response prior authorization information"""
    
    @classmethod
    def field_id_to_symbol(cls):
        """Response Prior Authorization segment field mappings from Ruby implementation"""
        base_fields = super().field_id_to_symbol()
        response_prior_auth_fields = {
            'PR': 'prior_authorization_processed_date',
            'PS': 'prior_authorization_effective_date',
            'PT': 'prior_authorization_expiration_date',
            'RA': 'prior_authorization_quantity',
            'RB': 'prior_authorization_dollars_authorized',
            'PW': 'prior_authorization_number_of_refills_authorized',
            'PX': 'prior_authorization_quantity_accumulated',
            'PY': 'prior_authorization_number_assigned',
        }
        return {**base_fields, **response_prior_auth_fields}

# Register the segment
BaseSegment.register_segment(ResponsePriorAuth, '26')
