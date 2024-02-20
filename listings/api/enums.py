from enum import Enum

class HomeType(Enum):
    SINGLE_FAMILY = "SingleFamily"
    MULTI_FAMILY = "MultiFamily2To4"
    VACANT_RESIDENTIAL_LAND = "VacantResidentialLand"
    CONDO = "Condominium"
    APARTMENT = "Apartment"
    DUPLEX = "Duplex"
    MISCEKLLANEOUS = "Miscellaneous"

    @classmethod
    def choices(cls):
        return tuple((c.name, c.value) for c in cls)