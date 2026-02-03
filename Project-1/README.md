# Matrix Operations Tool

A powerful, interactive, and visually stunning web-based tool for performing matrix operations. Built with **Python (Flask)** and **NumPy**.

## Features
- **Operations**: Addition, Subtraction, Multiplication, Transpose, Determinant.
- **Neo Mode UI**: A "Matrix" themed interface with falling digital rain and glowing green aesthetics.
- **Dynamic Inputs**: JavaScript-powered grid inputs that adjust rows/cols dynamically.
- **Mobile Responsive**: Fully usable on mobile devices with stacked layouts.
- **CLI Support**: Includes a terminal-based script (`matrix_ops.py`) for command-line usage.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sudanva21/Matrix-Operations-Tool.git
   cd Matrix-Operations-Tool
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Web Interface
1. Run the application:
   ```bash
   python app.py
   ```
2. Open `http://127.0.0.1:5000` in your browser.
3. Enter matrix dimensions and values, then select an operation to calculate.

### Command Line Interface
1. Run the script:
   ```bash
   python matrix_ops.py
   ```
2. Follow the interactive prompts.

## Deployment (Vercel)
This project is configured for easy deployment on **Vercel**.

1. **Push to GitHub**: Ensure your code is pushed to your GitHub repository.
2. **Login to Vercel**: Go to [vercel.com](https://vercel.com) and log in with GitHub.
3. **Import Project**: Click "Add New..." -> "Project" and select `Matrix-Operations-Tool`.
4. **Deploy**: Vercel will detect `vercel.json` and deploy automatically.
   - *Note*: Ensure "Framework Preset" is set to **Other** (or defaults to Python handles it).
