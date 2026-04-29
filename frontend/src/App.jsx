import React, { useState } from "react";
import axios from "axios";


const API_URL = "https://Salehmangrio-face-mask-detect.hf.space";

const App = () => {

  const [image, setImage] = useState(null);
  const [preview, setPreview] = useState(null);
  const [resultImage, setResultImage] = useState(null);
  const [prediction, setPrediction] = useState(null);
  const [confidence, setConfidence] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);


  const handleImageUpload = (e) => {
    const file = e.target.files[0];

    if (!file) return;

    setImage(file);
    setPreview(URL.createObjectURL(file));

    // Reset previous results
    setResultImage(null);
    setPrediction(null);
    setConfidence(null);
    setError(null);
  };

  const handlePrediction = async () => {
    if (!image) {
      setError("Please select an image first.");
      return;
    }

    setLoading(true);
    setError(null);

    try {
      const formData = new FormData();
      formData.append("file", image);

      const response = await axios.post(`${API_URL}/predict`, formData, {
        responseType: "blob",
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

      // Result image
      const imgUrl = URL.createObjectURL(response.data);
      setResultImage(imgUrl);

      // Headers data
      setPrediction(response.headers["x-prediction"]);
      setConfidence(response.headers["x-confidence"]);
    } catch (err) {
      setError("Prediction failed. Please try again.");
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-linear-to-br from-blue-900 via-indigo-900 to-purple-900">

      {/* ================= HEADER ================= */}
      <header className="text-center py-12">
        <h1 className="text-5xl font-bold text-white">
          Face Mask Detection
        </h1>
        <p className="text-blue-200 mt-3 text-lg">
          AI-Powered Computer Vision System
        </p>
      </header>

      {/* ================= MAIN ================= */}
      <main className="max-w-6xl mx-auto px-6 grid md:grid-cols-2 gap-10">

        {/* ================= UPLOAD SECTION ================= */}
        <section className="bg-white/10 backdrop-blur-lg p-8 rounded-3xl border border-white/20">

          <h2 className="text-white text-2xl font-semibold mb-6">
            Upload Image
          </h2>

          <label className="block border-2 border-dashed border-white/30 rounded-2xl p-8 text-center cursor-pointer">
            <input
              type="file"
              accept="image/*"
              onChange={handleImageUpload}
              className="hidden"
            />

            {preview ? (
              <img
                src={preview}
                alt="preview"
                className="rounded-xl max-h-80 mx-auto"
              />
            ) : (
              <p className="text-white">Click to upload image</p>
            )}
          </label>

          <button
            onClick={handlePrediction}
            disabled={loading}
            className="w-full mt-6 bg-blue-600 hover:bg-blue-700 text-white py-3 rounded-xl font-semibold"
          >
            {loading ? "Processing..." : "Detect Mask"}
          </button>

          {error && (
            <p className="text-red-400 mt-4 text-center">{error}</p>
          )}
        </section>

        {/* ================= RESULT SECTION ================= */}
        <section className="bg-white/10 backdrop-blur-lg p-8 rounded-3xl border border-white/20">

          <h2 className="text-white text-2xl font-semibold mb-6">
            Result
          </h2>

          {resultImage ? (
            <div>
              <img
                src={resultImage}
                alt="result"
                className="rounded-xl w-full"
              />

              <div className="mt-6 text-white">
                <p className="text-lg">
                  Prediction:{" "}
                  <span className="font-bold">{prediction}</span>
                </p>

                <p className="text-lg">
                  Confidence:{" "}
                  <span className="font-bold">{confidence}%</span>
                </p>
              </div>
            </div>
          ) : (
            <p className="text-white/60 text-center mt-20">
              No result yet
            </p>
          )}
        </section>

      </main>

      {/* ================= FOOTER ================= */}
      <footer className="text-center text-white/60 mt-16 pb-10">
        <p>Face Mask Detection System • AI + Computer Vision</p>
        <p>
          Developed by Saleh Mangrio • Kelash Kumar • Bheesham Kumar
        </p>
      </footer>

    </div>
  );
};

export default App;