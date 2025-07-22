"""NCPDP D.0 Segment classes"""

# Import all segment classes
from .patient import Patient
from .pharmacy_provider import PharmacyProvider
from .prescriber import Prescriber
from .insurance import Insurance
from .coord_of_benefits import CoordOfBenefits
from .workers_comp import WorkersComp
from .claim import Claim
from .dur_pps import DurPps
from .coupon import Coupon
from .compound import Compound
from .pricing import Pricing
from .prior_auth import PriorAuth
from .clinical import Clinical
from .additional_documentation import AdditionalDocumentation
from .facility import Facility
from .narrative import Narrative

# Response segments
from .response_message import ResponseMessage
from .response_status import ResponseStatus
from .response_claim import ResponseClaim
from .response_pricing import ResponsePricing
from .response_dur_pps import ResponseDurPps
from .response_insurance import ResponseInsurance
from .response_prior_auth import ResponsePriorAuth
from .response_insurance_additional_documentation import ResponseInsuranceAdditionalDocumentation
from .response_coord_of_benefits import ResponseCoordOfBenefits
from .response_patient import ResponsePatient

# Base segment class
from .base import BaseSegment

# All available segments
__all__ = [
    # Base class
    'BaseSegment',
    
    # Request segments (01-16)
    'Patient',
    'PharmacyProvider', 
    'Prescriber',
    'Insurance',
    'CoordOfBenefits',
    'WorkersComp',
    'Claim',
    'DurPps',
    'Coupon',
    'Compound',
    'Pricing',
    'PriorAuth',
    'Clinical',
    'AdditionalDocumentation',
    'Facility',
    'Narrative',
    
    # Response segments (20-29)
    'ResponseMessage',
    'ResponseStatus',
    'ResponseClaim',
    'ResponsePricing',
    'ResponseDurPps',
    'ResponseInsurance',
    'ResponsePriorAuth',
    'ResponseInsuranceAdditionalDocumentation',
    'ResponseCoordOfBenefits',
    'ResponsePatient',
]

# Segment registry - maps segment identifiers to classes
SEGMENT_CLASSES = {
    '01': Patient,
    '02': PharmacyProvider,
    '03': Prescriber,
    '04': Insurance,
    '05': CoordOfBenefits,
    '06': WorkersComp,
    '07': Claim,
    '08': DurPps,
    '09': Coupon,
    '10': Compound,
    '11': Pricing,
    '12': PriorAuth,
    '13': Clinical,
    '14': AdditionalDocumentation,
    '15': Facility,
    '16': Narrative,
    '20': ResponseMessage,
    '21': ResponseStatus,
    '22': ResponseClaim,
    '23': ResponsePricing,
    '24': ResponseDurPps,
    '25': ResponseInsurance,
    '26': ResponsePriorAuth,
    '27': ResponseInsuranceAdditionalDocumentation,
    '28': ResponseCoordOfBenefits,
    '29': ResponsePatient,
}
