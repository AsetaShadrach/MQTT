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

<font color='red'>DISCLAIMER</font> : THIS IS ONLY FOR DVELOPMENT <br>
For both cases use the `NGROK` link generated as the base URL<br>
e.g For a route `/home` if the ngrok generates `* ngrok tunnel "http://3735-102-1-138-209.ngrok.io" -> "http://127.0.0.1:5000"` <br>
then the full link will be `http://3735-102-1-138-209.ngrok.io/home`

### TODO

- Add pagination for get endpoints
- Add authentication for all endpoints
- Add callback processing for publish
- Use mqqt logging instead of python default