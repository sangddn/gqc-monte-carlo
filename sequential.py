"""
WONG CLASSES — SEQUENTIAL COMPUTING
* GQC: Sang & Joe
* 2022/11/06
"""

from random import choice
from dataclasses import dataclass

@dataclass
class SampleNormalWongs:
    size: int
    bb: int = 0

    def sample_2_children(self) -> str:
        return choice(['b', 'g']) + choice(['b', 'g'])

    def __post_init__(self) -> None:
        n_sample = 0
        while n_sample < self.size:
            children = self.sample_2_children()
            if 'b' in children:
                n_sample += 1
                if children == 'bb':
                    self.bb += 1
        return
    
    def ratio_of_bb(self) -> float:
        return self.bb / self.size

    def __str__(self) -> str:
        return f'Among these {self.size} Wongs, {self.bb}, which is {self.ratio_of_bb()*100:.3f}%, had 2 boys.'

class SampleOldestWongs(SampleNormalWongs):
    def sample_2_children(self) -> str:
        return 'b' + choice(['b', 'g'])