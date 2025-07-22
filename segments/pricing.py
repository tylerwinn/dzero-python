"""Pricing segment (11) for NCPDP D.0"""

from .base import BaseSegment

class Pricing(BaseSegment):
    """Pricing segment - Contains pricing information"""
    
    @classmethod
    def field_id_to_symbol(cls):
        """Pricing segment field mappings from Ruby implementation"""
        base_fields = super().field_id_to_symbol()
        pricing_fields = {
            'D9': 'ingredient_cost_submitted',
            'DC': 'dispensing_fee_submitted',
            'BE': 'professional_service_fee_submitted',
            'DX': 'patient_paid_amount_submitted',
            'E3': 'incentive_amount_submitted',
            'H7': 'other_amount_claimed_submitted_count',
            'H8': 'other_amount_claimed_submitted_qualifier',
            'H9': 'other_amount_claimed_submitted',
            'HA': 'flat_sales_tax_amount_submitted',
            'GE': 'percentage_sales_tax_amount_submitted',
            'HE': 'percentage_sales_tax_rate_submitted',
            'JE': 'percentage_sales_tax_basis_submitted',
            'DQ': 'usual_and_customary_charge',
            'DU': 'gross_amount_due',
            'DN': 'basis_of_cost_determination',
            'N3': 'medicaid_paid_amount',
        }
        return {**base_fields, **pricing_fields}

# Register the segment
BaseSegment.register_segment(Pricing, '11')
