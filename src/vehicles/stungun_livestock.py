from road_vehicle import LivestockTruckConsist
from base_platforms.trucks import DieselCaboverSemiTractorTruckGen5A


def main(roster_id):
    consist = LivestockTruckConsist(
        roster_id=roster_id,
        id="stungun_livestock",
        base_numeric_id=430,
        name="Stungun",
        gen=5,
        intro_date_offset=2,
    )  # introduce later than gen epoch by design

    consist.add_unit(base_platform=DieselCaboverSemiTractorTruckGen5A)

    consist.add_unit(base_platform=None, vehicle_length=8)

    return consist
