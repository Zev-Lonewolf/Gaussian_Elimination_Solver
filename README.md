<div align="center">

# 📐 MatrixSolver

![Python](https://img.shields.io/badge/Python-3.13-blue)
![MIT License](https://img.shields.io/badge/license-MIT-green)
![Academic Project](https://img.shields.io/badge/Academic--Project-University-yellow)
![Current State](https://img.shields.io/badge/Current%20State-Finished-brightgreen)

A simple Python project to solve linear systems using  
**Gaussian elimination** and **back-substitution**.

</div>

---

### 📚 About

This project was developed as a complementary study for a graduation assignment in the Linear Algebra course at UFMT.

Its goal is simple and straightforward: **to solve linear systems using matrix scaling (Gaussian elimination) and back-substitution techniques**. It demonstrates key numerical methods used to solve systems of linear equations and encourages hands-on learning through a command-line interface.

The chosen language was **Python**, recommended by the instructor as a great first challenge to combine algebraic reasoning with programming logic.

The project is intended for students, educators, or anyone curious about numerical solutions or just exploring the projects shared on this profile.

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white)
![VS Code](https://img.shields.io/badge/VSCode-Editor-007ACC?logo=visual-studio-code&logoColor=white)

### 🚀 How to Use

To run the program locally via terminal, follow the steps below:

1. **Clone the repository** (if you haven’t already):

    ```bash
    git clone https://github.com/Zev-Lonewolf/Gaussian_Elimination_Solver.git
    cd Gaussian_Elimination_Solver
    ```

2. **Navigate to the source directory and run the script:**

    ```bash
    python src/code.py
    ```

3. **Follow the prompts:**
    - Enter the number of variables in the system
    - Input the augmented matrix, one row at a time

4. **The program will:**
    - Display the original matrix
    - Show the escalated (triangular) form
    - Return the solution for each variable

> ✅ No external dependencies required — everything runs with standard Python.

## 🧪 Example of Use

Let's solve the following system of equations:
```
2x + 3y + z = 1
4x + y + 2z = 2
-2x + 5y + 2z = 3
```

### 💻 Terminal Execution

```bash
$ python src/code.py

🇺🇸 How many variables does the system have? 3
🇧🇷 Quantas variáveis tem o sistema? 3

🇺🇸 Enter the coefficients of the augmented matrix (line by line, including the results):
🇧🇷 Digite os coeficientes da matriz aumentada (linha por linha, incluindo os resultados):
Linha 1: 2 3 1 1
Linha 2: 4 1 2 2
Linha 3: -2 5 2 3

🇺🇸 Original matrix:
🇧🇷 Matriz original:
[2.0, 3.0, 1.0, 1.0]
[4.0, 1.0, 2.0, 2.0]
[-2.0, 5.0, 2.0, 3.0]

🇺🇸 Stepped Matrix:
🇧🇷 Matriz escalonada:
[2.0, 3.0, 1.0, 1.0]
[0.0, -5.0, 0.0, 0.0]
[0.0, 0.0, 1.0, 1.0]

🇺🇸 Solutions found:
🇧🇷 Soluções encontradas:
x1 = 0.00
x2 = 0.00
x3  = 1.00
```

## 🛠️ Technical Details & Techniques Used

This project implements a classical Gaussian elimination method followed by back-substitution to solve systems of linear equations.

Written in pure Python, the program follows a procedural style within a single script (`src/code.py`). It handles user input via the command line, manipulates matrices internally using Python lists, and outputs results directly to the terminal.

No external libraries or frameworks are required, ensuring lightweight execution in any standard Python environment.

Key functions include:  
- `escalonar()` for converting the matrix into upper triangular form,  
- `retro_substituicao()` for solving the system by back-substitution,  
- `print_matriz()` for displaying matrices neatly.

### Techniques Used  
- Gaussian Elimination (matrix scaling)  
- Back-substitution  
- Matrix manipulation with Python lists  
- Command-line interface (CLI) input handling and validation

Future enhancements might cover error handling, support for non-square matrices, and possibly a graphical user interface.

---

### 🙏 Acknowledgments

Thanks to UFMT and its dedicated professors for their hard work in shaping the new generation.

Credit is also due to the creators of the tools and languages that made this project possible — Python, Visual Studio Code, and many others.

Finally, a heartfelt nod to all the inspirations and the mathematicians whose formulas bring this solver to life.

### 🙌 Help the Developer

If you found this project useful or interesting, consider giving it a ⭐ star on GitHub — it really helps!

Feel free to follow me for more projects, updates, and nerdy adventures.

Every star and follower motivates me to keep creating and sharing cool stuff!

---

## 📎 License

This project is licensed under the MIT License.
Feel free to use, modify, and share it.

**MIT License © 2025 Zev Lonewolf**
