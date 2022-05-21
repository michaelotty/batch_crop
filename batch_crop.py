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

    file_names = list(file_names)

    writer = PdfFileWriter()

    for file_name in file_names:
        reader = PdfFileReader(str(file_name))
        for page_number in range(reader.getNumPages()):
            output_page = reader.getPage(page_number)
            output_page.mediaBox.lowerLeft = (
                0, output_page.mediaBox.getUpperLeft_y() / 2)
            writer.addPage(output_page)

    with open(file_names[0].with_stem('cropped_labels'), 'wb') as f:
        writer.write(f)


if __name__ == '__main__':
    main()
