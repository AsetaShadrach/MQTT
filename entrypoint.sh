#!/bin/bash

flask run;

flask db migrate;

flask db upgrade;