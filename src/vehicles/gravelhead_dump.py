from road_vehicle import DumpTruckConsist


def main(roster_id):
    consist = DumpTruckConsist(
        roster_id=roster_id,
        id="gravelhead_dump",
        base_numeric_id=580,
        name="Gravelhead",
        power=130,
        gen=4,
        intro_date=1920,
    )

    consist.add_unit(
        vehicle_length=6,
        effect_spawn_model="EFFECT_SPAWN_MODEL_STEAM",
        effects=["EFFECT_SPRITE_STEAM, -3, 0, 12"],
    )

    consist.add_unit(base_platform=None, vehicle_length=5)

    return consist
