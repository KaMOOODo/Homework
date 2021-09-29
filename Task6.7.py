"""Implement a Pagination class helpful to arrange text on pages and list content on given page. 
The class should take in a text and a positive integer which indicate how many symbols will be allowed per each page 
(take spaces into account as well). You need to be able to get the amount of whole symbols in text, 
get a number of pages that came out and method that accepts the page number and 
return quantity of symbols on this page. If the provided number of the page is missing print the warning message 
"Invalid index. Page is missing". 
If you're familliar with using of Excpetions in Python display the error message in this way.
Pages indexing starts with 0.
Optional: implement searching/filtering pages by symblos/words and displaying pages with all the symbols on it.
If you're querying by symbol that appears on many pages or
if you are querying by the word that is splitted in two return an array of all the occurences.
"""

class Pagination:
    pages = {}

    def __init__(self, content: str, page_len: int):
        self.content = content
        self.page_len = abs(page_len)
        self.item_count = len(self.content)
        self.pages = self.page_creator()
        self.page_count = self.set_page_count()

    def page_creator(self):
        counter = 0
        for i in range(0, self.item_count, self.page_len):
            self.pages[counter] = self.content[i:i+self.page_len]
            counter += 1
        return self.pages

    def set_page_count(self):
        return len(self.pages)

    def count_items_on_page(self, index):
        try:
            return print(len(self.pages[index]))
        except:
            KeyError(print("Invalid index. Page is missing."))

    def find_page(self, find_str):
        __indexes = []
        if find_str in self.content:
            for i in range(len(self.content)):
                if self.content.startswith(find_str, i):
                    __indexes.append(i // self.page_len)
                    if (i + len(find_str)) // self.page_len != (i // self.page_len):
                        __indexes.append((i + len(find_str)) // self.page_len)
            return print(__indexes)

        else:
            return print(f"'{find_str}' is missing on the pages")

    def display_page(self, number):
        return print(self.pages[number])


pages = Pagination('Your beautiful text', 5)
pages.page_count
# 4
pages.item_count
# 19
#
pages.count_items_on_page(0)
# 5
pages.count_items_on_page(3)
# 4
pages.count_items_on_page(4)
# Exception: Invalid index. Page is missing.
#
pages.find_page('Your')
# [0]
pages.find_page('e')
# [1, 3]
pages.find_page('beautiful')
# [1, 2]
pages.find_page('great')
# Exception: 'great' is missing on the pages
pages.display_page(0)
# 'Your '