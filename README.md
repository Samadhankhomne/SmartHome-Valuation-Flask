# SmartHome-Valuation-Flask

# House Price Prediction

This project is a machine learning application that predicts house prices based on square footage. It uses a Linear Regression model for prediction and provides a Flask-based web interface to allow users to input square footage and receive predicted house prices.

## Features

1. **Machine Learning Model**:
   - Trained using a Linear Regression algorithm.
   - Provides accurate predictions for house prices based on input square footage.
   - Evaluation metrics:
     - Training Score (R²)
     - Testing Score (R²)
     - Mean Squared Error (MSE)

2. **Data Visualization**:
   - Visualizes training and testing datasets with scatter plots.
   - Plots include:
     - Training Dataset Visualization
     - Testing Dataset Visualization

3. **Web Interface**:
   - Built using Flask.
   - Allows users to input square footage and view the predicted house price.

4. **Model Persistence**:
   - Saves the trained model as a `.pkl` file for future use.

## Dataset

- **Source**: `House_data.csv`
- **Features**:
  - `sqft_living`: Square footage of the house.
  - `price`: Price of the house.

## Steps

### 1. Data Preprocessing
- Load the dataset and extract features (`sqft_living`) and target (`price`).
- Split the data into training and testing sets using `train_test_split`.

### 2. Model Training
- Train a Linear Regression model on the training dataset.
- Save the trained model using `pickle` for reuse.

### 3. Model Evaluation
- Calculate the following metrics:
  - Training Score (R²)
  - Testing Score (R²)
  - Training and Testing MSE

### 4. Visualization
- Generate scatter plots for training and testing datasets with regression lines.

### 5. Web Application
- Develop a Flask application with the following routes:
  - `/`: Displays the home page with a form to input square footage.
  - `/predict`: Predicts house price based on user input and displays the result.

## Installation and Usage

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. **Install Dependencies**:
   Ensure you have Python installed and run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   ```bash
   python app.py
   ```

4. **Access the Web Application**:
   Open your browser and navigate to `http://127.0.0.1:5000`.

## Example Usage

- Input square footage: `600`
- Predicted price: `$123,456.78`

## Directory Structure

```
House-Price-Prediction/
|
├── app.py                 # Flask application
├── House_price.pkl        # Saved Linear Regression model
├── House_data.csv         # Dataset
├── templates/
│   └── index.html         # HTML template for the web interface
├── static/
│   └── background.jpg     # Background image for the web app
├── requirements.txt       # Required Python libraries
├── README.md              # Project description
```

## Technologies Used

- **Programming Language**: Python
- **Libraries**:
  - `numpy`
  - `pandas`
  - `matplotlib`
  - `scikit-learn`
  - `Flask`
- **Visualization Tools**: Matplotlib
- **Web Framework**: Flask

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
