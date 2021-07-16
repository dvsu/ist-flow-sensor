from machine import ADC


class ISTFS7:

    n = 0.46
    k = 0.5905
    Uo = 2.1612

    def __init__(self, pin:str):
        self.adc = ADC()
        self.apin = self.adc.channel(pin=pin, attn=ADC.ATTN_11DB)
    
    def _get_pin_voltage(self) -> float:
        try:
            return self.apin.voltage() / 1000

        except Exception as e:
            return 0
    
    def _velocity(self) -> float:
        try:
            U = self._get_pin_voltage()

            num = ((U-self.Uo)*(U+self.Uo))**(1/self.n)
            den = ((self.k)**(1/self.n))*((self.Uo)**(2/self.n))
            return abs(num) / den
        
        except Exception as e:
            return 0

    def get_measurement(self) -> dict:
        try:
            return {
                "velocity": round(self._velocity(), 3),
                "velocity_unit": "m/s"
            }
        
        except Exception as e:
            return {
                "velocity": 0.0,
                "velocity_unit": "m/s"
            }  
