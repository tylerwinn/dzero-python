from decimal import Decimal
from services.serializer import (
    deserialize_transmission_string,
    serialize_transmission_string,
    update_transmission_string
)
from examples.requests import SAMPLE
from pprint import pprint
from models.segments import (
    Header,
    Patient,
    Insurance,
    Claim,
    Pharmacy,
    Prescriber,
    Pricing
)

if __name__ == "__main__":
    header, patient, insurance, claim, pharmacy, prescriber, pricing = deserialize_transmission_string(SAMPLE)
    
    pprint(header)
    pprint(patient)
    pprint(insurance)
    pprint(claim)
    pprint(pharmacy)
    pprint(prescriber)
    pprint(pricing)

    header = Header(
        segment_order=0,
        bin_number='610591',
        version_number='D0',
        transaction_code='B1',
        processor_control_number='ADV',
        transaction_count='1',
        provider_id_qualifier='01',
        provider_id='1112223330',
        date_of_service='20260123',
        software_vendor_id='D012000030'
    )

    patient = Patient(
        segment_id='01',
        segment_order=1,
        date_of_birth='20230609',
        gender_code='1',
        first_name='JOHN',
        last_name='DOE',
        street_address='123 CHERRY ST',
        city='SOMEWHERE',
        state='NJ',
        zip_code='00012',
        phone_number='0987654321',
        residence_code='1',
        place_of_service='01',
        pregnancy_indicator='1',
        patient_id='',
        patient_id_qualifier=''
    )

    insurance = Insurance(
        segment_id='04',
        segment_order=2,
        cardholder_id='P12345678901234',
        cardholder_first_name='JOHN',
        cardholder_last_name='DOE',
        eligibility_clarification_code='0',
        group_id='RX1234',
        person_code='01',
        relationship_code='1',
        assignment_indicator='Y'
    )

    claim = Claim(
        segment_id='07',
        segment_order=3,
        prescription_reference_qualifier='1',
        prescription_reference_number='725637',
        product_service_id_qualifier='03',
        product_service_id='65862007101',
        quantity_dispensed='0000100000',
        quantity_prescribed='0000100000',
        fill_number='00',
        days_supply='010',
        compound_code='1',
        daw_code='0',
        written_date='20260123',
        authorized_refills='00',
        submission_clarification_code_count='1',
        submission_clarification_code='01',
        other_coverage_code='00',
        origin_code='3',
        service_code='01',
        unit_of_measure='ML'
    )

    pharmacy = Pharmacy(
        segment_id='02',
        segment_order=4,
        provider_id_qualifier='05',
        provider_id='1112223330'
    )

    prescriber = Prescriber(
        segment_id='03',
        segment_order=5,
        prescriber_id_qualifier='01',
        prescriber_id='9998887770',
        prescriber_last_name='DOE',
        prescriber_phone='1234567890',
        prescriber_street_address='123 MAIN ST',
        prescriber_city='SOMEWHERE',
        prescriber_state='NJ',
        prescriber_zip_code='07001'
    )

    pricing = Pricing(
        segment_id='11',
        segment_order=6,
        ingredient_cost=Decimal('35'),
        dispensing_fee=Decimal('4.5'),
        usual_and_customary=Decimal('39.5'),
        gross_amount_due=Decimal('39.5'),
        basis_of_cost_determination='03',
        incentive=Decimal('0'),
        patient_paid=Decimal('0')
    )

    transmission_string = serialize_transmission_string(
        header,
        patient,
        insurance,
        claim,
        pharmacy,
        prescriber,
        pricing
    )

    print("\nSerialized Transmission String:")
    print(transmission_string)

    pricing = Pricing(
        segment_id='11',
        segment_order=6,
        ingredient_cost=Decimal('50'),
        dispensing_fee=Decimal('5.0'),
        usual_and_customary=Decimal('55.0'),
        gross_amount_due=Decimal('55.0'),
        basis_of_cost_determination='03',
        incentive=Decimal('0'),
        patient_paid=Decimal('0')
    )

    updated_transmission_string = update_transmission_string(
        pricing=pricing,
        transmission_string=transmission_string
    )
    print("\nUpdated Transmission String:")
    print(updated_transmission_string)