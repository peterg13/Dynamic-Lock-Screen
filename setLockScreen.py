import requests

img_data = requests.get("https://external-preview.redd.it/EPwbE8mHsMJdvdqB2hKgVlYqOdlv8x2UD6mu29rcIU0.jpg?auto=webp&s=aad1b651244505c85889bed8d74f2b51e296cf4d").content
with open('image_name.jpg', 'wb') as handler:
    handler.write(img_data)