# 🐍 Python GUI Projects

A collection of Python GUI applications built to practice programming, automate tasks, and explore different Python libraries and technologies.

## 🚀 Projects

| Project | Description |
|---|---|
| [Watermark Desktop App](./) | A Python project to add a mark water to photos. |

*More projects will be added as the repository grows.*

## 🛠️ Technologies & Requirements

- **Language:** Python 3.8 or higher
- **Dependencies:** Check the `requirements.txt` file inside each project directory.
- **Environment:** A virtual environment is recommended for managing dependencies.

## 📦 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/luisssSoto/Python-Scripting.git
cd Python\ GUI
```

### 2. Create a virtual environment

**Windows (PowerShell):**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

If you encounter activation issues, refer to the `activate env.txt` file in the repository root.

### 3. Install project dependencies

Navigate to the desired project directory and install its requirements, if provided:

```bash
pip install -r requirements.txt
```

> **Note:** Each project may have its own dependencies. Follow the instructions in its directory.

## ⚙️ Configuration

Some projects may require environment variables, API keys, or other configuration settings.

If a project provides a `.env.example` file, copy it to `.env`:

```bash
cp .env.example .env
```

Then update the values in `.env` with your own configuration:

```env
API_KEY=your_actual_api_key_here
```

**Security:** Never commit real API keys, passwords, or other secrets to GitHub. Keep `.env` files out of version control using `.gitignore`.

## ▶️ Usage

Each project may have its own entry point and execution instructions.

1. Navigate to the project directory.
2. Activate the appropriate virtual environment.
3. Install the required dependencies.
4. Run the project's main script.

For example:

```bash
python main.py
```

If a script supports command-line arguments, you can usually view its options with:

```bash
python main.py --help
```

Refer to the individual project's documentation for specific commands, inputs, and examples.

## 📁 Repository Structure

```text
Python-GUI/
├── project1/
│   ├── data/                 # Project data files
│   ├── main.py               # Main script
│   └── requirements.txt      # Project dependencies
│
├── project2/
│   ├── src/                  # Source code
│   └── main.py               # Main script
│
├── .gitignore                # Files excluded from Git
├── README.md                 # Repository documentation
└── activate env.txt           # Virtual environment instructions
```

*The structure above is an example. Actual folders and files may vary between projects.*

## 🤝 Contributing

Suggestions, bug reports, and contributions are welcome!

- Open an issue to report a bug or suggest an improvement.
- Submit a pull request to contribute code or documentation.
- Keep contributions focused, readable, and consistent with Python best practices.

## 📄 License

This repository is available under the [MIT License](./LICENSE), provided that a `LICENSE` file containing the license terms is included.

## 👨‍💻 Author

**Luis Alejandro Soto Serafín**

- GitHub: [@luisssSoto](https://github.com/luisssSoto)

---

⭐ If you find these projects useful, feel free to explore the repository and follow my progress as I continue learning and building with Python.
