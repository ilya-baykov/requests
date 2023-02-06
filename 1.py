import requests


class Link_scanner:
    def __init__(self, link_A, link_B):
        self.__link_A = link_A
        self.__link_B = link_B

    @staticmethod
    def link_list_gen(current_link: str) -> list[str]:
        return [link for link in requests.get(current_link).text.split('"') if link.startswith("https:")]

    def equals_link(self) -> str:
        for link in self.link_list_gen(self.__link_A):
            for link_inners in self.link_list_gen(link):
                if link_inners == self.__link_B:
                    return "Yes"
            return "No"


test_1 = Link_scanner("https://stepic.org/media/attachments/lesson/24472/sample0.html",
                      "https://stepic.org/media/attachments/lesson/24472/sample2.html")

test_2 = Link_scanner("https://stepic.org/media/attachments/lesson/24472/sample0.html",
                      "https://stepic.org/media/attachments/lesson/24472/sample1.html")

test_3 = Link_scanner("https://stepic.org/media/attachments/lesson/24472/sample1.html",
                      "https://stepic.org/media/attachments/lesson/24472/sample2.html")

if __name__ == '__main__':
    print(test_1.equals_link())
    print(test_2.equals_link())
    print(test_3.equals_link())
