"""Response Coordination of Benefits segment (28) for NCPDP D.0"""

from .base import BaseSegment

class ResponseCoordOfBenefits(BaseSegment):
    """Response Coordination of Benefits segment - Contains response coordination of benefits information"""
    
    @classmethod
    def field_id_to_symbol(cls):
        """Response Coordination of Benefits segment field mappings from Ruby implementation"""
        base_fields = super().field_id_to_symbol()
        response_coord_of_benefits_fields = {
            'NT': 'other_payer_id_count',
            '5C': 'other_payer_coverage_type',
            '6C': 'other_payer_id_qualifier',
            '7C': 'other_payer_id',
            'MH': 'other_payer_processor_control_number',
            'NU': 'other_payer_cardholder_id',
            'MJ': 'other_payer_group_id',
            'UV': 'other_payer_person_code',
            'UB': 'other_payer_help_desk_phone_number',
            'UW': 'other_payer_patient_relationship_code',
            'UX': 'other_payer_benefit_effective_date',
            'UY': 'other_payer_benefit_termination_date',
        }
        return {**base_fields, **response_coord_of_benefits_fields}

# Register the segment
BaseSegment.register_segment(ResponseCoordOfBenefits, '28')
