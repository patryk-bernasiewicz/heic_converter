# HEIC to PNG/JPG converter

I was tired of using online converters all the time to convert my iPhone photos to usable formats, so I decided to write this simple Python script and use it as a CLI tool. Enjoy.

## Usage

### 1. Use via Python

```
python heic_converter.py <path_to_heic_files> <output_path> --format JPG
# or
python heic_converter.py <path_to_heic_files> <output_path> --format PNG
```

### 2. Use with PATH

You can throw the .exe file into a folder that is reachable by your PATH environment variable and just use it directly from your command line

```
heic_converter <path_to_heic_files> <output_path> --format JPG
# or
heic_converter <path_to_heic_files> <output_path> --format PNG
```

### Arguments

`<path_to_heic_files>` and `<output_path>` are optional and default to the current working directory. The script will scan for any .heic files in your current directory and output the JPG or PNG files in the same directory if you decide to omit them.

```
heic_converter --format JPG
```

## Features

- Batch converts all `.heic` files in a single directory
- Preserves EXIF data during conversion
- Saves to either JPG or PNG
- Can be ran as a python script or as a compiled .exe app
- Works offline

## License

Do whatever you want with it.
