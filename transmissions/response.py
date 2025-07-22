"""Response transmission class"""

from .base import BaseTransmission

class Response(BaseTransmission):
    """NCPDP D.0 Response transmission"""
    
    @classmethod  
    def header_schema(cls):
        """
        Header schema for response messages
        
        Returns:
            dict: Field names to field sizes
        """
        return {
            'version': 2,
            'transaction_code': 2, 
            'transaction_count': 1,
            'header_response_status': 1,
            'service_provider_id_qualifier': 2,
            'service_provider_id': 15,
            'date_of_service': 8
        }
