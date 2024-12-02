#!/bin/bash

show_info(){
    echo "=================================================================="
    echo "=================================================================="
    
    # Run the command and store the output in a variable
    distro=$(cat /etc/issue)
    echo -e "Service Running on: $distro"

    nodev=$(node -v)
    echo -e "Node version Running: $nodev"
    
    npmv=$(npm -v)
    echo -e "NPM version Running: $npmv"


    echo "=================================================================="
    echo -e "\n\n\n"
}

setup_app(){
    show_info
    # install_reqs
}

setup_app

cat <<EOT >> ~/.bashrc
    run(){
        npm start
    }
EOT

exec "$@"