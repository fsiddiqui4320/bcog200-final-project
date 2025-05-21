from src.exp import Exp

def test_generate_word_list():
    with open("test_word_bank.csv", 'w') as f:
        f.write("Apple,Banana,Cherry,Date,Elderberry,Fig,Grape,Honeydew,Kiwi,Lemon")
    
    words = Exp.generate_word_list(3, "test_word_bank.csv")
    assert len(words) == 3

def test_display_words():
    Exp.display_words(["Apple", "Banana"], display_time=0.1)

def test_collect_recall(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "apple banana")
    recalled = Exp.collect_recall()
    assert recalled == ["apple", "banana"]

def test_analyze_recall():
    recalled = ["apple"]
    original = ["Apple", "Banana"]
    df = Exp.analyze_recall(recalled, original)
    assert df['Recalled'].sum() == 1


# Test Description:
# This script outlines how to test the Serial Position Memory Recall Task end-to-end.
# 1. Load a sample word bank file named 'word_bank.txt' with at least 20 words, each on a separate line.
# 2. Use generate_word_list(n) to randomly select 10 words from this word bank.
# 3. Use display_words() to sequentially present these words to the participant for a short time (e.g., 1.5 seconds each).
# 4. Use collect_recall() to allow the participant to type in recalled words after the list has been shown.
# 5. Use analyze_recall() to compare recalled words with the original list and generate recall accuracy by word position.
# This test will help ensure the program logic, input handling, and output formatting are functioning correctly.