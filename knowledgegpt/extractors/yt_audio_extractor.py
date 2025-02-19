from knowledgegpt.extractors.base_extractor import BaseExtractor
from knowledgegpt.utils.utils_yt_whisper import transcribe_youtube_audio


class YoutubeAudioExtractor(BaseExtractor):
    """
    Takes a YouTube video ID as input, transcribes its audio, and returns the
    embeddings of the resulting text. Uses the embeddings to answer a query.
    """

    def __init__(self, video_id: str, embedding_extractor='hf', model_lang='en', is_turbo: bool = False,
                 verbose: bool = False, index_path: str = None, index_type: str = "basic"):
        super().__init__(embedding_extractor=embedding_extractor, model_lang=model_lang, is_turbo=is_turbo,
                         verbose=verbose, index_path=index_path, index_type=index_type)
        self.video_id = video_id

    def prepare_df(self):
        if self.df is None:
            if not self.verbose:
                print("Transcribing audio...")
            if not self.video_id:
                raise ValueError("Video ID is missing")
            self.df = transcribe_youtube_audio(self.video_id)
