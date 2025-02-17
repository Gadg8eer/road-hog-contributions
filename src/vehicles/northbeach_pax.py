from road_vehicle import PaxLocalTramConsist, ElectricVehicleUnit


def main(roster_id):
    consist = PaxLocalTramConsist(
        roster_id=roster_id,
        id="northbeach_pax",
        base_numeric_id=690,
        name="Northbeach",
        gen=4,
        intro_date_offset=1,
    )  # introduce later than gen epoch by design

    consist.add_unit(
        base_platform=None,  # pax trams have no base platform by design currently
        type=ElectricVehicleUnit,
        vehicle_length=8,
        effects=["EFFECT_SPRITE_ELECTRIC, 0, 0, 12"],
        repeat=2,
    )

    return consist
