import base64

with open("../static/images/services/404-page-not-found-monochromatic.png", "rb") as image_file:
    base64_string = base64.b64encode(image_file.read()).decode('utf-8')

with open("./404-base64.txt", "w") as res_save:
    res_save.write(base64_string)