from road_vehicle import BoxHauler

consist = BoxHauler(id='speedwell_box',
                    base_numeric_id=400,
                    name='Speedwell [Box Truck]',
                    semi_truck_so_redistribute_capacity=True,
                    vehicle_life=40,
                    intro_date=1997)

consist.add_unit(capacity=0,
                 vehicle_length=2,
                 semi_truck_shift_offset_jank=2,
                 effects=['EFFECT_SPRITE_DIESEL, -2, 1, 10'])

consist.add_unit(capacity=40,
                 vehicle_length=7)

