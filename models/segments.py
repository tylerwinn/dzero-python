from dataclasses import dataclass, field, fields
from typing import Optional
from decimal import Decimal

@dataclass
class Header:
    segment_order: int = 0
    
    # Fields in order
    bin_number: str = field(default="", metadata={"length": 6, "order": 0})
    version_number: str = field(default="D0", metadata={"length": 2, "order": 1})
    transaction_code: str = field(default="B1", metadata={"length": 2, "order": 2})
    processor_control_number: str = field(default="", metadata={"length": 10, "order": 3})
    transaction_count: str = field(default="1", metadata={"length": 1, "order": 4})
    provider_id_qualifier: str = field(default="01", metadata={"length": 2, "order": 5})
    provider_id: str = field(default="", metadata={"length": 15, "order": 6})
    date_of_service: str = field(default="", metadata={"length": 8, "order": 7})
    software_vendor_id: str = field(default="", metadata={"length": 10, "order": 8})

@dataclass
class Patient:
    segment_id: str = "01"
    segment_order: int = 1
    
    # Fields in order
    date_of_birth: str = field(default="", metadata={"field_id": "C4", "length": 8, "order": 0})
    gender_code: str = field(default="", metadata={"field_id": "C5", "length": 1, "order": 1})
    first_name: str = field(default="", metadata={"field_id": "CA", "length": 12, "order": 2})
    last_name: str = field(default="", metadata={"field_id": "CB", "length": 15, "order": 3})
    street_address: str = field(default="", metadata={"field_id": "CM", "length": 30, "order": 4})
    city: str = field(default="", metadata={"field_id": "CN", "length": 20, "order": 5})
    state: str = field(default="", metadata={"field_id": "CO", "length": 2, "order": 6})
    zip_code: str = field(default="", metadata={"field_id": "CP", "length": 15, "order": 7})
    phone_number: str = field(default="", metadata={"field_id": "CQ", "length": 10, "order": 8})
    residence_code: str = field(default="1", metadata={"field_id": "4X", "length": 1, "order": 9})
    place_of_service: str = field(default="01", metadata={"field_id": "C7", "length": 2, "order": 10})
    pregnancy_indicator: str = field(default="1", metadata={"field_id": "2C", "length": 1, "order": 11})
    
    # Fields without order
    patient_id: str = field(default="", metadata={"field_id": "CY", "length": 20})
    patient_id_qualifier: str = field(default="", metadata={"field_id": "CX", "length": 12})

@dataclass
class Insurance:
    segment_id: str = "04"
    segment_order: int = 2
    
    # Fields in order
    cardholder_id: str = field(default="", metadata={"field_id": "C2", "length": 20, "order": 0})
    cardholder_first_name: str = field(default="", metadata={"field_id": "CC", "length": 12, "order": 1})
    cardholder_last_name: str = field(default="", metadata={"field_id": "CD", "length": 15, "order": 2})
    eligibility_clarification_code: str = field(default="0", metadata={"field_id": "C9", "length": 1, "order": 3})
    group_id: str = field(default="", metadata={"field_id": "C1", "length": 15, "order": 4})
    person_code: str = field(default="", metadata={"field_id": "C3", "length": 2, "order": 5})
    relationship_code: str = field(default="", metadata={"field_id": "C6", "length": 1, "order": 6})
    assignment_indicator: str = field(default="Y", metadata={"field_id": "2D", "length": 1, "order": 7})

@dataclass
class Claim:
    segment_id: str = "07"
    segment_order: int = 3
    
    # Fields in order
    prescription_reference_qualifier: str = field(default="1", metadata={"field_id": "EM", "length": 1, "order": 0})
    prescription_reference_number: str = field(default="", metadata={"field_id": "D2", "length": 20, "order": 1})
    product_service_id_qualifier: str = field(default="03", metadata={"field_id": "E1", "length": 2, "order": 2})
    product_service_id: str = field(default="", metadata={"field_id": "D7", "length": 19, "order": 3})
    quantity_dispensed: str = field(default="", metadata={"field_id": "E7", "length": 10, "order": 4})
    quantity_prescribed: str = field(default="", metadata={"field_id": "ET", "length": 10, "order": 5})
    fill_number: str = field(default="00", metadata={"field_id": "D3", "length": 2, "order": 6})
    days_supply: str = field(default="", metadata={"field_id": "D5", "length": 3, "order": 7})
    compound_code: str = field(default="1", metadata={"field_id": "D6", "length": 1, "order": 8})
    daw_code: str = field(default="0", metadata={"field_id": "D8", "length": 1, "order": 9})
    written_date: str = field(default="", metadata={"field_id": "DE", "length": 8, "order": 10})
    authorized_refills: str = field(default="", metadata={"field_id": "DF", "length": 2, "order": 11})
    submission_clarification_code_count: str = field(default="1", metadata={"field_id": "NX", "length": 1, "order": 12})
    submission_clarification_code: str = field(default="01", metadata={"field_id": "DK", "length": 2, "order": 13})
    other_coverage_code: str = field(default="00", metadata={"field_id": "C8", "length": 2, "order": 14})
    origin_code: str = field(default="3", metadata={"field_id": "DJ", "length": 1, "order": 15})
    service_code: str = field(default="01", metadata={"field_id": "U7", "length": 2, "order": 16})
    unit_of_measure: str = field(default="", metadata={"field_id": "28", "length": 2, "order": 17})

@dataclass
class Pharmacy:
    segment_id: str = "02"
    segment_order: int = 4
    
    # Fields in order
    provider_id_qualifier: str = field(default="05", metadata={"field_id": "EY", "length": 2, "order": 0})
    provider_id: str = field(default="", metadata={"field_id": "E9", "length": 15, "order": 1})

@dataclass
class Prescriber:
    segment_id: str = "03"
    segment_order: int = 5
    
    # Fields in order
    prescriber_id_qualifier: str = field(default="01", metadata={"field_id": "EZ", "length": 2, "order": 0})
    prescriber_id: str = field(default="", metadata={"field_id": "DB", "length": 15, "order": 1})
    prescriber_last_name: str = field(default="", metadata={"field_id": "DR", "length": 15, "order": 2})
    prescriber_phone: str = field(default="", metadata={"field_id": "PM", "length": 10, "order": 3})
    prescriber_street_address: str = field(default="", metadata={"field_id": "2K", "length": 30, "order": 4})
    prescriber_city: str = field(default="", metadata={"field_id": "2M", "length": 20, "order": 5})
    prescriber_state: str = field(default="", metadata={"field_id": "2N", "length": 2, "order": 6})
    prescriber_zip_code: str = field(default="", metadata={"field_id": "2P", "length": 15, "order": 7})

@dataclass
class Pricing:
    segment_id: str = "11"
    segment_order: int = 6
    
    # Fields in order
    ingredient_cost: Decimal = field(default=Decimal("0.00"), metadata={"field_id": "D9", "length": 8, "order": 0})
    dispensing_fee: Decimal = field(default=Decimal("0.00"), metadata={"field_id": "DC", "length": 8, "order": 1})
    usual_and_customary: Decimal = field(default=Decimal("0.00"), metadata={"field_id": "DQ", "length": 8, "order": 2})
    gross_amount_due: Decimal = field(default=Decimal("0.00"), metadata={"field_id": "DU", "length": 8, "order": 3})
    basis_of_cost_determination: str = field(default="03", metadata={"field_id": "DN", "length": 2, "order": 4})
    incentive: Decimal = field(default=Decimal("0.00"), metadata={"field_id": "E3", "length": 8, "order": 5})
    patient_paid: Decimal = field(default=Decimal("0.00"), metadata={"field_id": "DX", "length": 8, "order": 6})

