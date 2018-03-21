from road_vehicle import FlatHauler

consist = FlatHauler(id='towerhouse_flat',
                        base_numeric_id=650,
                        name='Towerhouse [Flatbed Truck]',
                        semi_truck_so_redistribute_capacity=True,
                        vehicle_life=40,
                        intro_date=1968)

consist.add_unit(vehicle_length=2,
                 semi_truck_shift_offset_jank=2,
                 visual_effect='VISUAL_EFFECT_DIESEL',
                 always_use_same_spriterow=True)

consist.add_unit(capacity=40,
                 vehicle_length=7,
                 cargo_length=4)  # some cargo overlap eh?
