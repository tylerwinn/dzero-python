def get_gender_code(gender: str) -> str:
    match gender.upper():
        case "M" | "MALE":
            return "1"
        case "F" | "FEMALE":
            return "2"
        case _:
            return "0"
        
def get_relationship_code(person_code: str) -> str:
    match person_code:
        case "00" | "":
            return "1"  # Self
        case "01":
            return "2"  # Spouse
        case "02":
            return "3"  # Child
        case "03":
            return "4"  # Other
        case _:
            return "1"  # Unknown
        
def get_daw_code(daw_code: str) -> str:
    match daw_code:
        case "N":
            return "0"  # No product selection indicated
        case "Y":
            return "1"  # Substitution not allowed by prescriber
        case _:
            return "0"  # Default to No product selection indicated