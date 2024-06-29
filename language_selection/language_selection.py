class language:
    def __init__(self, language = "English"):
        self._language = language
        self.language_choices()
        
    def get_language(self):
        return self._language
    def set_language(self, option):
        self._option = option
        if self._option in self._languageChoices:
            self._language = option
            output = f"Language have been changed to {self._language}"
            return output
        else:
            output="No Similar Language is Found"
            return output
    def language_choices(self):
        self._languageChoices = [
            'English',
            'Japanese',
            'Hindi',
            'German',
            'Lithuanian',
            'tagalog']
        return self._languageChoices
