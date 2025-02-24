# 📖 Automated Novel Generation Tool
<div align="center">
✨ **Core Features** ✨
| Function Module          | Key Capabilities                          |
|--------------------------|-------------------------------------------|
| 🎨 Novel Setting Workshop | Worldview Architecture / Character Setting / Plot Blueprint |
| 📖 Intelligent Chapter Generation | Multi-stage Generation Ensures Plot Coherence |
| 🧠 State Tracking System | Character Development Trajectory / Foreshadowing Management System |
| 🔍 Semantic Retrieval Engine | Vector-based Long-term Context Consistency Maintenance |
| 📚 Knowledge Base Integration | Support for Local Document References |
| ✅ Automatic Review Mechanism | Detects Plot Contradictions and Logical Conflicts |
| 🖥 Visual Workbench | Full-process GUI Operation, Integrated Configuration/Generation/Review |
</div>
> A multi-functional novel generator based on large language models, helping you efficiently create long stories with rigorous logic and consistent settings
---

## 📑 Table of Contents
1. [Environment Preparation](#🛠-Environment-Preparation)
2. [Project Structure](#erdei-Project-Structure)
3. [Configuration Guide](#⚙️-Configuration-Guide)
4. [Running Instructions](#🚀-Running-Instructions)
5. [Usage Tutorial](#📘-Usage-Tutorial)
6. [Troubleshooting](#❓-Troubleshooting)

---

## 🛠 Environment Preparation
Ensure the following running conditions are met:
- **Python 3.9+** runtime environment (recommended 3.10-3.12)
- **pip** package management tool
- Valid API keys:
  - Cloud Services: OpenAI / DeepSeek, etc.
  - Local Services: Ollama, etc. (compatible with OpenAI interfaces)
---
## 📥 Installation Instructions
1. **Download the Project**
   - Download the project ZIP file from [GitHub](https://github.com), or clone this project using the following command:
     ```bash
     git clone https://github.com/YILING0013/AI_NovelGenerator
     ```
2. **Install Build Tools (Optional)**
   - If some packages fail to install, visit [Visual Studio Build Tools](https://visualstudio.microsoft.com/zh-hans/visual-cpp-build-tools/) to download and install the C++ build tools for building certain module packages;
   - During installation, by default, only MSBuild tools are included. Manually select the **C++ Desktop Development** option from the top-left list.
3. **Install Dependencies and Run**
   - Open a terminal and navigate to the project source directory:
     ```bash
     cd AI_NovelGenerator
     ```
   - Install project dependencies:
     ```bash
     pip install -r requirements.txt
     ```
   - After installation, run the main program:
     ```bash
     python main.py
     ```
> If some dependencies are missing, manually execute the following command to install them:
> ```bash
> pip install XXX
> ```

```markdown
## 🗂 Project Structure
```
novel-generator/
├── main.py                      # Entry file, runs the GUI
├── ui.py                        # User interface
├── novel_generator.py           # Core logic for chapter generation
├── consistency_checker.py       # Consistency checker to prevent plot conflicts
├── chapter_directory_parser.py   # Directory parser
├── embedding_adapters.py        # Embedding interface wrapper
├── llm_adapters.py              # LLM interface wrapper
├── prompt_definitions.py        # Define AI prompts
├── utils.py                     # Common utility functions, file operations
├── config_manager.py            # Configuration management (API Key, Base URL)
├── config.json                  # User configuration file (optional)
└── vectorstore/                 # (optional) Local vector database storage
```
---
## ⚙️ Configuration Guide
### 📌 Basic Configuration (config.json)
```json
{
    "api_key": "sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "base_url": "https://api.openai.com/v1",
    "interface_format": "OpenAI",
    "model_name": "gpt-4o-mini",
    "temperature": 0.7,
    "max_tokens": 4096,
    "embedding_api_key": "sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "embedding_interface_format": "OpenAI",
    "embedding_url": "https://api.openai.com/v1",
    "embedding_retrieval_k": 4,
    "topic": "The protagonist of Star Rail travels to the world of Teyvat in Genshin Impact, saves Teyvat, and engages in complex relationships with the characters there",
    "genre": "Fantasy",
    "num_chapters": 120,
    "word_number": 4000,
    "filepath": "D:/AI_NovelGenerator/filepath"
}
```
### 🔧 Configuration Explanation
1. **Generation Model Configuration**
   - `api_key`: API key for the large model service
   - `base_url`: API endpoint URL (for local services, use addresses like Ollama)
   - `interface_format`: Interface format
   - `model_name`: Name of the main generation model (e.g., gpt-4, claude-3)
   - `temperature`: Creativity parameter (0-1, higher values increase creativity)
   - `max_tokens`: Maximum response length of the model
2. **Embedding Model Configuration**
   - `embedding_model_name`: Model name (e.g., text-embedding-ada-002)
   - `embedding_url`: Service URL
   - `embedding_retrieval_k`: Number of top-k embeddings to retrieve
3. **Novel Parameters Configuration**
   - `topic`: Core story theme
   - `genre`: Genre of the work
   - `num_chapters`: Total number of chapters
   - `word_number`: Target word count per chapter
   - `filepath`: Path to store generated files
---
## 🚀 Running Instructions
### **Method 1: Using Python Interpreter**
```bash
python main.py
```
After execution, the GUI will launch, and you can perform various operations through the graphical interface.
### **Method 2: Packaging as an Executable File**
If you want to use this tool on a machine without Python, you can package it using **PyInstaller**:
```bash
pip install pyinstaller
pyinstaller main.spec
```
After packaging, the executable file (e.g., `main.exe` on Windows) will be generated in the `dist/` directory.
---
## 📘 Usage Tutorial
1. **After launching, complete the basic parameter settings:**
   - **API Key & Base URL** (e.g., `https://api.openai.com/v1`)
   - **Model Name** (e.g., `gpt-3.5-turbo`, `gpt-4o`)
   - **Temperature** (0-1, determines the creativity of the text)
   - **Theme (Topic)** (e.g., "AI rebellion in a wasteland world")
   - **Genre** (e.g., "Sci-Fi" / "Fantasy" / "Urban Fantasy")
   - **Number of Chapters** and **Words per Chapter** (e.g., 10 chapters, about 3000 words per chapter)
   - **Save Path** (it is recommended to create a new output folder)
2. **Click 「Step1. Generate Settings」**
   - The system will generate based on the theme, genre, and number of chapters:
     - `Novel_setting.txt`: Contains world-building, character information, hidden plot points, etc.
   - You can view or modify the generated settings in the `Novel_setting.txt` file.
3. **Click 「Step2. Generate Directory」**
   - The system will generate a directory for all chapters based on the completed `Novel_setting.txt`:
     - `Novel_directory.txt`: Includes titles and brief descriptions for each chapter.
   - You can view, modify, or supplement chapter titles and descriptions in the generated file.
4. **Click 「Step3. Generate Chapter Draft」**
   - Before generating a chapter, you can:
     - **Set the chapter number** (e.g., fill in `1` for Chapter 1)
     - **Provide any expectations or prompts for the chapter** in the "Chapter Guidance" input box
   - Click the button, and the system will:
     - Automatically read the previous settings, `Novel_directory.txt`, and finalized chapters
     - Use vector retrieval to review the plot and ensure context coherence
     - Generate the chapter outline (`outline_X.txt`) and body (`chapter_X.txt`)
   - After generation, you can view and edit the chapter draft in the left text box.
5. **Click 「Step4. Finalize Current Chapter」**
   - The system will:
     - **Update the global summary** (written to `global_summary.txt`)
     - **Update character states** (written to `character_state.txt`)
     - **Update the vector retrieval library** (to ensure subsequent chapters can call the latest information)
     - **Update plot points** (e.g., `plot_arcs.txt`)
   - After finalization, you can see the finalized text in `chapter_X.txt`.
6. **Consistency Check (Optional)**
   - Click the 「[Optional] Consistency Review」 button to detect conflicts in the latest chapter, such as character logic and plot inconsistencies.
   - If conflicts are found, detailed prompts will be output in the log area.
7. **Repeat Steps 4-6** until all chapters are generated and finalized!
> **Vector Retrieval Configuration Tips**
> 1. The embedding model requires explicit specification of the interface and model name.
> 2. For **local Ollama** **Embedding**, the Ollama service must be started in advance:
>    ```bash
>    ollama serve  # Start the service
>    ollama pull nomic-embed-text  # Download/enable the model
>    ```
> 3. It is recommended to clear the `vectorstore` directory after switching different embedding models.
> 4. Ensure the required API permissions are enabled for cloud embedding.
```

---

## ❓ Troubleshooting
### Q1: Expecting value: line 1 column 1 (char 0)
This issue is likely caused by the API not responding correctly, possibly returning an HTML or other content, leading to this error.

### Q2: HTTP/1.1 504 Gateway Timeout?
Check if the API endpoint is stable and responsive.

### Q3: How to switch different Embedding providers?
You can input the corresponding details in the GUI interface.

* * *
If you have more questions or requirements, feel free to raise them in the **Project Issues**.
