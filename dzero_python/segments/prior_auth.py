"""Prior Authorization segment (12) for NCPDP D.0"""

from .base import BaseSegment

class PriorAuth(BaseSegment):
    """Prior Authorization segment - Contains prior authorization information"""
    
    @classmethod
    def field_id_to_symbol(cls):
        """Prior Authorization segment field mappings from Ruby implementation"""
        base_fields = super().field_id_to_symbol()
        prior_auth_fields = {
            'PA': 'request_type',
            'PB': 'request_period_date_begin',
            'PC': 'request_period_date_end',
            'PD': 'basis_of_request',
            'PE': 'authorized_representative_first_name',
            'PF': 'authorized_rep_last_name',
            'PG': 'authorized_rep_street_address',
            'PH': 'authorized_rep_city',
            'PJ': 'authorized_rep_state_province',
            'PK': 'authorized_rep_zip_postal_code',
            'PY': 'prior_authorization_number_assigned',
            'F3': 'authorization_number',
            'PP': 'prior_authorization_supporting_documentation',
        }
        return {**base_fields, **prior_auth_fields}

# Register the segment
BaseSegment.register_segment(PriorAuth, '12')
