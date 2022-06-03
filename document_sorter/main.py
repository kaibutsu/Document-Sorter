import pathlib
from black import out
import pdfplumber
import logging

FORMAT = '%(asctime)-15s - %(levelname)s - %(name)s: %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)
logger = logging.getLogger(__name__)

def main(indir:str="tests/pdf", outdir:str="tests/out") -> int:
    indir_path = pathlib.Path(indir)
    outdir_path = pathlib.Path(outdir)
    logger.info("Filing files from '%s' to '%s'", indir_path.absolute(), outdir_path.absolute())
    all_pdfs = [f for f in indir_path.iterdir() if f.suffix.lower() == ".pdf"]
    for pdf_file in all_pdfs:
        logger.debug("Processing file %s", pdf_file)
        with pdfplumber.open(pdf_file) as pdf_object:
            print(pdf_object.metadata)

if __name__ == "__main__":
    main()