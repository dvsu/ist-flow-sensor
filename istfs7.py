from machine import ADC


class ISTFS7:

    n = 0.46
    k = 0.5905
    Uo = 2.1612

    def __init__(self, pin:str):
        self.adc = ADC()
        self.apin = self.adc.channel(pin=pin, attn=ADC.ATTN_11DB)
    
    def get_pin_voltage(self) -> float:
        return self.apin.voltage() / 1000

    def velocity(self) -> float:
        U = self.get_pin_voltage()
        num = ((U-self.Uo)*(U+self.Uo))**(1/self.n)
        den = ((self.k)**(1/self.n))*((self.Uo)**(2/self.n))
        return num / den
