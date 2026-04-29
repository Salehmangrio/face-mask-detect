# 😷 Face Mask Detection System (Frontend)

## 🚀 AI-Powered Image Classification Web App

A modern React-based frontend that connects with a deep learning backend API to detect whether a person is wearing a face mask or not.

The system allows users to upload images, sends them to an AI model, and displays predictions with confidence scores and processed results.

---

## 📌 Demo

👉 Upload Image → AI Prediction → Result Display

---

## 🧠 Project Overview

This project is part of a **Computer Vision + Deep Learning system** using a trained CNN (MobileNetV2-based model).

The frontend handles:

* Image upload
* API communication
* Result visualization
* User-friendly UI rendering

---

## 🎯 Features

* 📤 Image upload support
* 🤖 AI-based mask detection
* 📊 Confidence score display
* 🖼️ Processed image output
* ⚡ Fast API integration
* 🎨 Modern responsive UI (TailwindCSS)
* 🌐 Production-ready frontend

---

## 🛠️ Tech Stack

### Frontend

* React.js ⚛️
* Axios 🌐
* Tailwind CSS 🎨

### Backend (API)

* FastAPI 
* TensorFlow / Keras

---

## 📁 Project Structure

```
frontend/
│
├── src/
│   ├── App.jsx
│   ├── index.css
│   ├──main.jsx
│
├── public/
├── package.json
├── vite.config.js
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/salehmangrio/face-mask-detect.git
cd face-mask-detect/frontend
```

### 2️⃣ Install Dependencies

```bash
npm install
```

### 3️⃣ Run Project

```bash
npm start
```

👉 Open in browser:

```
http://localhost:5173
```

---

## 🔗 Backend API Setup

Update API URL inside `App.js`:

```js
const API_URL = "https://salehmangrio-face-mask-detect.hf.space";
```

---

## 📡 API Endpoint

### POST `/predict`

### Request:

* Form Data:

  * `file`: image file

### Response:

* Processed image (blob)
* Headers:

```json
x-prediction: "With Mask"
x-confidence: "95.21"
```

---

## 🧠 How It Works

1. User uploads image
2. Image is sent to backend API
3. AI model processes image:

   * Face detection
   * Mask classification
4. Backend returns:

   * Prediction label
   * Confidence score
   * Processed image
5. Frontend displays results

---

## 📊 Model Information

* Model: MobileNetV2 (Transfer Learning)
* Dataset: Kaggle Face Mask Detection
* Classes:

  * with_mask
  * without_mask
  * mask_weared_incorrect
* Accuracy: ~93–95%

---

## 🎨 UI Highlights

* Gradient background design
* Glassmorphism cards
* Responsive layout
* Smooth loading states
* Error handling UI

---

## 🚀 Deployment

### Build Project

```bash
npm run build
```


## 🔥 Future Improvements

* 🎥 Real-time webcam detection
* 👤 Face detection before classification
* 📊 Prediction history
* 🔐 Authentication system
* 📱 Mobile version (React Native)
* 🌍 Multi-language support

---

## 👨‍💻 Developers

* Saleh Mangrio
* Kelash Kumar
* Bheesham Kumar

---

## 📜 License

This project is created for **educational / semester project purposes**.

---

## ⭐ Acknowledgements

* Kaggle Dataset
* TensorFlow / Keras
* OpenCV
* React.js Community
