# File Extensions — Identifies the media (MIME) type of a file based on its extension.

fileName = input("File name: ").strip().lower()
prefix, suffix = fileName.split(".")

match suffix:
    case "jpg" | "gif" | "jpeg" | "png":
        print("img/" + suffix)
    case "txt" | "pdf":
        print("text/" + suffix)
    case "zip":
        print("compressed file/" + suffix)
    case _:
        print("application/octet-stream")