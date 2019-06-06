# Mediterranean Archaeology (Med-Arch)
> Under super vision of [Dr. Scott Mann](https://scholars.latrobe.edu.au/display/smann)

Mediterranean Archaeology project (Med-Arch) is a Python's Django and Bootstrap based application, which extracts data from a large set of images and a large pdf, then stores the data in a Postgres database and displays the records.

#### Team
* Biswas Nandamuri
* Hema Priya Movva
* Krishna Mohan Chiluveru

#### Original Project Report
Please check the [original project report](https://docs.biswas.coffee/Mediterranean-Archaeology.pdf) summited at the university.

### Technologies

Med-Arch uses a number of open source projects to work properly:

* [Django] - awesome web-based text editor
* [SQLAlchemy] - Markdown parser done right. Fast and easy to extend.
* [Bootstrap] - great UI boilerplate for modern web apps

### Installation

Dillinger requires [Python](https://nodejs.org/) v4+ to run.

##### Clone the repository.

```sh
$ cd YOUR_WORK_DIRECTORY
$ git clone https://github.com/Biswas-N/Mediterranean-Archaeology.git
$ cd Mediterranean-Archaeology
```

##### Install the dependencies and devDependencies.

Using Pipenv (creates a new Environment) (or)
```sh
$ pipenv --three
$ pipenv install
$ pipenv shell // To activate your env
```

Using Pip
```sh
$ pip install -r requirements.txt
```

Create your database tables (Using Django migrations)
> _For this, you need postgres installed in your PC/MAC. You can either use native software or [Docker image](https://hub.docker.com/_/postgres)_
```sh
$ py manage.py migrate
```

Start you dev server on port 8888
```sh
$ py manage.py runserver 0.0.0.0:8888
```

License
----

MIT
