# Book Recommendation System

A machine learning project that provides book recommendations using a content-based approach. It includes a web interface for user interaction.

## Features

- Content-Based Recommendations
- Interactive Web Interface

## Technologies Used

- Python (Pandas, NumPy, Scikit-learn, Flask)
- Jupyter Notebook

## Dataset

This project uses `Books.csv`, `Users.csv`, and `Ratings.csv` datasets, located in the `Data/` directory.

## Model Generation

Model files (`.pkl`) are not included in this repository. To generate them:

1.  **Navigate to the `notebook/` directory:**
    ```bash
    cd notebook/
    ```
2.  **Run Jupyter Notebook:**
    Launch Jupyter Notebook:
    ```bash
    jupyter notebook
    ```
    Open `bookrecommendation.ipynb`. Run all cells in the notebook. This will generate `popular_books.pkl` in the `notebook/` directory, which `app.py` expects to find there.

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/Book-Recommendation-System.git
    cd Book-Recommendation-System
    ```

    (Replace with your repository URL.)

2.  **Create and activate a virtual environment (optional but recommended):**

    ```bash
    python -m venv venv
    # Windows
    .\venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    (A `requirements.txt` file has been created for easier installation.)

## Running the Application

### Locally

1.  **Generate models:** Follow the "Model Generation" steps.
2.  **Run Flask app:**
    ```bash
    python app.py
    ```
3.  **Access:** Open `http://127.0.0.1:5000/` in your browser.

### Using Docker

1.  **Build the Docker image:**

    ```bash
    docker build -t book-recommendation-system .
    ```

2.  **Run the Docker container:**

    ```bash
    docker run -p 5000:5000 book-recommendation-system
    ```

3.  **Access:** Open `http://127.0.0.1:5000/` in your browser.

## Project Structure

```
.
├── app.py
├── Data/
│   ├── Books.csv
│   ├── Ratings.csv
│   └── Users.csv
├── notebook/
│   ├── bookrecommendation.ipynb
│   └── popular_books.pkl (generated)
├── requirements.txt
├── Dockerfile
├── README.md
├── static/
│   └── images/
│       └── systemUI.png
└── templates/
    ├── index.html
    └── recommend.html
```
