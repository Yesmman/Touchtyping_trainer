class Typing:
    number_of_mistakes = 0
    time = 0
    start_typing = False
    stop = False
    font = "Verdana 18"
    width = 60
    string = ""
    char_index = 0
    string_index = 1
    background_color = "misty rose"
    buttons_color = "misty rose"
    # number_of_symbols = 0

    mode = "Training"

    def reset_timer(self):
        if not self.start_typing:
            self.time = 0
            self.start_typing = True

    def get_result(self):

        number_of_symbols = len(self.string)
        speed = number_of_symbols / self.time
        speed_per_minute = number_of_symbols * 60 / self.time

        results = {
            "Number of symbols": number_of_symbols,
            "Time": self.time,
            "Symbols per second": speed,
            "Symbols per minute": speed_per_minute,
            "Mistakes": self.number_of_mistakes
        }
        return results

    def reset_values(self):
        self.number_of_mistakes = 0
        self.start_typing = False
        self.stop = False
        self.char_index = 0
        self.string_index = 1
        self.width = 60

    def do_stop(self):
        self.stop = True
