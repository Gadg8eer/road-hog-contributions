from road_vehicle import LivestockTramConsist
from base_platforms.trams import ElectricMotorTram4


def main(roster_id):
    consist = LivestockTramConsist(
        roster_id=roster_id,
        id="shotover_livestock",
        base_numeric_id=370,
        name="Shotover",
        gen=3,
        intro_date_offset=1,
    )  # introduce later than gen epoch by design

    consist.add_unit(base_platform=ElectricMotorTram4, repeat=2)

    return consist
