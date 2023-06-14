#! /bin/bash
 if [[ ! -f /data/dictionary.db ]]; then
  echo "Couldn't find dictionary"
  curl "https://www.dropbox.com/s/ooctnlclt9bdmeu/dictionary.db" -o dictionary.db 
  mv dictionary.db /data/
  chmod +w /data/dictionary.db
  chown -R appuser:appuser /data/dictionary.db
 fi

  gunicorn 'app:app' --bind=0.0.0.0:8000