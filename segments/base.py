"""Base class for all NCPDP D.0 segments"""

from .concerns import ParserMixin, SerializerMixin

class BaseSegment(ParserMixin, SerializerMixin):
    """Base class for all NCPDP D.0 segments"""
    
    # Class-level registries for segment management
    segment_id_to_symbol = {}
    segment_id_to_klass = {}
    segment_identifier = None
    symbol = None
    
    @classmethod 
    def register_segment(cls, segment_class, identifier):
        """
        Register a segment class with its identifier
        
        Args:
            segment_class: The segment class to register
            identifier (str): Two-character segment identifier
        """
        segment_class.segment_identifier = identifier
        segment_class.symbol = cls._class_name_to_symbol(segment_class.__name__)
        
        cls.segment_id_to_klass[identifier] = segment_class
        cls.segment_id_to_symbol[identifier] = segment_class.symbol
    
    @classmethod
    def field_id_to_symbol(cls):
        """
        Map field IDs to symbolic names. Override in subclasses.
        
        Returns:
            dict: Mapping of field IDs to symbol names
        """
        return {'AM': 'segment_identification'}
    
    @classmethod
    def get_field_by_symbol(cls, symbol):
        """
        Get field ID by symbol name
        
        Args:
            symbol (str): Symbol name
            
        Returns:
            str: Field ID or None if not found
        """
        mapping = cls.field_id_to_symbol()
        for field_id, sym in mapping.items():
            if sym == symbol:
                return field_id
        return None
    
    @classmethod
    def get_symbol_by_field(cls, field_id):
        """
        Get symbol name by field ID
        
        Args:
            field_id (str): Field ID
            
        Returns:
            str: Symbol name or None if not found
        """
        return cls.field_id_to_symbol().get(field_id)
    
    @classmethod
    def get_klass_by_symbol(cls, symbol):
        """
        Get segment class by symbol name
        
        Args:
            symbol (str): Symbol name
            
        Returns:
            class: Segment class or base class if not found
        """
        for identifier, sym in cls.segment_id_to_symbol.items():
            if sym == symbol:
                return cls.get_klass_by_identifier(identifier)
        return cls
    
    @classmethod
    def get_klass_by_identifier(cls, identifier):
        """
        Get segment class by identifier
        
        Args:
            identifier (str): Two-character segment identifier
            
        Returns:
            class: Segment class or base class if not found
        """
        return cls.segment_id_to_klass.get(identifier, cls)
    
    @classmethod
    def build(cls, initial_hash=None):
        """
        Build a segment instance from initial data
        
        Args:
            initial_hash (dict): Initial field data
            
        Returns:
            Segment instance
        """
        if initial_hash is None:
            initial_hash = {}
            
        # Check if we need to use a specific segment class based on identifier
        given_identifier = initial_hash.get(cls.get_field_by_symbol('segment_identification'))
        if given_identifier:
            segment_klass = cls.segment_id_to_klass.get(given_identifier)
            if segment_klass:
                return segment_klass(initial_hash)
        
        return cls(initial_hash)
    
    @staticmethod
    def _class_name_to_symbol(class_name):
        """
        Convert class name to symbol (snake_case)
        
        Args:
            class_name (str): Class name in CamelCase
            
        Returns:
            str: Symbol name in snake_case
        """
        # Convert CamelCase to snake_case
        import re
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', class_name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
    
    def __init__(self, initial_hash=None):
        """
        Initialize segment instance
        
        Args:
            initial_hash (dict): Initial field data
        """
        self.hash = {}
        
        # Set segment identification if this class has an identifier
        if self.__class__.segment_identifier:
            self['segment_identification'] = self.__class__.segment_identifier
        
        # Merge in initial data
        if initial_hash:
            self.merge(initial_hash)
    
    def __getitem__(self, key):
        """
        Get field value by key (supports both symbols and field IDs)
        
        Args:
            key (str): Field symbol name or ID
            
        Returns:
            str: Field value or None
        """
        if isinstance(key, str) and len(key) > 2:
            # Assume it's a symbol, convert to field ID
            key = self.__class__.get_field_by_symbol(key)
        
        return self.hash.get(key)
    
    def __setitem__(self, key, value):
        """
        Set field value by key (supports both symbols and field IDs)
        
        Args:
            key (str): Field symbol name or ID
            value (str): Field value
        """
        if isinstance(key, str) and len(key) > 2:
            # Assume it's a symbol, convert to field ID
            key = self.__class__.get_field_by_symbol(key)
        
        if key:
            self.hash[key] = str(value) if value is not None else ""
    
    def merge(self, data):
        """
        Merge data into segment
        
        Args:
            data (dict): Data to merge
            
        Returns:
            self: For method chaining
        """
        for key, value in data.items():
            self[key] = value
        return self
