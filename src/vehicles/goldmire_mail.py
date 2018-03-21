from road_vehicle import MailHauler

consist = MailHauler(id='goldmire_mail',
                     base_numeric_id=200,
                     name='Goldmire [Courier Truck]',
                     power=250,  # custom power
                     speed=75,
                     vehicle_life=40,
                     intro_date=1971)

consist.add_unit(capacity=25,
                 vehicle_length=6,
                 visual_effect='VISUAL_EFFECT_DIESEL')

