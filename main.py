"""
Usage:

$ python main.py html_file_origin pdf_destination
"""

def get_file_contents (file_path):
   f = open (file_path)
   contents = f.read ()
   f.close ()

   return contents

# Returns all the src values in an array.
def get_all_srcs_from_html (html):
   result = re.findall(r'src="([^"]*)"', html)
   return result

def download_images (image_srcs):
	images = []
	for img_src in image_srcs:
		response = requests.get (img_src)
		if (response.status_code == 200):
			print ("{img_src} successfully downloaded.")
			images.append (response.content)
		else:
			print ("Failed downloading file from {img_src}")

	return images

def create_new_pdf_with_images (pdf_filename, imgs):
	with open (pdf_filename, "wb") as f:
		f.write (img2pdf.convert (imgs))

def main (html_file_origin, pdf_destination):
	html_content = get_file_contents (html_file_origin)
	img_links = get_all_srcs_from_html (html_content)
	binary_encoded_images = download_images (img_links)
	create_new_pdf_with_images (pdf_destination, binary_encoded_images)

if __name__ == "__main__":
	import sys
	import re
	import requests
	import img2pdf

	html_file_origin = sys.argv[1]
	pdf_destination = sys.argv[2]

	main (html_file_origin, pdf_destination)
