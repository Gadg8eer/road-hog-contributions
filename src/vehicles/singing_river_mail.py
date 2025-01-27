from road_vehicle import MailTramConsist, ElectricVehicleUnit


def main(roster_id):
    consist = MailTramConsist(
        roster_id=roster_id,
        id="singing_river_mail",
        base_numeric_id=850,
        name="Singing River",
        power=600,
        gen=5,
    )

    consist.add_unit(
        base_platform=None,  # mail trams have no base platform by design currently
        type=ElectricVehicleUnit,
        vehicle_length=8,
        effects=["EFFECT_SPRITE_ELECTRIC, 0, 0, 10"],
    )

    return consist
