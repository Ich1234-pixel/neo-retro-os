import tkinter as tk
from tkinter import filedialog, messagebox
import platform
import os

def play_media_v3():
    path = filedialog.askopenfilename(
        title="Medien auswählen",
        filetypes=[("Medien-Dateien", "*.mp3 *.wav *.mp4 *.m4a *.mov *.avi *.flac *.mkv"), ("Alle Dateien", "*.*")]
    )
    if not path: return
    system = platform.system()
    if system == "Windows":
        os.system(f'start "" "{path}"')
    elif system == "Darwin":
        os.system(f'open "{path}"')
    elif system == "Linux":
        os.system(f'xdg-open "{path}"')
    else:
        messagebox.showerror("Fehler", "Unbekanntes Betriebssystem.")
    messagebox.showinfo("NeoRetro OS v3.1", f"📂 Datei geöffnet:\n{os.path.basename(path)}")

def bluescreen():
    bs = tk.Toplevel(root)
    bs.title("Systemfehler")
    bs.geometry("800x500")
    bs.configure(bg="blue")
    tk.Label(bs, text="NeoRetro OS", font=("Courier", 20, "bold"), bg="blue", fg="white").pack(pady=20)
    msg = (
        "Ein Problem wurde festgestellt und NeoRetro OS wurde heruntergefahren...\n\n"
        "BAD_RETRO_MODE_EXCEPTION\n\n"
        "Technische Infos:\n*** STOP: 0x0000008E (0xC0000005, 0x80500000)\n\n"
        "Drücke Neustart, um das System neu zu laden."
    )
    tk.Label(bs, text=msg, font=("Courier", 10), bg="blue", fg="white", justify="left").pack(padx=30, pady=10)
    tk.Button(bs, text="🔁 Neustart", font=("Courier", 12), bg="white", fg="blue", command=bs.destroy).pack(pady=20)

root = tk.Tk()
root.title("NeoRetro OS v3.1")
root.geometry("800x500")
root.configure(bg="#000022")

tk.Label(root, text="🌌 NeoRetro OS v3.1", font=("Courier", 24, "bold"), fg="#00ffff", bg="#000022").pack(pady=30)
tk.Label(root, text="✨ Willkommen im interaktiven Retro-Universum!", font=("Courier", 14), fg="#ffcc00", bg="#000022").pack(pady=10)

tk.Button(root, text="🎶 Medien öffnen", font=("Courier", 14), width=30, bg="#00ffaa", fg="black",
          command=play_media_v3).pack(pady=20)

tk.Button(root, text="💥 Bluescreen auslösen", font=("Courier", 14), width=30, bg="#ff3333", fg="white",
          command=bluescreen).pack(pady=10)

tk.Button(root, text="🚪 Beenden", font=("Courier", 12), bg="#ff0099", fg="white", command=root.quit).pack(pady=10)

root.mainloop()
