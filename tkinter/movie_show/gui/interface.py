import tkinter as tk
from tkinter import filedialog
from tkinter import ttk


class Window:

    def __init__(self, database, parser):
        # Inject interface for database and parser
        self.database = database
        self.parser = parser

    def mainloop(self):
        # Create the main application window
        root = tk.Tk()
        root.title("File Browser and Save State")

        # TODO:
        # Za `open_button` i `load_from_database` widget button-e,
        # dodajte akciju na `click` gdje se zovu pripadajuce metode:
        # `open_file_browser` i `load_from_db`.
        # Create and configure widgets
        self.open_button = tk.Button(root, text="Load from file",command=self.open_file_browser)
        self.load_from_database = tk.Button(root, text="Load from database",command=self.load_from_db)

        # Create a Treeview widget with two columns
        columns = ("Movie Title", "Year")
        self.tree = ttk.Treeview(root, columns=columns, show="headings")

        # Set column headers
        self.tree.heading("Movie Title", text="Movie Title")
        self.tree.heading("Year", text="Year")

        # Create a vertical scrollbar and associate it with the table
        self.vsb = ttk.Scrollbar(root,
                                 orient="vertical",
                                 command=self.tree.yview)

        self.tree.configure(yscrollcommand=self.vsb.set)

        # Pack widgets to the window
        self.open_button.pack()
        self.load_from_database.pack()
        self.tree.pack(side="left", fill="both", expand=True)
        self.vsb.pack(side="right", fill="y")

        # Start the main event loop
        root.mainloop()

    # Method to open a file dialog and get the selected file's path
    def open_file_browser(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.tree.delete(*self.tree.get_children())
            data = self.parser.parse(file_path)
            data = map(lambda x: (x.title, x.year), data)
            # Insert data into the table
            for item in data:
                self.tree.insert("", "end", values=item)

    # Method to load data from database
    def load_from_db(self):
        self.tree.delete(*self.tree.get_children())
        data = self.database.movies()
        data = map(lambda x: (x.title, x.year), data)

        # Insert data into the table
        for item in data:
            self.tree.insert("", "end", values=item)
