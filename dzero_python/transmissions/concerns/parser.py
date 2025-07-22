"""Parser concern for transmission parsing"""

from ...utils.fixed_width import parse_fixed_width

class ParserMixin:
    """Mixin providing parsing functionality for transmissions"""
    
    @classmethod
    def parse(cls, string):
        """
        Parse transmission from string
        
        Args:
            string (str): Raw transmission string
            
        Returns:
            Transmission instance
        """
        # Make a copy to avoid modifying the original
        string = string[:]
        
        # Parse fixed-width header
        header_length = sum(cls.header_schema().values())
        header_string = string[:header_length]
        header = parse_fixed_width(cls.header_schema(), header_string)
        
        # Remove header from string
        remaining_string = string[header_length:]
        
        # Split into transaction groups by group separator
        raw_groups = remaining_string.split("\x1D")  # GROUP_SEPARATOR
        
        # First group is transmission group (no separator prefix)
        raw_transmission_group = raw_groups[0] if raw_groups else ""
        
        # Import here to avoid circular imports
        from ..groups import TransmissionGroup, TransactionGroup
        transmission_group = TransmissionGroup.parse(raw_transmission_group)
        
        # Remaining groups are transaction groups
        transaction_groups = []
        for raw_group in raw_groups[1:]:
            if raw_group.strip():  # Skip empty groups
                transaction_groups.append(TransactionGroup.parse(raw_group))
        
        return cls(
            header=header,
            transmission_group=transmission_group,
            transaction_groups=transaction_groups
        )
