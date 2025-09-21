ML Project(ForestFirePrediction)

Algerian Forest Fire Analysis
This project involves data cleaning, visualization, and predictive modeling of the Algerian Forest Fire dataset.
It focuses on building and evaluating multiple regression models to predict fire-related metrics.

Here is my deployment link (hosted on Render):
🔗 https://forestfireprediction-5o4e.onrender.com/

📂 Project Structure
Data Cleaning: Handling missing values, converting data types, and cleaning column names.
Exploratory Data Analysis (EDA): Visualizing data distributions and relationships using matplotlib and seaborn.

Model Training: Building and evaluating multiple regression models:
Linear Regression
Lasso Regression
Ridge Regression
Elastic Net Regression

🛠️ Technologies Used
Python 3
pandas
numpy
matplotlib
seaborn
scikit-learn

🚀 How to Run the Project

Clone this repository:
git clone https://github.com/your-username/your-repo.git
cd your-repo

Install required dependencies:
pip install -r requirements.txt

Open the Jupyter Notebook:
jupyter notebook Cleaning&Visualizing.ipynb

Run all cells to clean the data, visualize, and train models.

📊 Dataset
The project uses the Algerian Forest Fire dataset. It includes various features such as:
Date (day, month, year)
Temperature
Relative Humidity (RH)
Wind Speed (Ws)
FFMC, DMC, DC, ISI indices
Region

🔍 Model Evaluation
Each regression model is evaluated using cross-validation to determine its performance and select the best regularization method.

📜 License
This project is licensed under the MIT License - see the LICENSE file for details.
