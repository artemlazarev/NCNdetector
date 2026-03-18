import sys
import os
import json
import argparse
from PIL import Image
import moondream as md


def main():
    parser = argparse.ArgumentParser(description="Moondream inference service")
    parser.add_argument("--image", required=True, help="Path to an image file")
    parser.add_argument("--question", required=True, help="Question to ask the model")
    parser.add_argument("--debug", action="store_true", help="Enable debug output")
    args = parser.parse_args()

    api_key = os.getenv("MOONDREAM_API_KEY", "YOUR_API_KEY")
    if args.debug:
        print(f"[DEBUG] Using API key: {api_key}")
    model = md.vl(api_key=api_key)

    try:
        image = Image.open(args.image)
    except Exception as e:
        print(f"Failed to open image {args.image}: {e}", file=sys.stderr)
        sys.exit(1)

    result = model.query(image, args.question)
    if args.debug:
        print(f"[DEBUG] Query result: {result}")
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
