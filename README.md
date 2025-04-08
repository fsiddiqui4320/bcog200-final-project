# bcog200-final-project
1. My project will demonstrate the Serial Position Effect, where participants are shown a list of words for a short duration and then asked to recall as many as possible. The experiment will analyze recall accuracy based on the position of each word in the list. The system will collect response data, visualize recall trends, and analyze how word position influences memory. The results will be displayed in a graph to give insights on how cognitive memory works.
  
2. a. generate_word_list: 
   This function will generate a randomized list of n words from a predefined word bank.

   b. display_words: This function will present the words one by one for a fixed duration.

   c. collect_recall: This function prompts the user to type in as many words as they remember, one by one.

   d. analyze_recall:
	 This function will compare the recalled words with the original list, track recall accuracy by word position, and generate data for plotting a serial position curve.


## Introduction

This program shows how memory works using a common psychology effect called the Serial Position Effect. People usually remember the first and last items in a list better than the middle ones. This project helps show that effect in a simple word recall experiment.
It uses a list of words, shows them to the user, and then asks them to recall as many as they can. The program collects the data and shows how well people remember based on where the words were in the list.

Great for learning about memory. Easy to run. Fast results.

## Functions

- `generate_word_list(n, word_bank)`  
  Picks `n` random words from a list.

- `display_words(word_list)`  
  Shows each word on the screen one by one.

- `collect_recall()`  
  Lets the user type in words they remember.

- `analyze_recall(recalled, original)`  
  Checks which words were remembered and shows results by word position.

## Example Use

- Teachers can use this to show how memory works.
- Students can try it themselves to see how well they remember words.
- Anyone interested in psychology can explore how recall works.

## Input Data
- The list of words shown to the user is stored in `config.py` as a predefined word bank.
- The user does not need to provide any input files.
- User responses (the words they recall) are collected during the experiment and stored separately by the program.