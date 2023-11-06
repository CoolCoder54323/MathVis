import customtkinter

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")


def log_in():
    print("test")


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=20, fill="both", expand=True)

Title = customtkinter.CTkLabel(master=frame, text="Visualize Integrals")
Title.pack(pady=12,padx=10,)

entry2 = customtkinter.CTkEntry(master=frame,placeholder_text="e.g. 5x+3")
entry2.pack(pady=12,padx=10)

button = customtkinter.CTkButton(master=frame,command=log_in,text="Submit")
button.pack()

root.mainloop()