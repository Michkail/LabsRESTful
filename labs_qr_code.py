import qrcode
from PIL import Image, ImageDraw

# Your website URL
website_url = "https://pitrlabs.com"

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=8,
    border=4,
)
qr.add_data(website_url)
qr.make(fit=True)

# Create a fully transparent background image with gradient QR code
background = Image.new("RGBA", (qr.modules_count * 10, qr.modules_count * 10), (0, 0, 0, 0))
draw = ImageDraw.Draw(background)

# Create a gradient effect for the QR code color
start_color = (50, 111, 191)
end_color = (0, 246, 255)

for x in range(background.width):
    for y in range(background.height):
        alpha = int((x / background.width) * 255)
        color = (
            int(start_color[0] + (end_color[0] - start_color[0]) * (x / background.width)),
            int(start_color[1] + (end_color[1] - start_color[1]) * (x / background.width)),
            int(start_color[2] + (end_color[2] - start_color[2]) * (x / background.width)),
            alpha,
        )
        draw.point((x, y), fill=color)

# Paste the QR code onto the transparent background
background.paste(qr.make_image(fill_color="black", back_color="black"), (0, 0), qr.make_image())

# Save the final image
background.save("pitrLabs_qrcode_black.png")
