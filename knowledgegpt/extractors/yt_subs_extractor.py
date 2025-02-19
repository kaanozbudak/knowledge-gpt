from knowledgegpt.extractors.base_extractor import BaseExtractor
from knowledgegpt.utils.utils_subtitles import scrape_youtube


class YTSubsExtractor(BaseExtractor):
    """
     Method that takes a YouTube video ID as input and returns the captions
    as a pandas DataFrame with the key "caption".
    :param video_id: YouTube video ID
    """

    def __init__(self, video_id: str, model_lang="en", embedding_extractor="hf", is_turbo: bool = False,
                 verbose: bool = False, index_path: str = None, index_type: str = "basic"):
        super().__init__(embedding_extractor=embedding_extractor, model_lang=model_lang, is_turbo=is_turbo,
                         verbose=verbose, index_path=index_path, index_type=index_type)
        self.video_id = video_id

    def prepare_df(self):
        if self.df is None:
            if not self.verbose:
                print("Extracting text...")
            if not self.video_id:
                raise ValueError("Video ID is missing")
            self.df = scrape_youtube(self.video_id)
