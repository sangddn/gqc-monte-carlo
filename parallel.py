"""
WONG CLASSES — PARALLEL COMPUTING
* GQC: Sang & Joe
* 2022/11/06
"""

from random import choice
from sequential import SampleNormalWongs as SequentialWong
from multiprocessing import Pool

class SampleNormalWongs(SequentialWong):
    def sample_2_children(self, _) -> bool:
        """Samples 2 children with at least 1 boy.
        Returns whether both children are boys.
        """
        results = ''
        while 'b' not in results:
            results = choice(['b', 'g']) + choice(['b', 'g'])
        return results == 'bb'

    def __post_init__(self):
        with Pool() as p:
            results = p.map(self.sample_2_children, range(self.size))
        self.bb = sum(results) # Expensive
        return

class SampleOldestWongs(SampleNormalWongs):
    def sample_2_children(self, _) -> bool:
        return 'b' + choice(['b', 'g']) == 'bb'