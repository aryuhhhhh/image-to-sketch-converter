# 🖼️ Image to Sketch Converter

A simple Python tool that converts any image into a pencil-style sketch using **OpenCV**.  
Supports grayscale and color sketch modes with adjustable intensity.

---

## ✨ Features
- Convert images into **pencil sketches** 🎨
- Choose between **grayscale** or **color** sketch
- **Adjust intensity** for darker/lighter sketches
- **Preview window** before saving
- Saves output automatically in the `output/` folder

---

## 📂 Project Structure
```text
image-to-sketch/
├─ image.jpg             # Example input image
├─ output/               # Stores generated sketches
│   ├─ sketch.png
│   └─ color_sketch.png
├─ sketch.py             # Main script
├─ requirements.txt      # Python dependencies
└─ README.md             # Documentation
```
---

## ⚡ Getting Started

### 1️⃣ Requirements

- Python **3.8+**
- Dependencies listed in `requirements.txt`

Install them with:

```bash
pip install -r requirements.txt
```
## 2️⃣ Run the Script

**Basic grayscale sketch:**
```bash
python sketch.py image.jpg
```
**Custom output filename:**
```bash
python sketch.py image.jpg -o output/mysketch.png
```
**Adjust sketch intensity:**
```bash
python sketch.py image.jpg -i 200
```
**Color sketch mode:**
```bash
python sketch.py image.jpg -c -o output/color_sketch.png
```

## 📊 Outputs

Outputs are stored inside the /output folder:
- sketch.png → Grayscale sketch
- color_sketch.png → Color sketch (if enabled)
  
Preview windows will also open, showing the original image and the sketch.

---
## 📝 Notes

- Works with .jpg and .png images.
- Sketch intensity can be tuned with the -i flag (default: 256).
- The script uses Gaussian Blur and image inversion to generate realistic sketch effects.

---
## 🚀 Future Improvements

- Batch mode: convert all images in a folder at once
- Add edge detection and shading effects
- Build a simple Streamlit GUI for easy uploads
- Option to export directly to PDF for artistic portfolios

---
