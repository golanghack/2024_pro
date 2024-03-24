# Dockerizong Django app with Postgres, Gunicorn, nginx

### DEV
1.rename *.env.dev-sample* to *.env.dev*.
2.update environment variables in the *docker-compose.yml and *.env.dev
3.build images
```sh
$ docker-compose up -d --build
```

### PROD
1.rename *.env.prod-sample* to *.env.prod and *.env.prod.db-sample to *.env.prod.db-sample
2.update variables
3.build images
```sh
$ docker-compose -f docker-compose.prod.yml up -d --build
``` 
