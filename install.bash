create_virtual_environment() {
    if [ -d ./.venv ]; then
        echo "[WARNING] Virtual environment already exists. If you want to perform clean setup, delete '.venv' directory and re-run script."
    else
        echo "[INFO] Creating virtual environment in .venv directory..."
        python3.6 -m venv .venv
        echo "[INFO] Created."
    fi
}

install_python_requirements() {
    echo "[INFO] Installing  requirements..."
    source .venv/bin/activate && \
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
    python get-pip.py && \
    pip install --upgrade setuptools && \
    pip install flake8 && \
    pip install mypy && \
    pip install pytest && \
    pip install addict && \
    pip install -r $1
    echo "[INFO] Requirements $1 have been installed."
}

create_virtual_environment
install_python_requirements "requirements.txt"
# bash "./installers/$1.bash"
