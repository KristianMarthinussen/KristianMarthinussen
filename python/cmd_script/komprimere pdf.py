import sys
import fitz  # PyMuPDF

def compress_pdf(input_path, output_path, dpi=100):
    pdf = fitz.open(input_path)
    new_pdf = fitz.open()

    for page_num in range(len(pdf)):
        page = pdf.load_page(page_num)
        pix = page.get_pixmap(dpi=dpi)
        img_pdf = fitz.open("pdf", pix.tobytes("png"))
        new_pdf.insert_pdf(img_pdf)

    new_pdf.save(output_path)
    new_pdf.close()
    pdf.close()
    print(f"Compressed PDF saved to: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python komprimere pdf.py input.pdf output.pdf [dpi]")
        sys.exit(1)
    input_pdf = sys.argv[1]
    output_pdf = sys.argv[2]
    dpi = int(sys.argv[3]) if len(sys.argv) > 3 else 100
    compress_pdf(input_pdf, output_pdf, dpi)