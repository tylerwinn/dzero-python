"""Additional Documentation segment (14) for NCPDP D.0"""

from .base import BaseSegment

class AdditionalDocumentation(BaseSegment):
    """Additional Documentation segment - Contains additional documentation information"""
    
    @classmethod
    def field_id_to_symbol(cls):
        """Additional Documentation segment field mappings from Ruby implementation"""
        base_fields = super().field_id_to_symbol()
        additional_documentation_fields = {
            '2Q': 'additional_documentation_type_id',
            '2V': 'request_period_begin_date',
            '2W': 'request_period_recert_revised_date',
            '2U': 'request_status',
            '2S': 'length_of_need_qualifier',
            '2R': 'length_of_need',
            '2T': 'prescriber_supplier_date_signed',
            '2X': 'supporting_documentation',
            '2Z': 'question_number_letter_count',
            '4B': 'question_number_letter',
            '4D': 'question_percent_response',
            '4G': 'question_date_response',
            '4H': 'question_dollar_amount_response',
            '4J': 'question_numeric_response',
            '4K': 'question_alphanumeric_response',
        }
        return {**base_fields, **additional_documentation_fields}

# Register the segment
BaseSegment.register_segment(AdditionalDocumentation, '14')
