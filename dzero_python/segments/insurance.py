"""Insurance segment (04) for NCPDP D.0"""

from .base import BaseSegment

class Insurance(BaseSegment):
    """Insurance segment - Contains insurance information"""
    
    @classmethod
    def field_id_to_symbol(cls):
        """Insurance segment field mappings from Ruby implementation"""
        base_fields = super().field_id_to_symbol()
        insurance_fields = {
            'C2': 'cardholder_id',
            'CC': 'cardholder_first_name',
            'CD': 'cardholder_last_name',
            'CE': 'home_plan',
            'FO': 'plan_id',
            'C9': 'eligibility_clarification_code',
            'C1': 'group_id',
            'C3': 'person_code',
            'C6': 'patient_relationship_code',
            'MG': 'other_payer_bin_number',
            'MH': 'other_payer_processor_control_number',
            'NU': 'other_payer_cardholder_id',
            'MJ': 'other_payer_group_id',
            '2A': 'medigap_id',
            '2B': 'medicaid_indicator',
            '2D': 'provider_accept_assignment_indicator',
            'G2': 'cms_part_d_defined_qualified_facility',
            'N5': 'medicaid_id_number',
            'N6': 'medicaid_agency_number',
        }
        return {**base_fields, **insurance_fields}

# Register the segment
BaseSegment.register_segment(Insurance, '04')
