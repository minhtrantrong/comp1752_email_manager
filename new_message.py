import tkinter as tk
import tkinter.scrolledtext as tkst
import tkinter.messagebox as messagebox
import font_manager as fonts

# Define a New Message class:
class NewMessage:
    def __init__(self, window, sender):
        #Creat a window for New message
        self.window = window
        self.window.geometry("750x550")
        self.window.title(f"New message")

        # Create a sender label and property
        self.sender = sender
        sender_lbl = tk.Label(self.window, text=f"From: {self.sender}")
        sender_lbl.grid(row=0, column=0, sticky="E", padx=10, pady=10)

        self.recipient = ""
        recipient_lbl = tk.Label(self.window, text="To: ")
        recipient_lbl.grid(row=1, column=0, sticky="E", padx=10, pady=10)
        self.recipient_txt = tk.Entry(self.window, width=40)
        self.recipient_txt.grid(row=1, column=1, columnspan=6, sticky="W", padx=10, pady=10)

        self.cc = ""
        cc_lbl = tk.Label(self.window, text="CC: ")
        cc_lbl.grid(row=2, column=0, sticky="E", padx=10, pady=10)
        self.cc_txt = tk.Entry(self.window, width=40)
        self.cc_txt.grid(row=2, column=1, columnspan=6, sticky="W", padx=10, pady=10)

        self.bcc = ""
        bcc_lbl = tk.Label(self.window, text="BCC: ")
        bcc_lbl.grid(row=3, column=0, sticky="E", padx=10, pady=10)
        self.bcc_txt = tk.Entry(self.window, width=40)
        self.bcc_txt.grid(row=3, column=1, columnspan=6, sticky="W", padx=10, pady=10)

        subject_lbl = tk.Label(self.window, text="Subject:")
        subject_lbl.grid(row=4, column=0, sticky="E", padx=10, pady=10)
        self.subject_txt = tk.Entry(self.window, width=40)
        self.subject_txt.grid(row=4, column=1, columnspan=6, sticky="W", padx=10, pady=10)

        # Create the email body
        self.body_txt = tkst.ScrolledText(self.window, width=48, height=6, wrap="word")
        self.body_txt.grid(row=5, column=1, columnspan=6, sticky="W", padx=10, pady=10)

        # Create a send button
        send_btn = tk.Button(self.window, text="Send", command=self.send_email)
        send_btn.grid(row=6, column=6, sticky="W", padx=10, pady=10)

        # Create a cancel button
        cancel_btn = tk.Button(self.window, text="Cancel", command=self.cancel)
        cancel_btn.grid(row=6, column=7, sticky="W", padx=10, pady=10)

    def send_email(self):
        # get all entries: self.recipient, self.cc, self.bcc, self.body_txt
        recipient = self.recipient_txt.get().strip()
        cc = self.cc_txt.get().strip()
        bcc = self.bcc_txt.get().strip()
        subject = self.subject_txt.get().strip()
        body = self.body_txt.get("1.0", "end").strip()
        # Valiadate for at least one recipient
        if not recipient:
            messagebox.showwarning("Missing Recipient", "Please enter at least one recipient before sending.")
            return
        # Prepare a short summary to display in the confirmation dialog
        preview = body if len(body) <= 200 else body[:200] + "..."
        summary = f"To: {recipient}\nCC: {cc}\nBCC: {bcc}\nSubject: {subject}\n\n{preview}"
        # Ask the user to confirm sending
        if messagebox.askyesno("Send Email", f"Send this message?\n\n{summary}"):
            messagebox.showinfo("Sent", "Message sent.")
            # Close the compose window after sending
            self.window.destroy()
        return
    
    def cancel(self):
        # Ask for confirmation to cancel composing email
        if messagebox.askyesno("Confirm", "Are you sure you want to cancel? All unsaved changes will be lost."):
            # If confirmed, close the NewMessage window
            self.window.destroy()  # close the NewMessage window
        return
    
if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()  # create a TK object
    fonts.configure()  # configure the fonts
    new_msg = NewMessage(window, "minhtt21@fpt.edu.vn")  # open the NewMessage GUI
    window.mainloop() 