class ModelException(Exception):

    def __init__(self, *args, **kwargs):
        """
        exception for model
        """
        super().__init__(*args, **kwargs)

class VideoException(Exception):

    def __init__(self, *args, **kwargs):
        """
        exception for video
        """
        super().__init__(*args, **kwargs)