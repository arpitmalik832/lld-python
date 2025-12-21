from abc import abstractmethod, ABC


class ICode(ABC):
    @abstractmethod
    def code(self):
        pass


class IResearch(ABC):
    @abstractmethod
    def research(self):
        pass


class IDesign(ABC):
    @abstractmethod
    def design(self):
        pass


class ChatGPT(ICode):
    def code(self):
        pass


class Gemini(IResearch):
    def research(self):
        pass


class Grok(IDesign):
    def design(self):
        pass


def main():
    chatgpt = ChatGPT()
    chatgpt.code()


main()
