import numpy as np
import sys

def get_matrix_input(prompt_text="Enter matrix elements"):
    """
    Parses user input into a NumPy array.
    Supports MATLAB-style input: "1 2; 3 4" means row 1 is [1, 2], row 2 is [3, 4].
    """
    print(f"\n{prompt_text}")
    print("Format: space-separated values for columns, semicolon ';' for rows.")
    print("Example: '1 2; 3 4' creates a 2x2 matrix.")
    
    while True:
        try:
            user_input = input(">> ").strip()
            if not user_input:
                return None
            
            # Replace format to match numpy compatible string or parse manually
            # method: split by ';', then split by space
            rows = user_input.split(';')
            matrix_data = []
            for row in rows:
                matrix_data.append([float(x) for x in row.strip().split()])
            
            return np.array(matrix_data)
        except ValueError:
            print("Invalid input. Please ensure you enter numbers separated by spaces.")
        except Exception as e:
            print(f"Error parsing matrix: {e}")

def print_matrix(name, matrix):
    print(f"\n--- {name} ---")
    print(matrix)
    print(f"Shape: {matrix.shape}")

def main():
    print("=== Matrix Operations Tool ===")
    
    while True:
        print("\nSelect Operation:")
        print("1. Add Matrices (A + B)")
        print("2. Subtract Matrices (A - B)")
        print("3. Multiply Matrices (A * B)")
        print("4. Transpose Matrix (A^T)")
        print("5. Determinant (det(A))")
        print("6. Exit")
        
        choice = input("Enter choice (1-6): ").strip()
        
        if choice == '6':
            print("Exiting...")
            break
            
        try:
            if choice in ['1', '2', '3']:
                # Binary operations
                print("\n--- Input Matrix A ---")
                A = get_matrix_input("Enter Matrix A:")
                if A is None: continue
                
                print("\n--- Input Matrix B ---")
                B = get_matrix_input("Enter Matrix B:")
                if B is None: continue

                if choice == '1':
                    result = np.add(A, B)
                    print_matrix("Result (A + B)", result)
                elif choice == '2':
                    result = np.subtract(A, B)
                    print_matrix("Result (A - B)", result)
                elif choice == '3':
                    result = np.dot(A, B) # Matrix multiplication
                    print_matrix("Result (A * B)", result)

            elif choice in ['4', '5']:
                # Unary operations
                print("\n--- Input Matrix A ---")
                A = get_matrix_input("Enter Matrix A:")
                if A is None: continue

                if choice == '4':
                    result = np.transpose(A)
                    print_matrix("Transposed Matrix", result)
                elif choice == '5':
                    if A.shape[0] != A.shape[1]:
                        print("\nError: Determinant requires a square matrix.")
                    else:
                        det = np.linalg.det(A)
                        print(f"\nDeterminant: {det:.4f}")
            else:
                print("Invalid choice. Please try again.")

        except ValueError as e:
            print(f"\nOperation Error: {e}")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
