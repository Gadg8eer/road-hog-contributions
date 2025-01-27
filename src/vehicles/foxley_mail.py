from road_vehicle import MailTramConsist, ElectricVehicleUnit


def main(roster_id):
    consist = MailTramConsist(
        roster_id=roster_id,
        id="foxley_mail",
        base_numeric_id=190,
        name="Foxley",
        power=240,  # custom HP
        gen=2,
        intro_date_offset=3,
    )  # introduce later than gen epoch by design

    consist.add_unit(
        base_platform=None,  # mail trams have no base platform by design currently
        type=ElectricVehicleUnit,
        vehicle_length=4,
        repeat=2,
    )

    return consist
