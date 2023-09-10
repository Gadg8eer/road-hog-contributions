from road_vehicle import MailTramConsist, ElectricVehicleUnit

consist = MailTramConsist(
    id="stagrun_mail",
    base_numeric_id=840,
    name="Stagrun",
    power=360,  # custom power
    gen=3,
    intro_date_offset=2,
)  # introduce later than gen epoch by design

consist.add_unit(
    base_platform=None,  # mail trams have no base platform by design currently
    type=ElectricVehicleUnit,
    vehicle_length=4,
    repeat=2,
)
