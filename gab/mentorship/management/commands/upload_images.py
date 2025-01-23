import os
from django.core.management.base import BaseCommand
from django.conf import settings
import cloudinary.uploader
from decouple import config

# this file uploads images to cloudinary and prints the urls of those images from cloudinary on terminal
#to make work easier, I have saved the images in WMI-GAB-projects/testimonial_cloudinary_images_urls.txt file
# these urls are then used instead of images since Vercel does not allow storage and there4 rendering of images
# To run this script, go project root dir(gab) then run this command: python manage.py upload_images

# configure cloudinary using Django settings
cloudinary.config(
    cloud_name = config('CLOUDINARY_CLOUD_NAME'),
    api_key = config('CLOUDINARY_API_KEY'),
    api_secret = config('CLOUDINARY_API_SECRET'),
    secure = True
)

class Command(BaseCommand):
    help = 'Upload testimonial images to Cloudinary and output URLs'

    def handle(self, *args, **kwargs):
        # Path to local image folder
        IMAGE_FOLDER = os.path.join(settings.BASE_DIR, 'mentorship', 'static', 'new_images')
        # IMAGE_FOLDER = "gab/mentorship/static/images"  # Replace this with the actual path
        # verify if folder exists
        if not os.path.exists(IMAGE_FOLDER):
            raise FileNotFoundError(f'Directory not found: {IMAGE_FOLDER}')

        # loop through images and upload each one
        for filename in os.listdir(IMAGE_FOLDER):
            if filename.endswith(('.jpg', '.png', '.jpeg')):
                file_path = os.path.join(IMAGE_FOLDER, filename)

                # Upload to Cloudinary
                upload_result = cloudinary.uploader.upload(file_path, public_id=filename)

                # Output the secure URL
                print(f"{filename}: {upload_result['secure_url']}")
