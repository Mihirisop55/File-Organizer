# File organizer
import os
import shutil

file_path = os.getcwd()
files = os.listdir(file_path)


for file in files:
    if os.path.isfile(file):
        # Images
        if os.path.splitext(file)[1] == ".png" or os.path.splitext(file)[1] == ".jpeg" or os.path.splitext(file)[1] == ".jpg" or os.path.splitext(file)[1] == ".gif" or os.path.splitext(file)[1] == ".bmp" or os.path.splitext(file)[1] == ".svg" or os.path.splitext(file)[1] == ".tiff" or os.path.splitext(file)[1] == ".heic" or os.path.splitext(file)[1] == ".webp":
            if not os.path.exists("Images"):
                os.mkdir("Images")
                shutil.move(file, "Images/" + file)
            else:
                shutil.move(file, "Images/" + file)
        # Videos
        if os.path.splitext(file)[1] == ".mp4" or os.path.splitext(file)[1] == ".mkv" or os.path.splitext(file)[1] == ".avi" or os.path.splitext(file)[1] == ".mov" or os.path.splitext(file)[1] == ".wmv" or os.path.splitext(file)[1] == ".flv" or os.path.splitext(file)[1] == ".webm":
            if not os.path.exists("Videos"):
                os.mkdir("Videos")
                shutil.move(file, "Videos/" + file)
            else:
                shutil.move(file, "Videos/" + file)
        # Audio
        if os.path.splitext(file)[1] == ".mp3" or os.path.splitext(file)[1] == ".wav" or os.path.splitext(file)[1] == ".aac" or os.path.splitext(file)[1] == ".flac" or os.path.splitext(file)[1] == ".ogg" or os.path.splitext(file)[1] == ".m4a":
            if not os.path.exists("Audio"):
                os.mkdir("Audio")
                shutil.move(file, "Audio/" + file)
            else:
                shutil.move(file, "Audio/" + file)
        # Documents
        if os.path.splitext(file)[1] == ".pdf" or os.path.splitext(file)[1] == ".doc" or os.path.splitext(file)[1] == ".docx" or os.path.splitext(file)[1] == ".txt" or os.path.splitext(file)[1] == ".rtf" or os.path.splitext(file)[1] == ".odt" or os.path.splitext(file)[1] == ".md":
            if not os.path.exists("Documents"):
                os.mkdir("Documents")
                shutil.move(file, "Documents/" + file)
            else:
                shutil.move(file, "Documents/" + file)
        # Spreadsheets & Presentations
        if os.path.splitext(file)[1] == ".xls" or os.path.splitext(file)[1] == ".xlsx" or os.path.splitext(file)[1] == ".csv" or os.path.splitext(file)[1] == ".ppt" or os.path.splitext(file)[1] == ".pptx" or os.path.splitext(file)[1] == ".key" or os.path.splitext(file)[1] == ".ods":
            if not os.path.exists("Spreadsheets & Presentations"):
                os.mkdir("Spreadsheets & Presentations")
                shutil.move(file, "Spreadsheets & Presentations/" + file)
            else:
                shutil.move(file, "Spreadsheets & Presentations/" + file)
        # Archives & Compressed Files
        if os.path.splitext(file)[1] == ".zip" or os.path.splitext(file)[1] == ".rar" or os.path.splitext(file)[1] == ".7z" or os.path.splitext(file)[1] == ".tar" or os.path.splitext(file)[1] == ".gz":
            if not os.path.exists("Archives & Compressed Files"):
                os.mkdir("Archives & Compressed Files")
                shutil.move(file, "Archives & Compressed Files/" + file)
            else:
                shutil.move(file, "Archives & Compressed Files/" + file)
        # Executables & System Files
        if os.path.splitext(file)[1] == ".exe" or os.path.splitext(file)[1] == ".msi" or os.path.splitext(file)[1] == ".app" or os.path.splitext(file)[1] == ".apk" or os.path.splitext(file)[1] == ".bat" or os.path.splitext(file)[1] == ".sh" or os.path.splitext(file)[1] == ".dll" or os.path.splitext(file)[1] == ".sys":
            if not os.path.exists("Executables & System Files"):
                os.mkdir("Executables & System Files")
                shutil.move(file, "Executables & System Files/" + file)
            else:
                shutil.move(file, "Executables & System Files/" + file)
        # Web & Code
        if os.path.splitext(file)[1] == ".html" or os.path.splitext(file)[1] == ".htm" or os.path.splitext(file)[1] == ".css" or os.path.splitext(file)[1] == ".js" or os.path.splitext(file)[1] == ".php" or os.path.splitext(file)[1] == ".py" or os.path.splitext(file)[1] == ".java" or os.path.splitext(file)[1] == ".xml" or os.path.splitext(file)[1] == ".json":
            if not os.path.exists("Web & Code"):
                os.mkdir("Web & Code")
                shutil.move(file, "Web & Code/" + file)
            else:
                shutil.move(file, "Web & Code/" + file)
