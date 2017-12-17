import global_constants
from road_vehicle import PaxHauler

# for each generation, bus and coach variants have same power and intro date
# coaches faster, lower capacity than equivalent bus

consist = PaxHauler(id='leyburn',
                    base_numeric_id=20,
                    title='Leyburn [Bus]',
                    power=100,  # custom power
                    speed=40,
                    vehicle_life=40,
                    intro_date=1909)

consist.add_unit(capacity=44,
                 vehicle_length=7,
                 visual_effect='VISUAL_EFFECT_DIESEL')

consist.add_model_variant(intro_date=0,
                          end_date=global_constants.max_game_date,
                          spritesheet_suffix=0)
