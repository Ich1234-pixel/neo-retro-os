import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
import winsound  # Nur für Windows
import platform
import os
import random

# 🎶 Musikplayer für WAV-Dateien
def play_selected_music():
    system = platform.system()
    filepath = filedialog.askopenfilename(
        title="Wähle deine WAV-Datei",
        filetypes=[("WAV Dateien", "*.wav")]
    )
    if not filepath:
        return

    if system == "Windows":
        try:
            winsound.PlaySound(filepath, winsound.SND_FILENAME | winsound.SND_ASYNC)
            messagebox.showinfo("GrungeTunes", "🎶 Deine Musik wird gespielt!")
        except RuntimeError:
            messagebox.showerror("Fehler", "Konnte WAV-Datei nicht abspielen.")
    else:
        try:
            os.system(f"afplay '{filepath}'")  # macOS
        except:
            messagebox.showerror("Nicht unterstützt", "Musikplayer funktioniert nur mit WAV auf diesem System.")

# 🕹️ Spielhalle (Demo)
def spielhalle():
    win = tk.Toplevel(root)
    win.title("Spielhalle")
    win.geometry("300x150")
    tk.Label(win, text="🕹️ SPACE INVADERS INCOMING!", font=("Courier", 14)).pack(pady=20)

# 💬 Chatroom 1999
def chatroom():
    chat = tk.Toplevel(root)
    chat.title("Chatroom 1999")
    chat.geometry("400x300")
    log = tk.Text(chat, bg="black", fg="lime", font=("Courier", 10))
    log.pack()
    def send():
        msg = simpledialog.askstring("Dein Text", "Was willst du sagen?")
        if msg:
            bot = random.choice(["LOL same 😂", "AOL_Bot: You've got mail!", "hahaha classic"])
            log.insert(tk.END, f"You: {msg}\nUser1999: {bot}\n")
    tk.Button(chat, text="Send Message", command=send).pack(pady=10)

# 📼 VHS Studio
def vhs_studio():
    studio = tk.Toplevel(root)
    studio.title("VHS Studio")
    studio.geometry("350x250")
    tk.Label(studio, text="🔄 Tracking-Modus aktiv!", font=("Courier", 12), fg="#ff00aa").pack(pady=20)
    for _ in range(15):
        glitch = random.choice(["█ ▒ ▓ ▄ ▀", "▓ ▓ ▓ ▓ ▓", "░ ░ ░ ░ ░"])
        tk.Label(studio, text=glitch, font=("Courier", 10), fg="gray").pack()

# 💥 Fake-Bluescreen
def show_bluescreen():
    bs = tk.Toplevel(root)
    bs.title("NeoRetro OS – Fatal Error")
    bs.geometry("800x500")
    bs.configure(bg="blue")

    tk.Label(bs, text="NeoRetro OS", font=("Courier", 20, "bold"), fg="white", bg="blue").pack(pady=20)

    error_msg = (
        "Ein Problem wurde festgestellt und NeoRetro OS wurde heruntergefahren, um Schäden zu vermeiden.\n\n"
        "BAD_RETRO_MODE_EXCEPTION\n\n"
        "Wenn Sie diese Fehlermeldung zum ersten Mal sehen, starten Sie das System neu.\n"
        "Wenn dieser Bildschirm erneut erscheint, folgen Sie diesen Schritten:\n\n"
        "• Entfernen Sie alle Disketten oder VHS-Kassetten.\n"
        "• Führen Sie CHKRETRO /F aus, um Glitches zu prüfen.\n"
        "• Hören Sie Musik der 80er zur Beruhigung.\n\n"
        "Technische Informationen:\n"
        "*** STOP: 0x0000008E (0xC0000005, 0x80500000, 0x00000000, 0x00000000)"
    )

    tk.Label(bs, text=error_msg, font=("Courier", 10), fg="white", bg="blue", justify="left").pack(padx=20, pady=10)
    tk.Button(bs, text="🔁 Neustart", font=("Courier", 12), bg="white", fg="blue", command=bs.destroy).pack(pady=20)

# 🌆 Hauptoberfläche
root = tk.Tk()
root.title("NeoRetro OS")
root.geometry("800x500")
root.configure(bg="#1a0033")

tk.Label(root, text="🌆 NeoRetro OS", font=("Courier", 24, "bold"), fg="#00ffee", bg="#1a0033").pack(pady=30)

btn_frame = tk.Frame(root, bg="#1a0033")
btn_frame.pack()

# 🔘 App-Verzeichnis
apps = {
    "🕹️ Spielhalle": spielhalle,
    "🎧 Eigene Musik abspielen": play_selected_music,
    "📟 Chatroom 1999": chatroom,
    "🎞️ VHS Studio": vhs_studio,
    "💥 Bluescreen auslösen": show_bluescreen,
    "🚪 Beenden": root.quit
}
colors = ["#ff00aa", "#ffaa00", "#00ffaa", "#33ccff", "#3399ff", "#ff3333"]

for i, (app_name, app_func) in enumerate(apps.items()):
    tk.Button(btn_frame, text=app_name, font=("Courier", 14), bg=colors[i], fg="black",
              width=25, pady=5, command=app_func).pack(pady=10)

root.mainloop()
