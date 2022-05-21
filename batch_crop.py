"""Batch crop some files."""

import tkinter
from pathlib import Path
from tkinter import filedialog

from PyPDF2 import PdfFileReader, PdfFileWriter


def main():
    """Program starts here."""
    tkinter.Tk().withdraw()
    file_names = map(
        Path,
        filedialog.askopenfilenames(title='Choose files to be cropped...',
                                    filetypes=(('PDFs', '.pdf'), )))

    for file_name in file_names:
        reader = PdfFileReader(str(file_name))
        output_page = reader.getPage(0)
        print(output_page.mediaBox)
        output_page.mediaBox.lowerLeft = (
            0, output_page.mediaBox.getUpperLeft_y() / 2)
        writer = PdfFileWriter()
        writer.addPage(output_page)

        with open(file_name.with_stem('cropped_' + file_name.stem), 'wb') as f:
            writer.write(f)


if __name__ == '__main__':
    main()
