import argparse
import os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--jpg_file', required=True, help='Input image file name (JPG/JPEG) from inputs directory')
    args = parser.parse_args()
    
    # Construct full input path
    input_path = os.path.join('inputs', args.jpg_file)
    
    # Check if input file exists
    if not os.path.exists(input_path):
        print(f"Error: Input file '{input_path}' does not exist")
        return

    try:
        from PIL import Image
        # Open the image
        img = Image.open(input_path)
        
        # Create outputs directory if it doesn't exist
        os.makedirs('outputs', exist_ok=True)
        
        # Create output filename in outputs directory
        base_name = os.path.splitext(args.jpg_file)[0]
        output_file = os.path.join('outputs', f"{base_name}.png")
        
        # Check if output file already exists
        if os.path.exists(output_file):
            print(f"Warning: Output file '{output_file}' already exists and will be overwritten")
        
        # Save as PNG
        img.save(output_file, 'PNG')
        print(f"Successfully converted {input_path} to {output_file}")
    except ImportError:
        print("Please install Pillow first: pip install Pillow")
    except Exception as e:
        print(f"Error converting file: {str(e)}")

if __name__ == "__main__":
    main()