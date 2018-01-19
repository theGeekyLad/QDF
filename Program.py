import img2pdf
import pathlib

path = pathlib.Path('.')

snaps = []
for file in path.iterdir():
    if file.is_file() and not(file.name.endswith('.py')):
        print("Analysing file:", file.name, "...")
        snaps.append(file.name)

snaps.sort()
qdf = open("out.pdf", "wb")
qdf.write(img2pdf.convert(snaps))

print("\nDone.")
