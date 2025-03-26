def code_xored_file(filename):
    try:
        # Otwieramy plik w trybie binarnym
        with open(filename, 'rb') as f:
            content = f.read()
            
            if len(content) == 0:
                print("Plik jest pusty!")
                return None
            
            # Obliczamy sumę kontrolną całego pliku
            checksum = sum(content) & 0xFF
            print(f"Odczytana suma kontrolna (hex): {hex(checksum)}")
            
            # Wykonujemy operację XOR na zawartości używając sumy kontrolnej
            coded_content = bytes([b ^ checksum for b in content])
            
            # Tworzymy nową zawartość z checksumem jako pierwszym bajtem
            final_content = bytes([checksum]) + coded_content
            
            # Zapisujemy zakodowane dane do nowego pliku
            output_filename = filename.replace('_xored.dat', '_coded.dat')
            with open(output_filename, 'wb') as out_file:
                out_file.write(final_content)
            print(f"Zapisano odkodowane dane do: {output_filename}")
            
            return final_content
            
    except FileNotFoundError:
        print(f"Nie znaleziono pliku: {filename}")
        return None
    except Exception as e:
        print(f"Wystąpił błąd: {str(e)}")
        return None

# Użycie funkcji
file_path = "d:\\Skoki Narciarskie 2002\\Mat\\003_xored.dat"
coded_data = code_xored_file(file_path)
