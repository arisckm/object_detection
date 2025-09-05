# 🚀 Object Detection with YOLOv5  

An end-to-end **Object Detection System** built using **YOLOv5**.  
The project covers the full lifecycle: dataset preparation, training, validation, and deployment as an interactive **Streamlit web app**.  

---

## 📌 Features  
- Custom dataset preprocessing & visualization  
- Model training and validation using **YOLOv5**  
- Performance metrics (Precision, Recall, mAP)  
- Exported best model weights (`best.pt`)  
- Live deployment with **Streamlit** for real-time detection  

---

## 🗂️ Dataset  
- Dataset contains **6 classes**: `car`, `dog`, `face`, `motorcycle`, `person`, `plate`.  
- Labeled with **YOLO format** (TXT files).  
- Split into **train/valid/test**.  

> Dataset link: [Roboflow Dataset](https://universe.roboflow.com/arisckm/object-detection-computer-vision-kkdzh/dataset/1)  

---

## ⚙️ Model Training  
- Base model: **YOLOv5s** (pre-trained on COCO)  
- Transferred learning with frozen layers for faster convergence  
- Training run for **30 epochs** on custom dataset  

**Results (Validation):**  
- Precision: `0.859`  
- Recall: `0.807`  
- mAP@0.5: `0.851`  
- mAP@0.5:0.95: `0.511`  

---

## 📊 Sample Results  

| Class        | Precision | Recall | mAP@0.5 | mAP@0.5:0.95 |
|--------------|-----------|--------|---------|--------------|
| Car          | 0.95      | 0.77   | 0.86    | 0.64         |
| Dog          | 0.87      | 0.94   | 0.92    | 0.53         |
| Face         | 0.94      | 0.93   | 0.95    | 0.49         |
| Motorcycle   | 0.97      | 1.00   | 1.00    | 0.65         |
| Person       | 0.88      | 0.83   | 0.90    | 0.53         |
| Plate        | 0.55      | 0.38   | 0.49    | 0.22         |

---

## 🚀 Deployment  

Deployed with **Streamlit** for interactive testing:  
- Upload an image  
- Run YOLOv5 inference  
- View detected objects with bounding boxes  

