Basic Installation
##################

These instructions cover an installation from the master branch in git.

Prerequisites
*************

The following prerequisites are required to run RocketMAD:

 * `MAD MySQL database <https://mad-docs.readthedocs.io/en/latest/installation/manual/#mariadb>`_
 * Python 3.6+
 * pip3
 * `node and npm <https://nodejs.org/en/download/package-manager/>`_

Downloading the Application
***************************

To run a copy from the latest ``master`` branch in ``git`` you can clone the repository:

.. code-block:: bash

  git clone https://github.com/cecpk/RocketMAD.git

Installing Modules
******************

At this point you should have the following:

 * Python 3.6+
 * pip3
 * RocketMAD application folder

First, open up your shell and change to the directory of RocketMAD.

You can verify your installation like this:

.. code-block:: bash

  python3 --version
  pip3 --version

The output should look something like:

.. code-block:: bash

  $ python3 --version
  Python 3.6.0
  $ pip3 --version
  pip 9.0.1 from /usr/lib/python3/dist-packages (python 3.6)

Now you can install all the Python dependencies, make sure you're still in the directory of RocketMAD:

.. code-block:: bash

  pip3 install -r requirements.txt

.. note:: It's highly recommended to use a `virtual environment <https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments>`_. A virtual environment is a Python environment such that the Python interpreter, libraries and scripts installed into it are isolated from those installed in other virtual environments.

Building Front-End Assets
===========================

In order to run from a git clone, you must compile the front-end assets with node. Make sure you have `node <https://nodejs.org/en/download/package-manager/>`_ installed for your platform.

Once node/npm is installed, open a shell and validate your install:

.. code-block:: bash

  node --version
  npm --version

The output should look something like:

.. code-block:: bash

  $ node --version
  v10.15.3
  $ npm --version
  6.0.1

Once node/npm is installed, you can install the node dependencies and build the front-end assets:

.. code-block:: bash

  npm install
  npm run build


Basic Launching
***************

Once those have run, you should be able to start using the application, make sure you're in the directory of RocketMAD then:

.. code-block:: bash

  python3 runserver.py --help

Read through the available options and set all the required CLI flags to start your own server. At a minimum you will need to provide a location.

The most basic config you could use would look something like this:

.. code-block:: bash

 python3 runserver.py -l "a street address or lat/lng coords here"

**Once your setup is running, open your browser to http://localhost:5000 and your pokemon will begin to show up! Happy hunting!**

Things to Know
**************

 * All of these flags can be set inside of a configuration file to avoid clutter in the command line. Go `here <http://rocketmad.readthedocs.io/en/latest/first-run/configuration-files.html>`_ to see how.
 * A full list of all commands are available `here. <https://rocketmad.readthedocs.io/en/latest/first-run/commandline.html>`_
 * A few tools to help you along the way are located `here. <https://rocketmad.readthedocs.io/en/latest/extras/Community-Tools.html>`_


Updating the Application
************************

RocketMAD is a very active project and updates often. You can follow the `latest changes <https://github.com/cecpk/RocketMAD/tree/master>`_ to see what's changing.

You can update with a few quick commands:

.. code-block:: bash

  git pull
  pip3 install -r requirements.txt --upgrade
  npm run build

Watch the `latest changes <https://github.com/cecpk/RocketMAD/tree/master>`_ on `Discord <https://discord.com/invite/arKePet>`_ to know when updating will require commands other than above.

**IMPORTANT** Some updates will include database changes that run on first startup. You should run only **one** ``runserver.py`` command until you are certain that the DB has been updated. You will know almost immediately that your DB needs updating if **Detected database version x, updating to x** is printed in the console. This can take a while so please be patient. Once it's done, you can start all your instances like you normally would.
