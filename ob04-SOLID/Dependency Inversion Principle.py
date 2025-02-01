# class Book():
#     def read(self):
#         print("Читаем книгу")
#
# class StoryReader():
#     def __init__(self):
#         self.book = Book()
#
#     def tell_story(self):
#         self.book.read()

from abc import ABC, abstractmethod

class StorySource(ABC):
    @abstractmethod
    def get_story(self):
        pass

class Book(StorySource):
    def get_story(self):
        print("Читаем книгу")

class AudioBook(StorySource):
    def get_story(self):
        print("Слушаем книгу")


class StoryReader():
    def __init__(self, story_source: StorySource):
        self.story_source = story_source

    def tell_story(self):
        self.story_source.get_story()


book = Book()
audio_book = AudioBook()

reader_book = StoryReader(book)
reader_audio_book = StoryReader(audio_book)

reader_book.tell_story()
reader_audio_book.tell_story()