"""Segment methods concern for transmission segment access"""

class SegmentMethodsMixin:
    """Mixin providing segment access methods for transmissions"""
    
    # Define which segments belong at which levels
    TRANSMISSION_LEVEL_SEGMENTS = [
        'patient',
        'insurance', 
        'response_message',
        'response_insurance',
        'response_patient'
    ]
    
    TRANSACTION_LEVEL_SEGMENTS = [
        'pharmacy_provider',
        'prescriber',
        'coord_of_benefits',
        'workers_comp',
        'claim',
        'dur_pps', 
        'coupon',
        'compound',
        'pricing',
        'prior_auth',
        'clinical',
        'additional_documentation',
        'facility',
        'narrative',
        'response_status',
        'response_claim',
        'response_pricing',
        'response_dur_pps',
        'response_prior_auth',
        'response_additional_documentation',
        'response_coord_of_benefits'
    ]
    
    def get_segment(self, segment_class):
        """
        Get segment from transmission or transaction groups
        
        Args:
            segment_class: Segment class to find
            
        Returns:
            Segment instance
        """
        # Look in transmission group first
        for segment in self.transmission_group.segments:
            if isinstance(segment, segment_class):
                return segment
        
        # Look in first transaction group
        if self.transaction_groups:
            for segment in self.transaction_groups[0].segments:
                if isinstance(segment, segment_class):
                    return segment
        
        # Create new segment and add to appropriate group
        new_segment = segment_class()
        self.segments.append(new_segment)
        return new_segment
    
    def sort_segments(self, segments):
        """
        Sort segments into appropriate groups based on type
        
        Args:
            segments (list): List of segments to sort
        """
        for segment in segments:
            segment_symbol = segment.__class__.symbol
            
            if segment_symbol in self.TRANSMISSION_LEVEL_SEGMENTS:
                self.transmission_group.segments.append(segment)
            else:
                # Add to transaction level - ensure we have at least one group
                if not self.transaction_groups:
                    from ..groups import TransactionGroup
                    self.transaction_groups.append(TransactionGroup(segments=[]))
                    
                self.transaction_groups[0].segments.append(segment)
    
    @property
    def segments(self):
        """
        Get all segments from all groups
        
        Returns:
            list: All segments
        """
        all_segments = []
        all_segments.extend(self.transmission_group.segments)
        
        for group in self.transaction_groups:
            all_segments.extend(group.segments)
            
        return [s for s in all_segments if s]  # Filter out None values

    def __getattr__(self, name):
        """
        Dynamic segment access via {segment_symbol}_segment attributes
        
        Args:
            name (str): Attribute name
            
        Returns:
            Segment instance or raises AttributeError  
        """
        if name.endswith('_segment'):
            segment_symbol = name[:-8]  # Remove '_segment' suffix
            
            # Import here to avoid circular import
            from ...segments import BaseSegment
            
            # Find segment class by symbol
            segment_class = BaseSegment.get_klass_by_symbol(segment_symbol)
            if segment_class and segment_class != BaseSegment:
                return self.get_segment(segment_class)
        
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")
