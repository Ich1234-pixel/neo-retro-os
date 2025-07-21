import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import winsound
import platform
import os
import random

def play_music_v2():
    path = filedialog.askopenfilename(title="Wähle WAV-Datei", filetypes=[("WAV Dateien", "*.wav")])
    if not path: return
    system = platform.system()
    if system == "Windows":
        winsound.PlaySound(path, winsound.SND_FILENAME | winsound.SND_ASYNC)
    else:
        os.system(f"afplay '{path}'")
    messagebox.showinfo("GrungeTunes", f"🎶 Musik gestartet:\n{os.path.basename(path)}")

def systeminfo():
    info = f"Betriebssystem: {platform.system()}\nVersion: {platform.version()}\nArchitektur: {platform.machine()}"
    messagebox.showinfo("📦 Systeminfo", info)

def spielhalle(): messagebox.showinfo("🕹️ Spielhalle", "Demoversion geladen... SPACE INVADERS kommt bald!")
def chatroom():
    chat = tk.Toplevel(root)
    chat.title("Chatroom")
    chat.geometry("400x300")
    log = tk.Text(chat, bg="black", fg="lime", font=("Courier", 10))
    log.pack()
    def send():
        msg = simpledialog.askstring("Dein Text", "Schreib was im Chat:")
        if msg: log.insert(tk.END, f"You: {msg}\nBot99: {random.choice(['LOL 😂', 'BRB', 'Retro detected'])}\n")
    tk.Button(chat, text="Message senden", command=send).pack()

def vhs_studio():
    vhs = tk.Toplevel(root)
    vhs.title("VHS Studio")
    vhs.geometry("350x250")
    tk.Label(vhs, text="🔄 Tracking-Störung aktiv!", font=("Courier", 12), fg="hotpink").pack(pady=10)
    for _ in range(10):
        tk.Label(vhs, text=random.choice(["█ ▒ ▓ ▄ ▀", "░ ░ ░ ░ ░", "▓ ▓ ▓ ▓ ▓"]), font=("Courier", 10), fg="gray").pack()

root = tk.Tk()
root.title("NeoRetro OS v2.0")
root.geometry("800x500")
root.configure(bg="#1e0033")
tk.Label(root, text="🌆 NeoRetro OS v2.0", font=("Courier", 24, "bold"), fg="#00ffee", bg="#1e0033").pack(pady=30)
frame = tk.Frame(root, bg="#1e0033"); frame.pack()

apps = {
    "🎧 Musikplayer": play_music_v2,
    "📟 Chatroom": chatroom,
    "🎞️ VHS Studio": vhs_studio,
    "🕹️ Spielhalle": spielhalle,
    "📦 Systeminfo": systeminfo,
    "🚪 Beenden": root.quit
}
colors = ["#ffaa00", "#00ffaa", "#ff00aa", "#33ccff", "#00ffff", "#ff3333"]

for i, (name, func) in enumerate(apps.items()):
    tk.Button(frame, text=name, font=("Courier", 14), width=25, bg=colors[i], fg="black",
              command=func).pack(pady=8)

root.mainloop()
