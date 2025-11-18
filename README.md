# 🚀 SpaceX Falcon 9 First Stage Landing Prediction

This project uses machine learning techniques to **predict whether the first stage of the SpaceX Falcon 9 rocket will successfully land**.  
Accurate landing predictions are important because SpaceX can reuse boosters, significantly reducing launch costs.

This project was developed as part of a Data Science & Machine Learning capstone.

---

## 📁 Project Structure

SpaceX-Falcon9-Landing-Prediction/
│
├── SpaceX Falcon 9 first stage Landing Prediction.ipynb # Main notebook (EDA, ML modeling, visualization)
├── app.py # Flask/Streamlit app (prediction interface)
├── Capstone_Presentation.pptx # Summary presentation of the project
└── README.md # Project documentation


---

## 🧠 Project Overview

The goal is to:

1. **Analyze Falcon 9 launch data**  
2. **Engineer features relevant to landing success**  
3. **Build machine learning models to predict landing outcome**  
4. **Deploy or prepare a prediction application (app.py)**  
5. **Present findings and model performance**

The notebook includes:

- Exploratory Data Analysis (EDA)
- Data Preprocessing
- Feature Engineering
- Model Training (Logistic Regression, Decision Trees, SVM, KNN, etc.)
- Hyperparameter Tuning
- Model Evaluation
- Visualizations (Heatmaps, Scatter plots, Landing success analysis)

---

## 🛰 Dataset

The dataset is based on **SpaceX Falcon 9 launches**, including:

- Launch site  
- Booster version  
- Payload mass  
- Orbit type  
- Flight number  
- Landing platform  
- Landing success/failure  

These were obtained from public SpaceX API sources and/or datasets provided as part of the learning project.

---

## 🔧 Machine Learning Models Used

Several machine learning models were trained and compared:

- Logistic Regression  
- Decision Tree Classifier  
- Support Vector Machine (SVM)  
- K-Nearest Neighbors (KNN)  
- Random Forest  

Performance was evaluated using:

- Accuracy  
- Confusion Matrix  
- Cross-Validation  
- Grid Search (Hyperparameter tuning)

---

## 📊 Key Findings (as summarized in the presentation)

- Payload mass and booster version category significantly influence landing success.  
- Some launch sites have a higher probability of successful booster recovery.  
- With hyperparameter tuning, ensemble models generally performed strongest.  

(For more details, see the PowerPoint: `Capstone_Presentation.pptx`)

---

## 🖥 Running the Prediction App

If `app.py` is a **Flask** or **Streamlit** app, you can run it locally.

### ▶️ **For Flask**
```bash
python app.py


▶️ For Streamlit
streamlit run app.py


Then open the provided URL in your browser.

⚙️ Installation & Requirements

Install dependencies with:

pip install -r requirements.txt


If no requirements file exists, typical packages include:

pandas

numpy

scikit-learn

matplotlib

seaborn

flask or streamlit

🧑‍💻 Author

Abdullahi Ahmed
Data Science & Machine Learning Enthusiast
GitHub: https://github.com/AbdullahiAhm

⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

📜 License

This project is open-source and available under the MIT License
