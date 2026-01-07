# Blood Type Calculator (Flask Web App)
A web-based application built with Python Flask. Features include child blood type prediction based on parental genetics and donor/recipient compatibility checks.

Key Features
  - **Child Blood Type Prediction:**
    - Calculates possible child blood types based on parents' phenotypes.
    - Implements **Genotype Mapping** (e.g., Type A = AA or AO) to simulate Punnett Square logic.
    
  - **Transfusion Compatibility:**
    - **Donor Check:** Finds who can donate blood to a specific recipient.
    - **Recipient Check:** Finds who can receive blood from a specific donor.
    - Based on the standard ABO blood group system.

Tech Stack 
  - Python (Flask), HTML, CSS

How to Run
1.  **Clone the repository**
    ```bash
    git clone [https://github.com/LittleCat1041/blood-type-calculator.git](https://github.com/LittleCat1041/blood-type-calculator.git)
    cd blood-type-calculator
    ```

2.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Start the application**
    ```bash
    python app.py
    ```

4.  **Open in browser**
    * Go to: `http://localhost:5000`

Screenshot

<img width="830" height="582" alt="image" src="https://github.com/user-attachments/assets/fe5c200e-9cbf-4a13-be56-be8a0530e78e" />

**Disclaimer:** This tool is for educational purposes only. For medical advice, please consult a professional.
