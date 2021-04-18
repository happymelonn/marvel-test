## Start environment

```
$ docker-compose up
```

## To rebuild image

```
$ docker-compose up --build
```

## To check results on database
```
>get mysqldb container
$ docker ps

>run docker container on interactive mode
$ docker exec -it <container> bash

>inside bash logon to mysql
$ mysql -uroot -pp@ssw0rd1

$ USE outputdb;

$ SHOW TABLES;

```

## Where to check out output files -- go to 'outputfile' folder
