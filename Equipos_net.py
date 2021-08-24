"""
La programacion orientada a objetos u OPP, permite tener una relación cercana al mundo real.
- Clases
- Atributos
- Métodos
"""

class Router:

    num_slots = 0

    def __init__(self, model, version, ip_add):
        self.model = model
        self.version = version
        self.ip_add = ip_add

    def Get_Description(self):
        desc = f"Modelo:\t {self.model}\nVersion: {self.version} \nIP Address: {self.ip_add}"
        return desc


router1 = Router("ASR1006", "IOS-XE", "10.14.165.24")   
print(router1.model)

print(router1.Get_Description())
print("\n")
router2 = Router("MX480", "JUNOS 14.02", "10.176.240.16")
print(router2.Get_Description())
router2.num_slots = 4

print(router2.num_slots)

