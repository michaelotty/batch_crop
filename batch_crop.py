"""Batch crop some PDF files.

Purpose of this script is to select a bunch of PDF files and collate them all
into one file. It also crops out the bottom half of every page for printing out
Royal Mail labels.
"""

import os
import tkinter
from pathlib import Path
from tkinter import filedialog

from PyPDF2 import PdfFileReader, PdfFileWriter


def batch_crop(file_names: list[str | Path] = None):
    """Batch crop a bunch of PDF files."""
    if not file_names:
        tkinter.Tk().withdraw()
        file_names = list(
            map(
                Path,
                filedialog.askopenfilenames(
                    title='Choose files to be cropped...',
                    filetypes=(('PDFs', '.pdf'), ))))

    writer = PdfFileWriter()

    for file_name in file_names:
        reader = PdfFileReader(str(file_name))
        for page_number in range(reader.getNumPages()):
            output_page = reader.getPage(page_number)
            output_page.mediaBox.lowerLeft = (
                0, output_page.mediaBox.getUpperLeft_y() / 2)
            writer.addPage(output_page)

    output_file_name = file_names[0].with_stem('cropped_labels')

    with open(output_file_name, 'wb') as file_object:
        writer.write(file_object)

    os.startfile(output_file_name)


if __name__ == '__main__':
    batch_crop()
