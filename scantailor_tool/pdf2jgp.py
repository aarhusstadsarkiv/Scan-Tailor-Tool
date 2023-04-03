import locale
from gooey import Gooey, GooeyParser
from pathlib import Path
import sys, fitz


__version__ = "1.0"


def pdf2png(PDF_path: Path, output_endpoint: Path) -> None:
    """
    Converts PDF from the PDF_path to .jpg files to the output_endpoint.

    Parameters
        PDF_path: Path to PDF
        output_endpoint: Folder which the .jpg files will end up it
    
    Returns:
        None
    
    """
    doc = fitz.open(PDF_path)
    for index, page in enumerate(doc):
        # render page to an image
        pix = page.get_pixmap()
        pix.save(f"{output_endpoint}\\page-{page.number}.jpg")

        print("progress: {}/{}".format(index + 1, len(doc)))


def check_pdf(PDF_path: Path) -> Path:
    """
    Check if the given path is a PDF. If not, then it will raise a ValueError
    Gooey's Dynamic Validation don't work

    Parameters
        PDF_path: Path to PDF
    
    Returns
        PDF_path: Path to PDF
    
    Raises
        ValueError: If the given path is not to a PDF
    """
    if PDF_path[-4:] == '.pdf':
        return PDF_path
    else:
        print("="*15)
        print("\n"*3)
        print("Your file needs to be a PDF")
        print("\n"*3)
        print("="*15)
        raise ValueError


@Gooey(
    program_name='PDF to JPG version {__version__}',
    default_size=(800, 700),
    show_restart_button=False,
    encoding=locale.getpreferredencoding(),
    show_failure_modal=False,
    show_success_modal=False,
) 
def main():
    parser = GooeyParser(description='First out of three step for spliting double pages PDF')
    input = parser.add_argument_group(
        "input", 
    )
    output = parser.add_argument_group(
        "Output", 
    )


    input.add_argument(
        'PDF_path',
        metavar="PDF path",
        widget="FileChooser",
        help='PDF-file which you want to use Scan Tailor to split double pages',
        type=check_pdf,
    ) 
    
    output.add_argument(
        'output_path',
        metavar="Output path",
        widget="DirChooser",
        help='Directory to out images to.',
        type=Path,
    ) 

    args = parser.parse_args()

    # Run conversion
    pdf2png(args.PDF_path, args.output_path)
    print(f"Successfully Converte PDF to .jpg files at {args.output_path}", flush=True)


if __name__ == "__main__":
    main()