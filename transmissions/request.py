"""Request transmission class"""

from .base import BaseTransmission

class Request(BaseTransmission):
    """NCPDP D.0 Request transmission"""
    
    @classmethod
    def header_schema(cls):
        """
        Header schema for request messages
        
        Returns:
            dict: Field names to field sizes
        """
        return {
            'bin_number': 6,
            'version': 2, 
            'transaction_code': 2,
            'processor_control_number': 10,
            'transaction_count': 1,
            'service_provider_id_qualifier': 2,
            'service_provider_id': 15,
            'date_of_service': 8,
            'software': 10
        }
