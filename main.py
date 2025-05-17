from src.exp import Exp
from src.gui import GUI

def main():
    gui = GUI()
    Exp.run_experiment(gui)
    gui.root.mainloop()

if __name__ == "__main__":
    main()