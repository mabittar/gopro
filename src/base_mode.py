
import abc
from goprocam import GoProCamera

class BaseMode:
    def __init__(self, mode: str):
        self.mode = mode
        self.gopro = GoProCamera.GoPro()

    @abc.abstractmethod
    def execute(self):
        pass
    