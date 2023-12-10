from goprocam import GoProCamera, constants


import typer

from .base_mode import BaseMode


class WhipeSD(BaseMode):
    def __init__(self, mode: str = all):
        super().__init__(mode)

    def execute(self):
        self.gopro.downloadAll()
        self.gopro.delete("all")
        typer.echo('SD card cleaned!')