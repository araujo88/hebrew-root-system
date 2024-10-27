from abc import ABC, abstractmethod

class RootADM(ABC):
    root = "אדם"
    
    @abstractmethod
    def construct_word(self):
        """Construct the word from the root by adding vowels or additional letters."""
        pass
    
    @abstractmethod
    def get_meaning(self):
        """Return the meaning of the constructed word."""
        pass

class Adam(RootADM):
    def construct_word(self):
        return self.root  # Uses the root directly

    def get_meaning(self):
        return "Human, man, the first man"

class Adamah(RootADM):
    def construct_word(self):
        return self.root + "ה"  # Extends the root with 'ה'

    def get_meaning(self):
        return "Ground, earth"

class Adom(RootADM):
    def construct_word(self):
        return self.root[:-1] + "ום"  # Changes the ending to create 'אדום'

    def get_meaning(self):
        return "Red"


def print_word_details(word):
    constructed_word = word.construct_word()
    print(f"Constructed Word: {constructed_word}")
    print(f"Meaning: {word.get_meaning()}")

# Create instances of each word
adam = Adam()
adamah = Adamah()
adom = Adom()

# Print details about each word
print("Adam:")
print_word_details(adam)
print("\nAdamah:")
print_word_details(adamah)
print("\nAdom:")
print_word_details(adom)
