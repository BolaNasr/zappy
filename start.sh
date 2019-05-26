tmux new-session -d -s angular "cd tweets/ ; ng serve --open" &
tmux new-session -d -s zappy "cd zappy_pro/ ; python3 manage.py migrate ;python3 manage.py runserver"&
tmux new-session -d -s starterbot "cd zappy_pro/  ;python3 manage.py migrate ;python3  bot.py "


