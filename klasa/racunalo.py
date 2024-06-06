from enum import Enum

class VrstaDiska(Enum):
    SSD = 'SSD'
    HDD = 'HDD'

class VrstaRacunala(Enum):
    PRIJENOSNO = 'PRIJENOSNO'
    STOLNO = 'STOLNO'


class Racunalo:
    def __init__(self,procesor,ram,disk:VrstaDiska,diskSize,vrsta:VrstaRacunala, imaExternuGraficku:bool) -> None:
        self.procesor = procesor
        self._ram = ram
        self._disk = disk
        self._diskSize = diskSize
        self.vrsta = vrsta
        self.graficka = imaExternuGraficku
    
    def azurirajRAMmemoriju(self,kolicina):
        self._ram = kolicina

    def azurirajDisk(self,disk:VrstaDiska = None, diskSize = None):
        if disk is not None:
            self._disk = disk

        if diskSize is not None:
            self._diskSize = diskSize
    
    def __repr__(self):
        return f"Racunalo ({self.vrsta.value}; procesor{self.procesor}), "\
               f"Ram: ({self._ram}; Disk: {self._disk};Disk: {self._diskSize}), "\
               f"externa graficka ({'ima'if self.graficka else 'nema'})"
               

r1 = Racunalo("intel i5", 16,VrstaDiska.SSD,512,VrstaRacunala.PRIJENOSNO,False)        
repr(r1)
r1.azurirajDisk(disk=VrstaDiska.HDD,diskSize=1024)

repr(r1.azurirajDisk(disk=VrstaDiska.HDD,diskSize=1024))