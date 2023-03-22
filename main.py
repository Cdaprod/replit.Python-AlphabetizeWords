import tkinter as tk


class WordListGUI:

  def __init__(self, master):
    self.master = master
    self.master.title("Word List")

    # Create input field
    self.input_label = tk.Label(self.master, text="Enter a word:")
    self.input_label.pack()

    self.input_field = tk.Entry(self.master)
    self.input_field.pack()

    # Create submit button
    self.submit_button = tk.Button(self.master,
                                   text="Submit",
                                   command=self.add_word)
    self.submit_button.pack()

    # Create word list
    self.word_list = tk.Listbox(self.master)
    self.word_list.pack()

    # Create clear button
    self.clear_button = tk.Button(self.master,
                                  text="Clear",
                                  command=self.clear_list)
    self.clear_button.pack()

    # Create quit button
    self.quit_button = tk.Button(self.master,
                                 text="Quit",
                                 command=self.master.quit)
    self.quit_button.pack()

    # Initialize word list
    self.words = []

  def add_word(self):
    # Get word from input field
    word = self.input_field.get()

    # Add word to list
    self.words.append(word)

    # Clear input field
    self.input_field.delete(0, tk.END)

    # Sort word list
    self.words.sort()

    # Update word list on GUI
    self.update_word_list()

  def clear_list(self):
    # Clear word list
    self.words = []

    # Update word list on GUI
    self.update_word_list()

  def update_word_list(self):
    # Clear word list on GUI
    self.word_list.delete(0, tk.END)

    # Add words to word list on GUI
    for word in self.words:
      self.word_list.insert(tk.END, word)


# Create GUI window
root = tk.Tk()

# Create WordListGUI object
word_list_gui = WordListGUI(root)

# Run GUI
root.mainloop()
