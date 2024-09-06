prompt = input("File name: ")

new_prompt = prompt.split(".")
extension = new_prompt[-1].lower().strip()

if extension in ["gif", "jpeg", "png"]:
    print(f"image/{extension}")
elif extension == "txt":
    print("text/plain")
elif extension == "pdf" or extension == "zip":
    print(f"application/{extension}")
elif extension == "jpg":
    print("image/jpeg")
else:
    print("application/octet-stream")
