# Test Description:
# This script outlines how to test the Serial Position Memory Recall Task end-to-end.
# 1. Load a sample word bank file named 'word_bank.txt' with at least 20 words, each on a separate line.
# 2. Use generate_word_list(n) to randomly select 10 words from this word bank.
# 3. Use display_words() to sequentially present these words to the participant for a short time (e.g., 1.5 seconds each).
# 4. Use collect_recall() to allow the participant to type in recalled words after the list has been shown.
# 5. Use analyze_recall() to compare recalled words with the original list and generate recall accuracy by word position.
# This test will help ensure the program logic, input handling, and output formatting are functioning correctly.