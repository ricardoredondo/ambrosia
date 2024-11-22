#!/bin/bash

show_info(){
    echo "=================================================================="
    echo "=================================================================="
    
    # Run the command and store the output in a variable
    distro=$(cat /etc/issue)
    echo -e "Service Running on: $distro"

    pythonv=$(python --version 2>&1)
    echo -e "Python version Running: $pythonv"
    
    echo "=================================================================="
    echo -e "\n\n\n"
}


install_reqs(){
    echo "Upgrade PIP Version"
    pip install --upgrade pip
    
    echo "Installing requirements"exit
    FILE="./requirements.txt"
    if [ -e "$FILE" ]; then
        echo "Requirements Exist. All good. Thanks for asking."
    else
        echo "File does not exist. Creating the requirements.txt file"
        touch requirements.txt
    fi

    pip install --no-cache-dir -r requirements.txt
}


cat <<EOT >> ~/.bashrc
    run(){
        python app.py
    }
EOT


setup_app(){
    show_info
    install_reqs
}

setup_app

exec "$@"