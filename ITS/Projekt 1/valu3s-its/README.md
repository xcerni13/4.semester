# VALU3S web

## Start

Use [Docker](https://docs.docker.com/get-started/) and
[docker-compose](https://docs.docker.com/compose/) to build and run the VALU3S
web in a separated container:

    $ docker-compose up -d

Note that the first build will take 3-20 minutes (depending on performance of
your machine and connection speed).

Access the web in http://localhost:8080/VALU3S

Initial credentials are:

| Login  | Password | Type |
|--------|----------|------|
| admin     | admin     | Main administrator    |
| itsadmin  | itsadmin  | Testing administrator |
| itsreviewer | itsreviewer | Testing reviewer      |

## Stop

Stop the container using:

    $ cd path/to/valu3s-its
    $ docker-compose down

## Restore original data

The database of the web is stored in `filestorage` directory. To restore the
original data, simply stop the container, restore the directory, and run it
again:

    $ cd path/to/valu3s-its
    $ docker-compose down
    $ git reset --hard
    $ docker-compose up -d
