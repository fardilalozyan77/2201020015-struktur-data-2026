import os
import pandas as pd

def main():
    # Baca file jawaban.txt
    with open('jawaban.txt', 'r') as file:
        jawaban = file.read().strip()
    
    # Simpan jawaban ke dalam file jawaban_output.txt
    with open('jawaban_output.txt', 'w') as output_file:
        output_file.write(jawaban) 
        # Simpan jawaban ke dalam file jawaban_output.csv
    df = pd.DataFrame({'Jawaban': [jawaban]})
    df.to_csv('jawaban_output.csv', index=False)
    
if __name__ == "__main__":    main()
