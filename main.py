import tkinter as tk
from tkinter import filedialog, messagebox
from makeCia import make_cia
import os


class CiaMaker:

    def __init__(self, root):
        self.root = root
        self.root.title("CIAMAKER")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        self.elf = ""
        self.rsf = ""

        tk.Label(
            root,
            text="CIAMAKER",
            font=("Arial", 22, "bold")
        ).pack(pady=10)

        tk.Label(
            root,
            text="A simple CIA file creator"
        ).pack()


        # ELF
        tk.Button(
            root,
            text="Select ELF",
            command=self.select_elf
        ).pack(pady=10)

        self.elf_label = tk.Label(
            root,
            text="ELF: Not selected"
        )
        self.elf_label.pack()


        # RSF
        tk.Button(
            root,
            text="Select RSF",
            command=self.select_rsf
        ).pack(pady=10)

        self.rsf_label = tk.Label(
            root,
            text="RSF: Not selected"
        )
        self.rsf_label.pack()


        # Create
        tk.Button(
            root,
            text="BUILD CIA",
            font=("Arial", 12, "bold"),
            command=self.build
        ).pack(pady=15)


        # Log
        self.log = tk.Text(
            root,
            height=8,
            width=70
        )
        self.log.pack(pady=10)


    def select_elf(self):
        file = filedialog.askopenfilename(
            title="Choose ELF",
            filetypes=[
                ("ELF file", "*.elf"),
                ("All files", "*.*")
            ]
        )

        if file:
            self.elf = file
            self.elf_label.config(
                text="ELF: " + file
            )


    def select_rsf(self):
        file = filedialog.askopenfilename(
            title="Choose RSF",
            filetypes=[
                ("RSF file", "*.rsf"),
                ("All files", "*.*")
            ]
        )

        if file:
            self.rsf = file
            self.rsf_label.config(
                text="RSF: " + file
            )


    def build(self):

        if not self.elf:
            messagebox.showerror(
                "Error",
                "Select an ELF file first."
            )
            return

        if not self.rsf:
            messagebox.showerror(
                "Error",
                "Select an RSF file first."
            )
            return


        self.log.delete(
            "1.0",
            tk.END
        )

        self.log.insert(
            tk.END,
            "Building CIA...\n"
        )

        success, result = make_cia(
            self.elf,
            self.rsf
        )

        self.log.insert(
            tk.END,
            result
        )


        if success:
            messagebox.showinfo(
                "CIAMAKER",
                "CIA created in ELF folder!"
            )


root = tk.Tk()

app = CiaMaker(root)

root.mainloop()
