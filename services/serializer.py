from decimal import Decimal
from typing import Optional, Tuple
from utils.money import encode_overpunch, decode_overpunch
from dataclasses import fields
from utils.string import format
from services.constants import GS, RS, FS
from models.segments import (
    Header,
    Patient,
    Insurance,
    Claim,
    Pharmacy,
    Prescriber,
    Pricing
)

def serialize_transmission_string(
    header: Header,
    patient: Patient,
    insurance: Insurance,
    claim: Claim,
    pharmacy: Pharmacy,
    prescriber: Prescriber,
    pricing: Pricing
) -> str:
    segments = [patient, insurance, claim, pharmacy, prescriber, pricing]
    transmission_string = ""
    for segment in segments:
        segment_string = ""
        sorted_fields = sorted(
            [f for f in fields(segment) if f.name not in ["segment_id", "segment_order"]],
            key=lambda f: f.metadata.get("order", 999)
        )
        for field_info in sorted_fields:
            value = getattr(segment, field_info.name)
            if value is None or value == "":
                continue
            if segment.segment_id == "11" and isinstance(value, Decimal):
                # For pricing segment, encode decimal amounts to overpunch
                value = encode_overpunch(value)
            length = field_info.metadata.get("length", 0)
            field_id = field_info.metadata.get("field_id", "")
            formatted_value = format(value, length)
            segment_string += FS + field_id + formatted_value
        segment_string = FS + "AM" + segment.segment_id + segment_string
        if segment.segment_id == "07":
            transmission_string += GS
        transmission_string += RS + segment_string

    return build_header_string(header) + transmission_string

def deserialize_transmission_string(transmission_string: str) -> Tuple[Header, Patient, Insurance, Claim, Pharmacy, Prescriber, Pricing]:
    """Parse a transmission string and return model objects."""
    
    # Build reverse mappings for each segment class (field_id -> field_name)
    segment_classes = {
        "01": Patient,
        "02": Pharmacy,
        "03": Prescriber,
        "04": Insurance,
        "07": Claim,
        "11": Pricing,
    }
    
    def get_reverse_mapping(cls):
        return {
            f.metadata.get("field_id"): f.name 
            for f in fields(cls) 
            if f.metadata.get("field_id")
        }
    
    # Parse header (fixed-width fields at the start)
    header_field_info = sorted(
        [f for f in fields(Header) if f.name != "segment_order"],
        key=lambda f: f.metadata.get("order", 999)
    )
    
    header_data = {}
    pos = 0
    for field_info in header_field_info:
        length = field_info.metadata.get("length", 0)
        header_data[field_info.name] = transmission_string[pos:pos + length].strip()
        pos += length
    
    header = Header(**header_data)
    
    # Parse segments
    segment_data = transmission_string[pos:]
    raw_segments = segment_data.split(RS)
    
    parsed_segments = {}
    
    for segment in raw_segments:
        if not segment:
            continue
        # Remove GS if present
        segment = segment.lstrip(GS)
        segment_fields = segment.split(FS)
        
        # Find segment ID (AM field)
        segment_id = None
        field_values = {}
        
        for f in segment_fields:
            if not f:
                continue
            if f.startswith("AM"):
                segment_id = f[2:]
            else:
                field_id = f[:2]
                field_value = f[2:].rstrip(GS)  # Strip trailing GS from field values
                field_values[field_id] = field_value
        
        if segment_id and segment_id in segment_classes:
            cls = segment_classes[segment_id]
            reverse_mapping = get_reverse_mapping(cls)
            
            kwargs = {}
            for field_id, value in field_values.items():
                if field_id in reverse_mapping:
                    # Decode overpunch for Pricing segment amount fields
                    if segment_id == "11" and field_id in ["D9", "DC", "DQ", "DU", "E3", "DX"]:
                        kwargs[reverse_mapping[field_id]] = decode_overpunch(value)
                    else:
                        kwargs[reverse_mapping[field_id]] = value
            
            parsed_segments[segment_id] = cls(**kwargs)
    
    return (
        header,
        parsed_segments.get("01", Patient()),
        parsed_segments.get("04", Insurance()),
        parsed_segments.get("07", Claim()),
        parsed_segments.get("02", Pharmacy()),
        parsed_segments.get("03", Prescriber()),
        parsed_segments.get("11", Pricing()),
    )

def build_header_string(header: Header) -> str:
    header_string = ""
    sorted_fields = sorted(
        [f for f in fields(header) if f.name != "segment_order"],
        key=lambda f: f.metadata.get("order", 999)
    )
    for field_info in sorted_fields:
        value = getattr(header, field_info.name)
        length = field_info.metadata.get("length", 0)
        formatted_value = format(value, length, trim=False)
        header_string += formatted_value
    return header_string

def update_transmission_string(
        header: Optional[Header] = None,
        patient: Optional[Patient] = None,
        insurance: Optional[Insurance] = None,
        claim: Optional[Claim] = None,
        pharmacy: Optional[Pharmacy] = None,
        prescriber: Optional[Prescriber] = None,
        pricing: Optional[Pricing] = None,
        transmission_string: str = "") -> str:
    """Update specific segments in an existing transmission string."""
    existing_header, existing_patient, existing_insurance, existing_claim, existing_pharmacy, existing_prescriber, existing_pricing = deserialize_transmission_string(transmission_string)
    
    updated_header = header if header else existing_header
    updated_patient = patient if patient else existing_patient
    updated_insurance = insurance if insurance else existing_insurance
    updated_claim = claim if claim else existing_claim
    updated_pharmacy = pharmacy if pharmacy else existing_pharmacy
    updated_prescriber = prescriber if prescriber else existing_prescriber
    updated_pricing = pricing if pricing else existing_pricing
    
    return serialize_transmission_string(
        updated_header,
        updated_patient,
        updated_insurance,
        updated_claim,
        updated_pharmacy,
        updated_prescriber,
        updated_pricing
    )