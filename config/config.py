class Config:
    word_bank = [
        "Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape",
        "Honeydew", "Kiwi", "Lemon", "Mango", "Nectarine", "Orange", "Papaya",
        "Quince", "Raspberry", "Strawberry", "Tangerine", "Ugli", "Vanilla",
        "Watermelon", "Xigua", "Yam", "Zucchini", "Art", "Ball", "Cat", "Dog",
        "Elephant", "Fish", "Guitar", "House", "Island", "Jungle", "Kite",
        "Lamp", "Mountain", "Notebook", "Ocean", "Pencil", "Queen", "River",
        "Sun", "Tree", "Umbrella", "Violin", "Window", "Xylophone", "Yogurt",
        "Zoo", "Ambition", "Bravery", "Creativity", "Determination", "Empathy",
        "Fortitude", "Generosity", "Hope", "Integrity", "Joy", "Kindness",
        "Love", "Mindfulness", "Nobility", "Optimism", "Perseverance",
        "Quality", "Resilience", "Strength", "Unity", "Valor", "Wisdom", "Zeal",
        "Artful", "Bliss", "Calm", "Delight", "Energy", "Freedom", "Grace",
        "Harmony", "Inspiration", "Justice", "Knowledge", "Light", "Melody",
        "Nature", "Openness", "Passion", "Quiet", "Respect", "Serenity", "Trust",
        "Understanding", "Vibrancy", "Wonder", "X-factor", "Youth", "Zest",
        "Abstract"
    ]
    num_words = 20

    window_width = 800
    window_height = 600

    stimulus_time = 1.0     
    isi_time = 0.5          
    instruction_delay = 1000

    intro_text = (
        """The serial position effect describes the tendency to recall the first and last items in a list better than the middle items. 
        This experiment is meant to demosntrate this effect. You will see a series of words, one at a time.
        Try to remember as many as you can. After all words have appeared, you’ll be asked
        to type in all the words you recall, separated by spaces.
        Press Enter when you’re ready to begin."""
    )