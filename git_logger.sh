if [[ "$1" == "add" || "$1" == "commit" || "$1" == "push" ]]; then
  # Do not log these commands, just pass them to git
  git "$@"
else
  # Log the command (with date and time) and pass it to git
  echo "$(date) git $@" >> ~/gitcounter/frequency.log
  git "$@"
fi
