# Skin Pack Creation Guide

This guide explains how to create a custom skin pack for Minecraft using the Python script provided. The script helps in generating the necessary files to package a skin pack into a `.mcpack` file format.

## Features

- Automatically generates the necessary `manifest.json`, `skins.json`, and language files (`en_US.lang`).
- Supports PNG files as texture sources.
- Packages everything into a `.mcpack` file, ready to be imported into Minecraft.
- Cleans up temporary files after creation.

## Requirements

- Python 3.x

---

## Setup

**No virtual environment (`venv`) required!**

1. **Place your PNG files** (textures) in the same directory as the script.
   - **Note**: The PNG files should be named according to the skin names you want in your pack. For example, if you want a skin named `Cool_Skin`, name the texture file `Cool_Skin.png`.

2. **Run the script**:

   ```bash
   python Generate-Bedrock-Skinpack.py
   ```

3. **Enter the required information** when prompted:
   - **Skin Pack Name**: The name of your skin pack.
   - **Version Number**: The version of the skin pack in `x.y.z` format (e.g., `1.0.0`).

4. The script will:
   - Generate `manifest.json` with unique UUIDs.
   - Create `skins.json` based on the textures you provided.
   - Add entries to `en_US.lang` for localization.
   - Package everything into a `.mcpack` file.

---

## Directory Structure

The script will generate the following directory structure:

```plaintext
<skinpack_name>/
├── manifest.json
├── skins.json
├── texts/
│   └── en_US.lang
└── <texture_files> (PNG files)
```

Once the `.mcpack` file is created, you can distribute it or import it into Minecraft.

---

## Output

The script will create a `.mcpack` file named `<skinpack_name>.mcpack` in the current directory. This file can be imported into Minecraft directly by dragging it into the Minecraft interface or placing it in the `com.mojang/skin_packs` folder.

---

## Cleanup

After successfully creating the `.mcpack` file, the script will delete the temporary directories and files used in the creation process.

---

## Troubleshooting

- **No PNG files found**: If the script doesn't find any PNG files in the current directory, it will display an error. Make sure to place your texture files in the same directory as the script.
- **Invalid version format**: If an invalid version is entered, the script defaults to version `1.0.0`.

### Skin Limitations:

- **Be cautious if you add more than 5 skins**: There is a known bug in the Bedrock Edition skin selector that may cause issues when a custom skin pack contains more than **5 skins**. In these cases, the skin selector might not let you expand to view all skins. To avoid this issue, it’s recommended to keep your skin pack to 5 or fewer skins.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
