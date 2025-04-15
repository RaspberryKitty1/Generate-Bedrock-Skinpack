# 🧑‍🎨 Skin Pack Creation Guide 🎒

Want to add your own custom skins to Minecraft? This guide will walk you through creating a **custom skin pack** using a handy Python script 🐍. It’ll generate everything you need to make a `.mcpack` file you can import right into the game! 🧱🚀

---

## 🌟 Features

✅ Automatically creates:

- `manifest.json` 📜  
- `skins.json` 👕  
- `en_US.lang` 🌍 (for language support)  

✅ Supports **PNG** files as textures 🖼  
✅ Bundles everything into a neat `.mcpack` 📦  
✅ Cleans up temporary files after packaging 🧹  

---

## 🧰 Requirements

- Python 3.x 🐍  
(That's it! No need for a virtual environment.)

---

## ⚙️ Setup

### ✨ No virtual environment (`venv`) required

1. **Drop your PNG files** into the same folder as the script 🗂  
   - 📝 Make sure each PNG file is named the same as the skin name you want.  
     > *Example:* `Cool_Skin.png` will be named **Cool_Skin** in-game.

2. **Run the script** 💻:

   ```bash
   python Generate-Bedrock-Skinpack.py
   ```

3. **Fill in the prompts** when asked:
   - 🎨 **Skin Pack Name**: What you want your pack to be called
   - 🔢 **Version Number**: Use `x.y.z` format (e.g., `1.0.0`)

4. The script will:
   - 🧾 Generate `manifest.json` with unique UUIDs
   - 👤 Create `skins.json` using your textures
   - 🌐 Add localization entries to `en_US.lang`
   - 📦 Bundle everything into a `.mcpack` file

---

## 🗂 Directory Structure

Here's what gets created behind the scenes:

```plaintext
<skinpack_name>/
├── manifest.json
├── skins.json
├── texts/
│   └── en_US.lang
└── <texture_files> (PNG skins)
```

➡️ After that, your `.mcpack` file is ready to import into Minecraft! 🎮

---

## 📤 Output

The result will be a `.mcpack` file called:

```plaintext
<skinpack_name>.mcpack
```

You can:

- Drag it directly into Minecraft 🖱  
- Or drop it in this folder:  

  ```plaintext
  com.mojang/skin_packs
  ```

---

## 🧽 Cleanup

When it’s all done, the script will clean up all the temporary files it created. Nice and tidy! 🧼✨

---

## 🛠 Troubleshooting

😕 **No PNG files found?**  
Make sure your textures are in the **same folder** as the script.

😕 **Version format error?**  
If you enter something invalid, it’ll just default to `1.0.0`.

---

### ⚠️ Skin Limitations

> [!WARNING]
> 🚧 If you're adding **more than 5 skins**, beware:  
> There’s a **known bug** in Minecraft Bedrock where the skin selector won’t expand properly if there are too many custom skins. Try to stick to 5 or fewer for best results! 🙅‍♂️

---

## 📄 License

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for details.
