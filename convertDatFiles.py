import os
import shutil

def copy_and_rename_dat_to_txt(input_root, output_root):
    for dirpath, _, filenames in os.walk(input_root):
        for filename in filenames:
            if filename.endswith('.dat'):
                # Full path to the original file
                input_path = os.path.join(dirpath, filename)

                # Relative path from the input root
                rel_path = os.path.relpath(input_path, input_root)

                # Change extension to .txt
                rel_path_txt = rel_path[:-4] + '.txt'

                # Full output path
                output_path = os.path.join(output_root, rel_path_txt)

                # Create output directory if needed
                os.makedirs(os.path.dirname(output_path), exist_ok=True)

                # Copy the file
                shutil.copy2(input_path, output_path)
                print(f"Copied: {input_path} → {output_path}")


copy_and_rename_dat_to_txt("Instances", "ConvertedInstances")
