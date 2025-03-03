if [ "$1" = "up" ]; then
    cd environment/local
    docker compose up -d
elif [ "$1" = "down" ]; then
    cd environment/local
    docker compose down
elif [ "$1" = "build" ]; then
    cd environment/local
    docker compose build
else
    echo "Error: Invalid argument. Please use 'up' or 'down'."
fi
