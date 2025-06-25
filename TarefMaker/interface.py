import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('400x240')
        self.title('TarefMaker')

if __name__ == '__main__':
    app = App()
    app.mainloop()