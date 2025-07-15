# Ticket Agent

TODO

## Environment Setup

This project uses conda for virtual environment management and pip for package dependencies.

### Prerequisites

- [Conda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/products/distribution) installed on your system

### Creating the Environment

1. Create a new conda environment with Python 3.10:
   ```bash
   conda create -n ticket-agent python=3.10 -y
   ```

2. Activate the environment:
   ```bash
   conda activate ticket-agent
   ```

3. Install packages from requirements.txt:
   ```bash
   pip install -r requirements.txt
   ```

### Environment Variables

Create a `.env` file in the project root with:

```bash
DEEPSEEK_API_KEY=your_deepseek_api_key
OPENAI_API_KEY=your_openai_api_key
HF_TOKEN=your_huggingface_token
LANGCHAIN_API_KEY=your_langchain_api_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=your_project_name
```

### Git LFS

This project uses Git LFS for large files. Install Git LFS and set it up:

```bash
git lfs install
git lfs pull
```

### Code Formatting

This project uses Ruff for formatting and linting:

```bash
ruff format .
ruff check --fix .
```