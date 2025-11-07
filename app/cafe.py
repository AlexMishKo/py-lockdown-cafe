import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        name = visitor["name"]
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{name} is not vaccinated.")

        expiration_date = visitor["vaccine"]["expiration_date"]
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError(f"Vaccine of "
                                       f"{name} is expired.")

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(f"{name} "
                                      f"is not wearing a mask.")

        return f"Welcome to {self.name}"
