import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from runTool import run_tool

root = tk.Tk()
root.title("CIAMAKER")
root.geometry("600x300")
root.resizable(False, False)

elf_var = tk.StringVar()
output_var = tk.StringVar()

def browse_elf():
    file = filedialog.askopenfilename(
        title="Select ELF",
        filetypes=[("ELF Files", "*.elf"), ("All Files", "*.*")]
    )
    if file:
        elf_var.set(file)

def browse_output():
    folder = filedialog.askdirectory(title="Output Folder")
    if folder:
        output_var.set(folder)

def build():
    if not elf_var.get():
        messagebox.showerror("Error", "Select an ELF file.")
        return

    if not output_var.get():
        messagebox.showerror("Error", "Select an output folder.")
        return

    log.delete("1.0", tk.END)

    success, text = run_tool(
        elf_var.get(),
        output_var.get()
    )

    log.insert(tk.END, text)

    if success:
        messagebox.showinfo("Done", "Finished successfully.")
    else:
        messagebox.showerror("Failed", "Command returned an error.")

ttk.Label(root, text="ELF").pack(anchor="w", padx=10, pady=(10,0))
ttk.Entry(root, textvariable=elf_var, width=60).pack(padx=10)
ttk.Button(root, text="Browse", command=browse_elf).pack(padx=10, anchor="e")

ttk.Label(root, text="Output Folder").pack(anchor="w", padx=10)
ttk.Entry(root, textvariable=output_var, width=60).pack(padx=10)
ttk.Button(root, text="Browse", command=browse_output).pack(padx=10, anchor="e")

ttk.Button(root, text="Run Tool", command=build).pack(pady=10)

log = tk.Text(root, height=8)
log.pack(fill="both", expand=True, padx=10, pady=10)

root.mainloop()
