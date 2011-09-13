class Joke:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __str__(self):
        out = "\n"
        out += "########################\n"
        out += "Title: " + self.title + "\n"
        out += "########################\n"
        out += "########################\n"
        out += "Content:"
        out += self.content + "\n"
        out += "########################\n"
        return out
