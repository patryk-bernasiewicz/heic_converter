import argparse
import os

from pathlib import Path
from PIL import Image
from pillow_heif import register_heif_opener

register_heif_opener()

def convert_heic_images(input_dir = '.', output_dir = '.', output_format = 'jpg'):
  """
  Convert HEIC images to specified format (JPG or PNG)
  
  Args:
    input_dir (str): The path to the directory contianing HEIC images (default = .)
    output_dir (str): The path to the directory to save the converted images (default = .)
    format (str): The format to convert the images to (enum: jpg, png) (default = jpg)
  """

  Path(output_dir).mkdir(parents = True, exist_ok = True)

  print(f"Scanning for HEIC files in: {input_dir}")
  print(f"Saving converted {output_format.upper()} files to: {output_dir}")

  format_map = {
    'JPG': { 'ext': '.jpg', 'format': 'JPEG' },
    'PNG': { 'ext': '.png', 'format': 'PNG' },
  }

  if output_format.upper() not in format_map:
    raise ValueError(f"Invalid output format: {output_format}. Must be one of: {', '.join(format_map.keys())}")

  target_format = format_map[output_format.upper()]

  for filepath in Path(input_dir).rglob('*.heic'):
    try:
      print(f"Converting {filepath.name}")

      image = Image.open(filepath)
      exif_data = image.info.get('exif')

      output_filename = filepath.stem + target_format['ext']
      output_path = Path(output_dir) / output_filename

      if exif_data:
        image.save(output_path, format=target_format['format'], exif=exif_data)
      else:
        image.save(output_path, format=target_format['format'])

      print(f"   -> Saved: {output_path}")
    
    except Exception as e:
      print(f"   -> Error converting {filepath.name}: {e}")

  print(f"\nConversion complete!")



if __name__ == "__main__":
  parser = argparse.ArgumentParser(
    description = "Convert HEIC images to JPG or PNG",
    formatter_class = argparse.ArgumentDefaultsHelpFormatter
  )

  parser.add_argument("input_dir", help="Path to the directory with HEIC images. Default = . (current directory)")
  parser.add_argument("output_dir", help="Path to the directory to save the converted images. Default = . (current directory)")
  parser.add_argument("-f", "--format", choices=["JPG", "PNG"], default="JPG", help="Output format (JPG or PNG, default = JPG)")

  args = parser.parse_args()

  convert_heic_images(args.input_dir, args.output_dir, args.format)