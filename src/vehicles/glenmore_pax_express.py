from road_vehicle import PaxExpressCoachConsist, DieselRoadVehicle

# for each generation, bus and coach variants have same power and intro date
# coaches faster, lower capacity than equivalent bus

consist = PaxExpressCoachConsist(id='glenmore_pax_express',
                          base_numeric_id=50,
                          name='Glenmore',
                          power=160,
                          speed=55,
                          vehicle_life=40,
                          gen=3,
                          intro_date_offset=-4)  # introduce earlier than gen epoch by design

consist.add_unit(type=DieselRoadVehicle,
                 capacity=30,
                 vehicle_length=7)
