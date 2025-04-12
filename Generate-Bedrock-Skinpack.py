import json
import os
import zipfile
import uuid
import logging
import shutil  # Import shutil for directory removal

# Set up logging
log_file = "skinpack_creation.log"
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_and_print(message, level="info"):
    """Logs and prints messages to the console."""
    if level == "info":
        logging.info(message)
    elif level == "warning":
        logging.warning(message)
    elif level == "error":
        logging.error(message)
    print(message)

# Function to generate a new UUID
def generate_uuid():
    uuid_value = str(uuid.uuid4())
    log_and_print(f"🆔 Generated UUID: {uuid_value}")
    return uuid_value

# Get user input for the skin pack name and version
skinpack_name = input("🎨 Enter the skin pack name: ").strip()
log_and_print(f"Skin pack name: {skinpack_name}")

version_input = input("🔢 Enter the version number (format: x.y.z, e.g., 1.0.0): ").strip()
log_and_print(f"Version input: {version_input}")

# Validate version format
try:
    version = list(map(int, version_input.split(".")))
    if len(version) != 3:
        raise ValueError
    log_and_print(f"✅ Validated version: {version}")
except ValueError:
    log_and_print("⚠️ Invalid version format. Using default version [1, 0, 0].", level="warning")
    version = [1, 0, 0]

# Generate UUIDs for manifest
header_uuid = generate_uuid()
module_uuid = generate_uuid()

# Base manifest.json
manifest = {
    "format_version": 1,
    "header": {
        "name": skinpack_name,
        "uuid": header_uuid,
        "version": version
    },
    "modules": [
        {
            "type": "skin_pack",
            "uuid": module_uuid,
            "version": version
        }
    ]
}
log_and_print(f"📄 Created manifest.json structure. \n {manifest}")

# Get all PNG files in the current working directory
cwd = os.getcwd()
textures = [f for f in os.listdir(cwd) if f.endswith(".png")]
log_and_print(f"🖼️ Found textures: {textures}")

if not textures:
    log_and_print("❌ No PNG files found in the current directory. Add some textures and try again!", level="error")
    exit()

# Create skins.json dynamically based on textures
skins = []
lang_entries = [f"skinpack.{skinpack_name}={skinpack_name}\n"]
log_and_print(f"📝 Started generating skins.json and lang entries. \n {lang_entries}")

for texture in textures:
    skin_name = os.path.splitext(texture)[0].replace("_", " ").replace("-", " ").title()
    geometry_name = f"geometry.{skinpack_name}.{skin_name}"
    skins.append({
        "localization_name": skin_name,
        "geometry": geometry_name,
        "texture": texture,
        "type": "free"
    })
    lang_entries.append(f"skin.{skinpack_name}.{skin_name}={skin_name}\n")
    log_and_print(f"✔️ Processed texture: {texture}, Skin name: {skin_name}, Geometry: {geometry_name}")

skins_json = {
    "skins": skins,
    "serialize_name": skinpack_name,
    "localization_name": skinpack_name
}
log_and_print(f"📄 Completed skins.json structure. \n {skins_json}")

# Create output directory
output_dir = skinpack_name
os.makedirs(output_dir, exist_ok=True)
log_and_print(f"📂 Created output directory: {output_dir}")

# Write manifest.json and skins.json
manifest_path = os.path.join(output_dir, "manifest.json")
with open(manifest_path, "w") as manifest_file:
    json.dump(manifest, manifest_file, indent=4)
log_and_print(f"💾 Saved manifest.json to: {manifest_path}")

skins_path = os.path.join(output_dir, "skins.json")
with open(skins_path, "w") as skins_file:
    json.dump(skins_json, skins_file, indent=4)
log_and_print(f"💾 Saved skins.json to: {skins_path}")

# Write the lang file
texts_dir = os.path.join(output_dir, "texts")
os.makedirs(texts_dir, exist_ok=True)
log_and_print(f"📂 Created texts directory: {texts_dir}")

lang_file_path = os.path.join(texts_dir, "en_US.lang")
with open(lang_file_path, "w") as lang_file:
    lang_file.writelines(lang_entries)
log_and_print(f"💾 Saved en_US.lang to: {lang_file_path}")

# Copy texture files into the output directory
log_and_print("🔄 Copying texture files to the output directory.")
for texture in textures:
    dest_path = os.path.join(output_dir, texture)
    with open(dest_path, "wb") as texture_file:
        with open(texture, "rb") as src_file:
            texture_file.write(src_file.read())
    log_and_print(f"✔️ Copied texture: {texture} to {dest_path}")

# Create .mcpack (ZIP archive with .mcpack extension)
mcpack_filename = f"{skinpack_name}.mcpack"
log_and_print(f"🛠️ Creating .mcpack file: {mcpack_filename}")
with zipfile.ZipFile(mcpack_filename, "w", zipfile.ZIP_DEFLATED) as mcpack:
    for root, _, files in os.walk(output_dir):
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, output_dir)
            mcpack.write(file_path, arcname)
            log_and_print(f"✅ Added to .mcpack: {arcname}")

log_and_print(f"🎉 Skin pack '{skinpack_name}' created successfully: {mcpack_filename}")

# Cleanup: Remove the output directory
log_and_print("🧹 Cleaning up temporary files...")
try:
    shutil.rmtree(output_dir)
    log_and_print(f"🗑️ Removed temporary directory: {output_dir}")
except Exception as e:
    log_and_print(f"⚠️ Error during cleanup: {e}", level="error")

