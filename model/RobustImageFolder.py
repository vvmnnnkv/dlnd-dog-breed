from torchvision import datasets
from PIL import ImageFile

class RobustImageFolder(datasets.ImageFolder):
    def __getitem__(self, *args, **kwargs):
        ImageFile.LOAD_TRUNCATED_IMAGES = True
        return super(RobustImageFolder, self).__getitem__(*args, **kwargs)
