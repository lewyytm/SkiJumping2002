def calculate_checksum(filename):
    try:
        # Otwieramy plik w trybie binarnym
        with open(filename, 'rb') as f:
            content = f.read()
            
            if len(content) == 0:
                print("Plik jest pusty!")
                return None
                
            
            first_byte = content[0]
            print(f"Pierwszy bajt (hex): {hex(first_byte)}")
            
            xored_content = bytes([b ^ first_byte for b in content[1:]])
            
            # Zapisujemy przekształcone dane do nowego pliku
            output_filename = filename.replace('.dat', '_xored.dat')
            with open(output_filename, 'wb') as out_file:
                out_file.write(xored_content)
            print(f"Zapisano przekształcone dane do: {output_filename}")
            
            checksum = sum(xored_content) & 0xFF

            return checksum
            
    except FileNotFoundError:
        print(f"Nie znaleziono pliku: {filename}")
        return None
    except Exception as e:
        print(f"Wystąpił błąd: {str(e)}")
        return None

# Użycie funkcji
file_path = "d:\\Skoki Narciarskie 2002\\Mat\\003.dat"
checksum = calculate_checksum(file_path)
