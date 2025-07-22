"""Serializer concern for transmission serialization"""

import json

class SerializerMixin:
    """Mixin providing serialization functionality for transmissions"""
    
    def to_json(self, **options):
        """
        Serialize transmission to JSON/dict
        
        Args:
            **options: Serialization options passed to segments
            
        Returns:
            dict: JSON representation
        """
        return {
            "header": self.header,
            "transmission_group": self.transmission_group.to_json(**options),
            "transaction_groups": [group.to_json(**options) for group in self.transaction_groups]
        }
