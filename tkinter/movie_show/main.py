from gui.interface import Window
from csv_parser.parser import Parser
from database.view import View


gui = Window(View('test_data/movies.db'), Parser())
gui.mainloop()
