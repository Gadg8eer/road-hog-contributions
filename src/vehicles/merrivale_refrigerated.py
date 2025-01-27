from road_vehicle import RefrigeratedTruckConsist
from base_platforms.trucks import DieselConventionalCabSemiTractorTruckGen3A


def main(roster_id):
    consist = RefrigeratedTruckConsist(
        roster_id=roster_id,
        id="merrivale_refrigerated",
        base_numeric_id=300,
        name="Merrivale",
        gen=3,
        intro_date_offset=10,
    )  # introduce later than gen epoch by design

    consist.add_unit(base_platform=DieselConventionalCabSemiTractorTruckGen3A)

    consist.add_unit(base_platform=None, vehicle_length=6)

    return consist
