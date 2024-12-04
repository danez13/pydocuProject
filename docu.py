import os
import subprocess

def generate_pydoc_recursive(root_dir, output_dir):
    """
    Recursively generates HTML documentation for all Python modules in a directory.

    Args:
        root_dir (str): Path to the root directory containing Python modules.
        output_dir (str): Path to save the generated HTML documentation.
    """
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.py'):
                # Remove the .py extension to pass the module name to pydoc
                module_path = os.path.join(root, file)
                module_name = module_path[:-3].replace(os.sep, ".")
                
                # Change the output directory for pydoc
                original_cwd = os.getcwd()
                os.chdir(output_dir)
                
                try:
                    print(f"Generating documentation for module: {module_name}")
                    subprocess.run(['pydoc', '-w', module_name], check=True)
                except subprocess.CalledProcessError as e:
                    print(f"Failed to generate documentation for {module_name}: {e}")
                finally:
                    os.chdir(original_cwd)

# Usage
if __name__ == "__main__":
    source_directory = "C:/Users/Daniel Hernandez/Desktop/GITHUB/CAP-XAI"
    docs_output_directory = "docs/"
    generate_pydoc_recursive(source_directory, docs_output_directory)
