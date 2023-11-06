import customtkinter as ctk
import subprocess

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("500x350")
root.title("MathVis")


def log_in():
    file_to_execute = "Visualize.py"
    arguments = ["arg1", "arg2", "arg3"]
    try:
        result = subprocess.run(["python", file_to_execute] + arguments, capture_output=True, text=True, check=True)
        print("External script output:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"External script returned an error code: {e.returncode}")
        print("Error output:")
        print(e.stderr)


frame = ctk.CTkFrame(master=root)
frame.pack(fill="both", expand=True)

title = ctk.CTkLabel(master=frame, text="Visualize Integrals", font=("", 20))
title.pack(pady=12, padx=10)

input_frame = ctk.CTkFrame(master=frame, width=400, height=40)
input_frame.pack()

integral_unicode = '\u222B'

integral_label = ctk.CTkLabel(master=input_frame, text=u'{integral_unicode}'.format(
    integral_unicode=integral_unicode), font=("", 30))
# integral_label.pack(padx=0,side="left")
integral_label.place(x=13, y=4)

entry2 = ctk.CTkEntry(master=input_frame, placeholder_text="e.g. 5x+3")
entry2.pack(pady=12, padx=30)

button = ctk.CTkButton(master=frame, command=log_in, text="Submit")
button.pack(pady=12)

root.mainloop()
