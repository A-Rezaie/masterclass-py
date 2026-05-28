class TextAnalyzer:
    """Analyze a sentence and find the longest word(s)."""

    def __init__(self, sentence):
        self.sentence = sentence

    def get_longest_words(self):
        words = self.sentence.split()
        if not words:
            return [], 0
        max_length = 0
        longest_words = []
        for item in words:
            if len(item) > max_length:
                max_length = len(item)
        for item in words:
            if len(item) == max_length:
                longest_words.append(item)

        return longest_words, max_length
        


    def display_results(self):
        longest_words, max_length = self.get_longest_words()
        if not longest_words:
            print("No words found.")
            return
        print("Longest word(s):")
        print()
        for word in longest_words:
            print(f"{word} ({max_length} letters)")


def main():
    text = input("Enter your sentence: ")
    analyzer = TextAnalyzer(text)
    analyzer.display_results()
    


if __name__ == "__main__":
    main()

