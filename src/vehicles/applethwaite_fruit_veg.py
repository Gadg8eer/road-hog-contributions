from road_vehicle import FruitVegTramConsist
from base_platforms.trams import ElectricMotorTram1


def main(roster_id):
    consist = FruitVegTramConsist(
        roster_id=roster_id,
        id="applethwaite_fruit_veg",
        base_numeric_id=940,
        name="Applethwaite",
        gen=2,
        intro_date_offset=1,
    )  # introduce later than gen epoch by design

    consist.add_unit(base_platform=ElectricMotorTram1, repeat=2)

    return consist
