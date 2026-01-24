# dzero-python

A Python library for parsing and serializing NCPDP D.0 (Telecommunication Standard) pharmacy claim transactions.

## Overview

This library provides tools to work with NCPDP D.0 format strings used in pharmacy benefit management and claims processing. It supports:

- **Deserializing** transmission strings into Python dataclasses
- **Serializing** Python dataclasses back into transmission strings
- **Overpunch encoding/decoding** for monetary values
- **Field formatting** according to NCPDP specifications

## Installation

Clone the repository and use directly:

```bash
git clone <repository-url>
cd dzero-python
```

No external dependencies required — uses only Python standard library.

## Quick Start

### Parsing a Transmission String

```python
from services.serializer import deserialize_transmission_string

transmission_string = "610591D0B1ADV..."  # Your NCPDP D.0 string

header, patient, insurance, claim, pharmacy, prescriber, pricing = deserialize_transmission_string(transmission_string)

print(patient.first_name)  # "JOHN"
print(pricing.gross_amount_due)  # Decimal("39.50")
```

### Creating a Transmission String

```python
from decimal import Decimal
from services.serializer import serialize_transmission_string
from models.segments import Header, Patient, Insurance, Claim, Pharmacy, Prescriber, Pricing

header = Header(
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
    date_of_birth='20230609',
    gender_code='1',
    first_name='JOHN',
    last_name='DOE',
    street_address='123 CHERRY ST',
    city='SOMEWHERE',
    state='NJ',
    zip_code='00012'
)

# ... create other segments ...

transmission_string = serialize_transmission_string(
    header, patient, insurance, claim, pharmacy, prescriber, pricing
)
```

### Updating an Existing Transmission String

```python
from services.serializer import update_transmission_string
from models.segments import Patient

# Update only the patient segment
updated_string = update_transmission_string(
    patient=Patient(first_name='JANE', last_name='SMITH'),
    transmission_string=existing_string
)
```

## Supported Segments

| Segment    | ID  | Description                                    |
|------------|-----|------------------------------------------------|
| Header     | -   | BIN, version, transaction code, provider info  |
| Patient    | 01  | Demographics, address, identifiers             |
| Pharmacy   | 02  | Provider identification                        |
| Prescriber | 03  | Prescriber info and address                    |
| Insurance  | 04  | Cardholder info, group, eligibility            |
| Claim      | 07  | Prescription details, NDC, quantities          |
| Pricing    | 11  | Costs, fees, amounts (overpunch encoded)       |

## Project Structure

```
dzero-python/
├── example.py              # Usage examples
├── models/
│   └── segments.py         # Dataclass definitions for all segments
├── services/
│   ├── constants.py        # NCPDP constants and lookup tables
│   └── serializer.py       # Serialize/deserialize functions
├── utils/
│   ├── money.py            # Overpunch encoding/decoding
│   ├── ncpdp.py            # NCPDP helper functions
│   ├── number.py           # Number utilities
│   └── string.py           # String formatting utilities
└── examples/
    └── requests.py         # Sample transmission strings
```

## Overpunch Notation

NCPDP uses overpunch notation to encode the sign of monetary values in the last digit:

| Positive | Value | Negative | Value |
|----------|-------|----------|-------|
| {        | 0     | }        | 0     |
| A        | 1     | J        | -1    |
| B        | 2     | K        | -2    |
| C        | 3     | L        | -3    |
| D        | 4     | M        | -4    |
| E        | 5     | N        | -5    |
| F        | 6     | O        | -6    |
| G        | 7     | P        | -7    |
| H        | 8     | Q        | -8    |
| I        | 9     | R        | -9    |

Example: `0000350{` = $3.50, `0000987I` = $98.79

## Running the Example

```bash
python example.py
```

This will:
1. Parse a sample transmission string
2. Display all parsed segments
3. Create new segments from scratch
4. Serialize them back to a transmission string

## License

MIT
