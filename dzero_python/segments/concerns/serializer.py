"""Serializer mixin for segment serialization functionality"""

class SerializerMixin:
    """Mixin providing serialization functionality for segments"""
    
    def to_s(self):
        """
        Serialize segment to NCPDP D.0 string format
        
        Returns:
            str: Formatted segment string
        """
        # Join field ID and value pairs with field separators
        field_strings = [f"{field_id}{value}" for field_id, value in self.hash.items()]
        string = "\x1C".join(field_strings)
        
        # Add field separator at start and segment separator at end
        return "\x1C" + string + "\x1E"
    
    def to_json(self, readable=False, **options):
        """
        Serialize segment to JSON/dictionary format
        
        Args:
            readable (bool): If True, use human-readable field names instead of codes
            **options: Additional options (for compatibility)
            
        Returns:
            dict: Dictionary representation of segment
        """
        result = {}
        
        for field_id, value in self.hash.items():
            if readable:
                # Convert field ID to readable symbol name
                readable_key = self.__class__.get_symbol_by_field(field_id)
                key = readable_key if readable_key else field_id
            else:
                key = field_id
                
            result[key] = value
            
        return result
