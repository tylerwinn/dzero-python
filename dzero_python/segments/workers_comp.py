"""Workers Compensation segment (06) for NCPDP D.0"""

from .base import BaseSegment

class WorkersComp(BaseSegment):
    """Workers Compensation segment - Contains workers compensation information"""
    
    @classmethod
    def field_id_to_symbol(cls):
        """Workers Compensation segment field mappings from Ruby implementation"""
        base_fields = super().field_id_to_symbol()
        workers_comp_fields = {
            'DY': 'date_of_injury',
            'CF': 'employer_name',
            'CG': 'employer_street_address',
            'CH': 'employer_city_address',
            'CI': 'employer_state_province_address',
            'CJ': 'employer_zip_postal_code',
            'CK': 'employer_phone_number',
            'CL': 'employer_contact_name',
            'CR': 'carrier_id',
            'DZ': 'claim_reference_id',
            'TR': 'billing_entity_type_indicator',
            'TS': 'pay_to_qualifier',
            'TT': 'pay_to_id',
            'TU': 'pay_to_name',
            'TV': 'pay_to_street_address',
            'TW': 'pay_to_city_address',
            'TX': 'pay_to_state_province_address',
            'TY': 'pay_to_zip_postal_zone',
            'TZ': 'generic_equivalent_product_id_qualifier',
            'UA': 'generic_equivalent_product_id',
        }
        return {**base_fields, **workers_comp_fields}

# Register the segment
BaseSegment.register_segment(WorkersComp, '06')
