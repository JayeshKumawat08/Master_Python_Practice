def secure_file_loader(filename):
    print(f"Attempting to load {filename}")

    try:
        with open(filename,'r') as file:
            data = file.read()

    except FileNotFoundError:
        print(f"The file {filename} not found in the directory")

    except PermissionError:
        print(f"You do not have admin rights to read {filename}")

    except Exception as e:
        print(f"Unknown ERROR: {e}")

    else:
        print(f"Successfully loadded {len(data)} characters from the file.")

    finally:
        print("File loading operation terminated")

secure_file_loader("missing_dataset.csv")
