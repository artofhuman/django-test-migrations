# -*- coding: utf-8 -*-

from typing import Optional, Tuple

from django.core.management import call_command
from django.db import DEFAULT_DB_ALIAS, connections
from django.db.migrations.executor import MigrationExecutor
from django.db.migrations.state import ProjectState

# Regular or rollback migration: 0001 -> 0002, or 0002 -> 0001
# Rollback migration to initial state: 0001 -> None
_Migration = Tuple[str, Optional[str]]


class Migrator(object):
    """
    Class to manage your migrations and app state.

    It is designed to be used inside the tests to ensure that migrations
    are working as intended: both data and schema migrations.

    This class can be but probably should not be used directly.
    Because we have utility test framework
    integrations for ``unitest`` and ``pytest``.

    Use them for better experience.
    """

    def __init__(
        self,
        database: Optional[str] = None,
    ) -> None:
        """That's where we initialize all required internals."""
        if database is None:
            database = DEFAULT_DB_ALIAS

        self._database: str = database
        self._executor = MigrationExecutor(connections[self._database])

    def before(self, migrate_from: _Migration) -> ProjectState:
        """Reverse back to the original migration."""
        return self._executor.migrate([migrate_from])

    def after(self, migrate_to: _Migration) -> ProjectState:
        """Apply the next migration."""
        self._executor.loader.build_graph()  # reload.
        return self._executor.migrate([migrate_to])

    def reset(self) -> None:
        """Reset the state to the most recent one."""
        return call_command('migrate')
