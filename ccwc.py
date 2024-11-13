class Ccwc:
    """test doc"""

    def __init__(self, path):
        """test doc"""
        self.path = path

    def number_of_lines(self):
        """test doc"""
        with open(self.path, "r", encoding="utf-8") as file:
            lines = len(file.readlines())
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


txt_file = Ccwc("test.txt")

print(txt_file.number_of_lines())
print(txt_file.number_of_bytes())
print(txt_file.number_of_chars())
print(txt_file.number_of_words())