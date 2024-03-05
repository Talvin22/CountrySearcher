import re


class EmojiCleaner:
    def __init__(self):
        self.__emoji_pattern = re.compile("["
                                          u"\U0001F600-\U0001F64F"  # emoticons
                                          u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                          u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                          u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                          u"\U00002500-\U00002BEF"  # chinese char
                                          u"\U00002702-\U000027B0"
                                          u"\U00002702-\U000027B0"
                                          u"\U000024C2-\U0001F251"
                                          u"\U0001f926-\U0001f937"
                                          u"\U00010000-\U0010ffff"
                                          u"\u2640-\u2642"
                                          u"\u2600-\u2B55"
                                          "]+", flags=re.UNICODE)

    def remove_emojis(self, text: str) -> str:
        return self.__emoji_pattern.sub(r'', text)
