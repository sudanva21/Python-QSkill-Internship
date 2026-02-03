from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

def parse_matrix(matrix_str):
    """
    Parses a string input like "1 2; 3 4" into a NumPy array.
    """
    try:
        if not matrix_str.strip():
            return None
        rows = matrix_str.strip().split(';')
        matrix_data = []
        for row in rows:
            matrix_data.append([float(x) for x in row.strip().split()])
        return np.array(matrix_data)
    except Exception as e:
        raise ValueError(f"Invalid matrix format: {e}")

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None
    matrix_a_str = ""
    matrix_b_str = ""
    operation = "add"

    if request.method == 'POST':
        matrix_a_str = request.form.get('matrix_a', '')
        matrix_b_str = request.form.get('matrix_b', '')
        operation = request.form.get('operation')

        try:
            A = parse_matrix(matrix_a_str)
            # Some operations might not need B, but we'll parse it if provided
            B = parse_matrix(matrix_b_str) if matrix_b_str else None

            if A is None:
                raise ValueError("Matrix A is required.")

            if operation == 'add':
                if B is None: raise ValueError("Matrix B is required for addition.")
                res_mat = np.add(A, B)
                result = f"Result (A + B):\n{res_mat}"
            elif operation == 'sub':
                if B is None: raise ValueError("Matrix B is required for subtraction.")
                res_mat = np.subtract(A, B)
                result = f"Result (A - B):\n{res_mat}"
            elif operation == 'mul':
                if B is None: raise ValueError("Matrix B is required for multiplication.")
                res_mat = np.dot(A, B)
                result = f"Result (A * B):\n{res_mat}"
            elif operation == 'transpose':
                res_mat = np.transpose(A)
                result = f"Result (Transpose A):\n{res_mat}"
            elif operation == 'det':
                if A.shape[0] != A.shape[1]:
                    raise ValueError("Determinant requires a square matrix.")
                det_val = np.linalg.det(A)
                result = f"Determinant of A: {det_val:.4f}"
            else:
                error = "Invalid operation."

        except ValueError as e:
            error = str(e)
        except Exception as e:
            error = f"An error occurred: {e}"

    return render_template('index.html', result=result, error=error, 
                           matrix_a=matrix_a_str, matrix_b=matrix_b_str, operation=operation)

if __name__ == '__main__':
    app.run(debug=True)
