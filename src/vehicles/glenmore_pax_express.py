from road_vehicle import PaxExpressCoach, DieselRoadVehicle

# for each generation, bus and coach variants have same power and intro date
# coaches faster, lower capacity than equivalent bus

consist = PaxExpressCoach(id='glenmore_pax_express',
                          base_numeric_id=50,
                          name='Glenmore',
                          power=160,
                          speed=55,
                          vehicle_life=40,
                          gen=4,
                          intro_date=1935)

consist.add_unit(type=DieselRoadVehicle,
                 capacity=30,
                 vehicle_length=7)
