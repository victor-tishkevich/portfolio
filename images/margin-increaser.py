import cv2
import argparse
import os

def add_margins(
    input_path,
    output_path,
    top,
    bottom,
    left,
    right,
    color=(255, 255, 255)
):
    # Read image
    img = cv2.imread(input_path)
    if img is None:
        raise ValueError(f"Could not read image: {input_path}")

    # Add border
    bordered = cv2.copyMakeBorder(
        img,
        top,
        bottom,
        left,
        right,
        borderType=cv2.BORDER_CONSTANT,
        value=color
    )

    # Save output
    cv2.imwrite(output_path, bordered)
    print(f"Saved image with margins to: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add white margins to an image (OpenCV)")
    parser.add_argument("input", help="Path to input image")
    parser.add_argument(
        "-m", "--margin",
        type=int,
        default=50,
        help="Margin size in pixels for all sides"
    )
    parser.add_argument(
        "-o", "--output",
        default=None,
        help="Output image path"
    )

    args = parser.parse_args()

    if args.output is None:
        name, ext = os.path.splitext(args.input)
        args.output = f"{name}_with_margin{ext}"

    add_margins(
        input_path=args.input,
        output_path=args.output,
        top=args.margin,
        bottom=args.margin,
        left=args.margin,
        right=args.margin
    )
