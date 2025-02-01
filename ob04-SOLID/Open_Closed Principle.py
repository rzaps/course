# class Report():
#     def __init__(self, titlle, content):
#         self.titlle = titlle
#         self.content = content
#
#     def doc_printer(self):
#         print(f"Сформирован отчет: {self.titlle} - {self.content}")
#
from abc import ABC, abstractmethod

class Formatted(ABC):
    @abstractmethod
    def format(self, report):
        pass

class TextFormatted(Formatted):
    def format(self, report):
        print(report.title)
        print(report.content)

class HtmlFormatted(Formatted):
    def format(self, report):
        print(f"<h1>{report.title}</h1>")
        print(f"<p>{report.content}</p>")

class Report():
    def __init__(self, title, content, formatted):
        self.title = title
        self.content = content
        self.formatted = formatted

    def doc_printer(self):
        self.formatted.format(self)


report = Report("Заголовок", "Текст отчета", HtmlFormatted())

report.doc_printer()