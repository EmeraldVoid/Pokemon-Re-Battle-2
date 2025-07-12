import os

def convert_jpg_to_png(input_folder, output_folder):
    try:
        from PIL import Image
    except ImportError:
        print("PIL module not found. Please install it using 'pip install pillow'.")
        return

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        if filename.endswith('.jpg'):
            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path)
            png_filename = os.path.splitext(filename)[0] + '.png'
            img.save(os.path.join(output_folder, png_filename))
            print(f'Converted {filename} to {png_filename}')

input_folder = input('Enter the input folder path: ')
output_folder = input('Enter the output folder path: ')
convert_jpg_to_png(input_folder, output_folder)

