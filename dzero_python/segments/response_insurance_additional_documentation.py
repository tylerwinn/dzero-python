"""Response Insurance Additional Documentation segment (27) for NCPDP D.0"""

from .base import BaseSegment

class ResponseInsuranceAdditionalDocumentation(BaseSegment):
    """Response Insurance Additional Documentation segment - Contains response insurance additional documentation information"""
    
    @classmethod
    def field_id_to_symbol(cls):
        """Response Insurance Additional Documentation segment field mappings from Ruby implementation"""
        base_fields = super().field_id_to_symbol()
        response_insurance_additional_documentation_fields = {
            'UR': 'medicare_part_d_coverage_code',
            'UQ': 'cms_low_income_cost_sharing_lics_level',
            'U1': 'contract_number',
            'FF': 'formulary_id',
            'U6': 'benefit_id',
            'US': 'next_medicare_part_d_effective_date',
            'UT': 'next_medicare_part_d_termination_date',
        }
        return {**base_fields, **response_insurance_additional_documentation_fields}

# Register the segment
BaseSegment.register_segment(ResponseInsuranceAdditionalDocumentation, '27')
