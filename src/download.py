import typer

from .base_mode import BaseMode


class Download(BaseMode):
    def __init__(self, mode: str = all):
        super().__init__(mode)

    def execute(self):
        medialist = self.gopro.listMedia(format=True, media_array=True)
        if self.mode == 'video':
            typer.echo('Stating video download mode')
            for media in medialist:
                if "MP4" in media[1]:
                    newpath = self.mode + "/" + media[1]
                    self.gopro.downloadMedia(media[0], media[1], newpath)
        elif self.mode== 'photo':
            typer.echo('Stating photo download mode')
            for media in medialist:
                if "JPG" in media[1]:
                    newpath = self.mode + "/" + media[1]
                    self.gopro.downloadMedia(media[0], media[1], newpath)
        elif self.mode == 'all':
            typer.echo('Download everything mode')
            for media in medialist:
                newpath = self.mode + "/" + media[1]
                self.gopro.downloadMedia(media[0], media[1], newpath)

        else:
            typer.echo('Invalid mode')
            raise typer.Exit()
        