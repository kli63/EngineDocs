from PIL import Image

def resize_gif(input_path, output_path):
    # Open the image file
    img = Image.open(input_path)

    # Check if either dimension is greater than 128 pixels
    if img.width > 128 or img.height > 128:
        # Calculate the new height maintaining the aspect ratio
        aspect_ratio = img.height / img.width
        new_height = int(64 * aspect_ratio)

        # List to hold each frame
        frames = []

        # Loop through each frame in the animated GIF
        while True:
            # Resize the current frame
            new_frame = img.resize((64, new_height), Image.LANCZOS)

            # Append the resized frame to the list
            frames.append(new_frame)

            # Try to move to the next frame
            try:
                img.seek(img.tell() + 1)
            except EOFError:
                break

        # Save all frames as a new GIF
        frames[0].save(output_path, save_all=True, append_images=frames[1:], loop=0, format='GIF', optimize=True)
    else:
        # Save the image as is if no resizing is needed
        img.save(output_path, format='GIF', save_all=True)

# Specify the path to your GIF file and the output path
input_path = 'tablegif.gif'
output_path = 'resized_tablegif.gif'

# Call the function to resize the GIF
resize_gif(input_path, output_path)
