import customtkinter as ctk
import cv2
import time
from PIL import Image, ImageTk
from FaceAuthentication import recognize_face
from commands import execute_command

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("AI Desktop Assistant")
app.geometry("1000x650")
app.resizable(False, False)

title = ctk.CTkLabel(app, text="AI Desktop Assistant", font=("Segoe UI", 28, "bold"))
title.pack(pady=20)

camera_frame = ctk.CTkFrame(app, width=640, height=480)
camera_frame.pack(pady=10)

camera_label = ctk.CTkLabel(camera_frame, text="")
camera_label.pack(fill="both", expand=True)

status = ctk.CTkLabel(app, text="Status : Initializing Camera...", font=("Segoe UI", 18))
status.pack(pady=15)

progress = ctk.CTkProgressBar(app, width=500)
progress.pack()
progress.set(0)

cap = cv2.VideoCapture(0)

match_start_time = None
required_match_seconds = 3
authenticated = False


def update_camera():
    global match_start_time, authenticated

    ret, frame = cap.read()

    if not ret:
        status.configure(text="Status : Camera not available")
        return

    matched, processed_frame, auth_status = recognize_face(frame)

    if matched:
        if match_start_time is None:
            match_start_time = time.time()

        elapsed = time.time() - match_start_time
        progress_value = min(elapsed / required_match_seconds, 1)
        progress.set(progress_value)

        status.configure(text=f"Status : Matching Identity... {int(progress_value * 100)}%")

        if elapsed >= required_match_seconds:
            authenticated = True
            status.configure(text="Status : Authentication Successful ✅")
            progress.set(1)

            cap.release()
            app.after(1500, start_assistant_screen)
            return
    else:
        match_start_time = None
        progress.set(0)
        status.configure(text=f"Status : {auth_status}")

    processed_frame = cv2.cvtColor(processed_frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(processed_frame)
    img = img.resize((640, 480))
    imgtk = ImageTk.PhotoImage(image=img)

    camera_label.imgtk = imgtk
    camera_label.configure(image=imgtk)

    app.after(10, update_camera)


def start_assistant_screen():
    camera_frame.pack_forget()
    progress.pack_forget()

    status.configure(text="Status : Assistant Ready ✅")

    welcome_label = ctk.CTkLabel(
        app,
        text="Welcome Rakshit\nType a command below",
        font=("Segoe UI", 24, "bold")
    )
    welcome_label.pack(pady=30)

    command_entry = ctk.CTkEntry(
        app,
        width=500,
        height=40,
        placeholder_text="Example: open google, open youtube, time, date"
    )
    command_entry.pack(pady=10)

    response_label = ctk.CTkLabel(
        app,
        text="Assistant response will appear here",
        font=("Segoe UI", 18)
    )
    response_label.pack(pady=20)

    def run_command():
        command = command_entry.get()
        result = execute_command(command)

        if result == "EXIT":
            app.destroy()
        else:
            response_label.configure(text=f"Assistant : {result}")

        command_entry.delete(0, "end")
    
    command_entry.bind("<Return>", lambda event: run_command())

    run_button = ctk.CTkButton(
        app,
        text="Run Command",
        width=200,
        command=run_command
    )
    run_button.pack(pady=10)


def on_close():
    cap.release()
    app.destroy()


app.protocol("WM_DELETE_WINDOW", on_close)

update_camera()
app.mainloop()