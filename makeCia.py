import subprocess
import os


def make_cia(elf_file, rsf_file, output_file):
    makerom = "tools/makerom.exe"

    if not os.path.exists(makerom):
        return False, "makerom.exe não encontrado."

    if not os.path.exists(elf_file):
        return False, "Arquivo ELF não encontrado."

    if not os.path.exists(rsf_file):
        return False, "Arquivo RSF não encontrado."

    command = [
        makerom,
        "-f",
        "cia",
        "-o",
        output_file,
        "-elf",
        elf_file,
        "-rsf",
        rsf_file
    ]

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True
        )

        log = result.stdout + "\n" + result.stderr

        if result.returncode == 0:
            return True, "CIA criado com sucesso!\n\n" + log
        else:
            return False, "Erro ao criar CIA:\n\n" + log

    except Exception as e:
        return False, f"Erro: {e}"
