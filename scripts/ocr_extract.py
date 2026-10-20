#!/usr/bin/env python3
import subprocess
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# extracted/textbook/unitNN/page-N.png (300 dpi) and extracted/textbook/unitNN.txt (tesseract kor+eng)
output_dir = os.path.join(ROOT, 'extracted', 'textbook')
img_dir = output_dir
os.makedirs(output_dir, exist_ok=True)
os.makedirs(img_dir, exist_ok=True)

# Units to process: `python3 scripts/ocr_extract.py 14 15 16` or all of them by default.
UNITS = [int(a) for a in sys.argv[1:]] or list(range(5, 23))

for unit in UNITS:
    pdf_path = os.path.join(ROOT, 'source', 'textbook',
                            f"KMU student's book unit {unit:02d}.pdf")
    unit_img_dir = os.path.join(img_dir, f'unit{unit:02d}')
    os.makedirs(unit_img_dir, exist_ok=True)
    
    # Convert PDF to images using pdftoppm
    print(f"Converting Unit {unit}...")
    subprocess.run([
        'pdftoppm', '-png', '-r', '300',
        pdf_path,
        os.path.join(unit_img_dir, 'page')
    ], check=True)
    
    # OCR each page
    all_text = []
    pages = sorted([f for f in os.listdir(unit_img_dir) if f.endswith('.png')])
    for page_file in pages:
        page_path = os.path.join(unit_img_dir, page_file)
        result = subprocess.run([
            'tesseract', page_path, 'stdout',
            '-l', 'kor+eng',
            '--psm', '6'
        ], capture_output=True, text=True)
        page_num = page_file.replace('page-', '').replace('.png', '')
        all_text.append(f"--- Page {page_num} ---")
        all_text.append(result.stdout)
    
    # Save output
    out_path = os.path.join(output_dir, f'unit{unit:02d}.txt')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(all_text))
    print(f"Unit {unit}: {len(pages)} pages OCR'd -> {out_path}")

print("All done!")
