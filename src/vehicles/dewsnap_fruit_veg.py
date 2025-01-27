from road_vehicle import FruitVegFeldbahnConsist
from base_platforms.feldbahn import SteamEngineFeldbahnGen2A, WagonFeldbahnA


def main(roster_id):
    consist = FruitVegFeldbahnConsist(
        roster_id=roster_id,
        id="dewsnap_fruit_veg",
        base_numeric_id=1180,
        name="Dewsnap",
        gen=2,
    )

    consist.add_unit(base_platform=SteamEngineFeldbahnGen2A)

    consist.add_unit(base_platform=WagonFeldbahnA, repeat=5)

    return consist
