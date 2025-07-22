"""Transmission Group - top level transmission segments"""

from .base import BaseGroup

class TransmissionGroup(BaseGroup):
    """Group containing transmission-level segments"""
    
    def to_s(self):
        """
        Serialize transmission group to string
        
        Transmission level segments are not preceded by a group separator
        
        Returns:
            str: Serialized transmission group
        """
        string = "".join(segment.to_s() for segment in self.segments)
        
        # Remove the trailing segment separator, if any
        if string.endswith("\x1E"):
            string = string[:-1]
            
        return string
