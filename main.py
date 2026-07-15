import tkinter as tk
from tkinter import filedialog, messagebox
from makeCia import make_cia
import os


class CiaMakerApp:

    def __init__(self, root):
        self.root = root
        self.root.title("CIAMAKER")
        self.root.geometry("650x420")
        self.root.resizable(False, False)

        self.elf_file = ""
        self.rsf_file = ""

        title = tk.Label(
            root,
            text="CIAMAKER\nA simple CIA Creator",
            font=("Arial", 18, "bold")
        )
        title.pack(pady=15)


        # ELF
        tk.Label(root, text="ELF File:").pack(anchor="w", padx=20)

        self.elf_label = tk.Label(
            root,
            text="No file selected",
            relief="sunken",
            width=70
        )
        self.elf_label.pack(padx=20)

        tk.Button(
            root,
            text="Select ELF",
            command=self.select_elf
        ).pack(pady=5)


        # RSF
        tk.Label(root, text="RSF File:").pack(anchor="w", padx=20)

        self.rsf_label = tk.Label(
            root,
            text="No file selected",
            relief="sunken",
            width=70
        )
        self.rsf_label.pack(padx=20)

        tk.Button(
            root,
            text="Select RSF",
            command=self.select_rsf
        ).pack(pady=5)


        # Output
        tk.Label(root, text="Output CIA:").pack(anchor="w", padx=20)

        self.output = tk.Entry(root, width=70)
        self.output.insert(0, "output/app.cia")
        self.output.pack(padx=20)


        # Build
        tk.Button(
            root,
            text="CREATE CIA",
            font=("Arial", 12, "bold"),
            command=self.create
        ).pack(pady=15)


        # Log
        self.log = tk.Text(
            root,
            height=8
        )
        self.log.pack(
            fill="both",
            padx=20,
            pady=5
        )


    def select_elf(self):
        file = filedialog.askopenfilename(
            filetypes=[
                ("ELF Files", "*.elf"),
                ("All Files", "*.*")
            ]
        )

        if file:
            self.elf_file = file
            self.elf_label.config(text=file)


    def select_rsf(self):
        file = filedialog.askopenfilename(
            filetypes=[
                ("RSF Files", "*.rsf"),
                ("All Files", "*.*")
            ]
        )

        if file:
            self.rsf_file = file
            self.rsf_label.config(text=file)


    def create(self):

        if not self.elf_file or not self.rsf_file:
            messagebox.showerror(
                "Error",
                "Select ELF and RSF first."
            )
            return


        output = self.output.get()

        os.makedirs(
            os.path.dirname(output),
            exist_ok=True
        )

        success, msg = make_cia(
            self.elf_file,
            self.rsf_file,
            output
        )

        self.log.delete(
            "1.0",
            tk.END
        )

        self.log.insert(
            tk.END,
            msg
        )


        if success:
            messagebox.showinfo(
                "CIAMAKER",
                "CIA created!"
            )


root = tk.Tk()
app = CiaMakerApp(root)
root.mainloop()
