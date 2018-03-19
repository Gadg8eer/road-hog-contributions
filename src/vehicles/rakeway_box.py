from road_vehicle import BoxHauler

consist = BoxHauler(id='rakeway_box',
                    base_numeric_id=870,
                    title='Rakeway [Box Tram]',
                    tram_type='ELRL',
                    vehicle_life=40,
                    intro_date=1900)

consist.add_unit(capacity=30,
                 vehicle_length=8,
                 effects=['EFFECT_SPRITE_ELECTRIC, 0, 0, 10'],
                 repeat=2)

