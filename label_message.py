import tkinter as tk
import tkinter.scrolledtext as tkst
import font_manager as fonts
import message_manager as mm

class LabelMessage:
    def __init__(self, window):
        self.messages = mm.messages

        # Create window for Label Message
        self.window = window
        self.window.geometry("800x600")
        self.window.title(f"Label messages")
        # Create a list all labeled messages button
        list_messages_btn = tk.Button(self.window, text="List All Messages Labeled", command=self.list_lbl_messages)
        list_messages_btn.grid(row=0, column=0, sticky="W", padx=10, pady=10)
        # Label entry
        self.label_txt = tk.Entry(self.window, width=4)
        self.label_txt.grid(row=0, column=1, sticky="W", padx=10, pady=10)
        # Add label button
        label_btn = tk.Button(self.window, text="Add Label To Message", command=self.add_label)
        label_btn.grid(row=0, column=2, sticky="W", padx=10, pady=10)
        # Message ID entry
        self.label_txt = tk.Entry(self.window, width=4)
        self.label_txt.grid(row=0, column=3, sticky="W", padx=4, pady=10)
        # Close button
        close_btn = tk.Button(self.window, text="Close", command=self.clase_window)
        close_btn.grid(row=0, column=4, sticky="W", padx=10, pady=10)
        # listbox to show messages
        self.msg_list_txt = tkst.ScrolledText(self.window, width=90, height=25, wrap="word")
        self.msg_list_txt.grid(row=1, column=0, columnspan=5, sticky="W", padx=10, pady=10)

    def list_lbl_messages(self):
        # Use the message_manager.list_all function to get formatted output
        try:
            output = mm.list_all()
        except Exception:
            output = "Error retrieving messages."

        # Clear the text area and insert the output
        self.msg_list_txt.delete("1.0", "end")
        self.msg_list_txt.insert("1.0", output)
        return
    
    def add_label(self):
        return
    
    def clase_window(self):
        self.window.destroy()
        return
    
if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()  # create a TK object
    fonts.configure()  # configure the fonts
    label_msg = LabelMessage(window)  # open the LabelMessage GUI
    window.mainloop()