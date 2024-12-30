import os
import PyPDF2

def pdf_to_txt(input_folder, output_folder="bugTXTs"):
    #create output folder if DNE
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    #iterate through all input files
    for filename in os.listdir(input_folder):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(input_folder, filename)

            #extract text
            try:
                with open(pdf_path, "rb") as pdf_file:
                    reader = PyPDF2.PdfReader(pdf_file)
                    text = ""
                    for page in reader.pages:
                        text += page.extract_text()

                #make the output .txt
                txt_filename = os.path.splitext(filename)[0] + ".txt"
                txt_path = os.path.join(output_folder, txt_filename)

                #write text to the .txt file
                with open(txt_path, "w", encoding="utf-8") as txt_file:
                    txt_file.write(text)

                #success
                print(f"Converted: {filename} -> {txt_filename}")

            except Exception as e:
                print(f"Error processing {filename}: {e}")


pdf_folder_path = "path/to/PDFS"
pdf_to_txt(pdf_folder_path)
