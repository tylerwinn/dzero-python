"""Compound segment (10) for NCPDP D.0"""

from .base import BaseSegment

class Compound(BaseSegment):
    """Compound segment - Contains compound medication information"""
    
    @classmethod
    def field_id_to_symbol(cls):
        """Compound segment field mappings from Ruby implementation"""
        base_fields = super().field_id_to_symbol()
        compound_fields = {
            'EF': 'compound_dosage_form_description_code',
            'EG': 'compound_dispensing_unit_form_indicator',
            'EC': 'compound_ingredient_component_count',
            'RE': 'compound_product_id_qualifier',
            'TE': 'compound_product_id',
            'ED': 'compound_ingredient_quantity',
            'EE': 'compound_ingredient_drug_cost',
            'UE': 'compound_ingredient_basis_of_cost_determination',
            '2G': 'compound_ingredient_modifier_code_count',
            '2H': 'compound_ingredient_modifier_code',
        }
        return {**base_fields, **compound_fields}

# Register the segment
BaseSegment.register_segment(Compound, '10')
