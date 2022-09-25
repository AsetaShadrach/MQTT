# MQTT

- Using paho mqtt since flask mqtt only allows one worker <br>
- Using postgres database

To initialize db run : <br>
`flask db init` <br>
`flask db migrate -m "Initial migration."`

The migration script needs to be reviewed and edited, as Alembic has issues with migrations e.g.not detecting table name changes

Then you can apply the migration to the database:

`flask db upgrade`

To run project:
- Without docker:<br>
  `flask run`
- With docker:<br>
  `docker-compose up --build`

### TODO

- Add pagination for get endpoints
- Add authentication for all endpoints
- Add callback processing for publish
- Use mqqt logging instead of python default