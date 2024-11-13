class Ccwc:
    """ test doc"""
    def __init__(self, path):
        """ test doc"""
        self.path = path

    def number_of_lines(self):
        """ test doc"""
        with open(self.path, 'r', encoding='utf-8') as file:
            lines = len(file.readlines())
            return lines

    def number_of_bytes(self):
        """ test doc"""
        with open(self.path, 'rb') as file:
            file_content = file.read()
            return len(file_content)

    def number_of_words(self):
        pass
    
    def number_of_chars(self):
        """ test doc"""
        with open(self.path, 'r', encoding='utf-8') as file:
            file_content = file.read()
        return len(file_content)

txt_file = Ccwc("test.txt")

print(txt_file.number_of_lines())
print(txt_file.number_of_bytes())
print(txt_file.number_of_chars())