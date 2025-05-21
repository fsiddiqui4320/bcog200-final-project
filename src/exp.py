import pandas as pd
import random
from config.config import Config
import matplotlib.pyplot as plt

class Exp:
    def generate_word_list(n, word_bank):
        return random.choices(word_bank, k=n)

    def analyze_recall(recalled, original):
        results = []
        correct = 0
        for w in original:
            was = w.lower() in recalled
            if was:
                correct += 1
            results.append({'Word': w, 'Recalled': was})
        df = pd.DataFrame(results)
        print(df)
        print(f"\nTotal Recall Accuracy: {correct/len(original):.2%}")
        return df

    def plot_recall(df):
        plt.figure(figsize=(10,6))
        plt.bar(df['Word'], df['Recalled'].astype(int))
        plt.xlabel('Words')
        plt.ylabel('Recalled (1 = Yes, 0 = No)')
        plt.title('Recall by Position')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def run_experiment(gui):
        gui.show_instructions(Config.intro_text)
        words = Exp.generate_word_list(Config.num_words, Config.word_bank)
        for w in words:
            gui.show_stimulus(w)
        recalled = gui.show_recall_prompt()
        df = Exp.analyze_recall(recalled, words)
        Exp.plot_recall(df)