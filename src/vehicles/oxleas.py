from road_vehicle import PaxExpressHauler

# for each generation, bus and coach variants have same power and intro date
# coaches faster, lower capacity than equivalent bus

consist = PaxExpressHauler(id='oxleas',
                           base_numeric_id=610,
                           title='Oxleas [Coach]',
                           power=240,
                           speed=75,
                           vehicle_life=40,
                           intro_date=1964)

consist.add_unit(capacity=40,
                 vehicle_length=7,
                 visual_effect='VISUAL_EFFECT_DIESEL')

consist.add_model_variant(spritesheet_suffix=0)
