class Ccwc:
    """test doc"""

    def __init__(self, path):
        """test doc"""
        self.path = path
        self.number_of_liness = 0

    def number_of_lines(self):
        """test doc"""
        with open(self.path, "r", encoding="utf-8") as file:
            lines = len(file.readlines())
            self.number_of_liness += lines 
        return lines

    def number_of_bytes(self):
        """test doc"""
        with open(self.path, "rb") as file:
            file_content = file.read()
            return len(file_content)

    def number_of_words(self):
        """test doc"""
        with open(self.path, "r", encoding="utf-8") as file:
            file_content = file.read()
        return len(file_content.split())

    def number_of_chars(self):
        """test doc"""
        with open(
            self.path, "rb"
        ) as file:  # Open in binary mode to handle all bytes directly
            file_content = file.read()
        # Decode the content, ignoring any BOM or unusual markers
        text = file_content.decode("utf-8-sig")
        num_of_chars = len(text)
        if file_content.endswith(b"\n") and not text.endswith("\n"):
            num_of_chars += 1
        return num_of_chars

    def default_mode(self):
        lines = self.number_of_lines()
        words = self.number_of_words()
        #chars = self.number_of_chars()
        bytes = self.number_of_bytes()
        return str(bytes) + (" ") +  str(lines) + (" ") + str(words) + (" ") +  self.path

     


txt_file = Ccwc("test.txt")
#print(txt_file.number_of_lines())
"""print(txt_file.number_of_bytes())
print(txt_file.number_of_chars())
print(txt_file.number_of_words())"""
print(txt_file.default_mode())