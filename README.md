# MQTT

With the above application you can create a migration repository with the following command:

$ flask db init

This will add a migrations folder to your application. 
The contents of this folder need to be added to version control along with your other source files.

You can then generate an initial migration:

$ flask db migrate -m "Initial migration."

The migration script needs to be reviewed and edited, as Alembic has issues with migrations e.g.not detecting table name changes

Then you can apply the migration to the database:

$ flask db upgrade