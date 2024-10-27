# Hebrew Root System Demonstration

## Overview
This repository contains Python code designed to illustrate the Hebrew root system, a foundational concept in the morphology of Hebrew and other Semitic languages. The code demonstrates how words in Hebrew are derived from roots by modifying these roots through the addition of vowels and sometimes extra consonants.

## Purpose
The primary purpose of this project is to provide a simple, educational tool that mimics the process of word formation in Semitic languages using object-oriented programming principles. It aims to help users, especially those unfamiliar with Semitic languages, understand how a single root can produce multiple related words through systematic morphological changes.

## The Hebrew Root System
In Semitic languages like Hebrew, words are typically formed by starting with a basic set of consonants, known as a root. These roots generally consist of three consonants and encode a basic lexical meaning. Words are formed by inserting vowels and sometimes affixes around these roots, allowing a variety of related meanings to emerge from a single root.

### Example
A common example is the root אדם (ADM), which relates to the concept of man or humanity. From this root, words such as:
- **אדם (Adam)** - "man" or "human"
- **אדמה (Adamah)** - "earth" or "ground"
- **אדום (Adom)** - "red"

are formed, each illustrating a different aspect of the root's lexical field.

## How It Works
The repository contains an abstract base class `RootADM` that outlines the structure for classes that represent words derived from the root אדם. Each derived class implements the abstract methods `construct_word()` and `get_meaning()` to specify how the word is formed from the root and what it means.

### Structure
- **RootADM**: Abstract base class with a method to construct a word from the root אדם.
- **Derived Classes**: Specific classes for each word (e.g., Adam, Adamah, Adom) that implement the abstract methods to provide their unique contributions to the root.

## Usage
To use the code, instantiate an object of the desired class and call its methods to retrieve the constructed word and its meaning. This can be useful for educational purposes or as a starting point for a more comprehensive exploration of Hebrew morphology in software applications.

## Conclusion
This project serves as a conceptual bridge between linguistics and computer science, using the principles of object-oriented programming to model linguistic structures. It is hoped that this will foster a greater appreciation of the complexity and beauty of Semitic languages.
