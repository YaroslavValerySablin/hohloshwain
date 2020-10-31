from cx-Freeze import setup, Executable

setup(
    name = "Hex Generator",
    version = "0.1",
    description = "Generator Hex",
    executables = [Executable("hex_generator.py")]
)