import os


def list_files(directory):
    try:
        # List all files in the given directory
        files = os.listdir(directory)

        # Filter out only files (not directories)
        files = [f for f in files if os.path.isfile(os.path.join(directory, f))]

        return files
    except Exception as e:
        print(f"Error: {e}")
        return []