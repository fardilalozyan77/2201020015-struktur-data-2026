import os
def main():
    # Baca file jawaban.txt
    with open('jawaban.txt', 'r') as file:
        jawaban = file.read().strip()
    
    # Simpan jawaban ke dalam file jawaban_output.txt
    with open('jawaban_output.txt', 'w') as output_file:
        output_file.write(jawaban)