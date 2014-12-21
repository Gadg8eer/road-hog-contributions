import global_constants
from road_vehicle import EngineConsist, PaxHauler

consist = EngineConsist(id = 'acton',
              base_numeric_id = 600,
              title = 'Acton [Coach]',
              replacement_id = '-none',
              power = 220,
              speed_dibble = 'speedy',
              vehicle_life = 40,
              intro_date = 1972)

consist.add_unit(PaxHauler(consist = consist,
                        weight = 20,
                        capacity = 50,
                        vehicle_length = 7,
                        visual_effect = 'VISUAL_EFFECT_DIESEL',
                        spriterow_num = 0))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
