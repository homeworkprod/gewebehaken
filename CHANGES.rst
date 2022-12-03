Changelog
=========


0.3 (2022-12-04)
-----------------

- Added support for Python 3.10.

- Updated blinker to v1.5 (from v1.4).

- Updated Flask to v2.2.2 (from v1.1.2).

- Updated Werkzeug to v2.2.2 (from v1.0.1).

- Move continuous integration from Travis CI to GitHub Actions.


0.2 (2022-12-03)
----------------

Developed from 2021-02-25 to 2021-02-26.

- Dropped support for Python 3.4.

- Changed supported Python versions to 3.7, 3.8, and 3.9.

- Updated blinker to v1.4 (from v1.3).

- Updated Flask to v1.1.2 (from v0.10.1).

- Updated Werkzeug to v1.0.1 (from v0.15.0).

- Ported tests from unittest and nose2 to pytest.

- Remove usage of tox.

- Switched codebase to ``src/`` package layout.

- Moved package configuration from ``setup.py`` to ``setup.cfg``.

- Turned ``run_gewebehaken.py`` script into actual console entrypoint
  script.

- Make log filename optional and configurable via command-line argument
  ``--logfile``.

- Require ``target_account_screen_name`` key to be passed to Twitter
  endpoints.


0.1 (unreleased)
----------------

Developed from 2015-06-28 to 2015-08-10.

Initial implementation
