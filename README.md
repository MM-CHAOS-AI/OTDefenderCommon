# OTDefenderCommon
Common utils for OTDefender code base

This module has the common modules reusable across all other projects.

Adding as a uv dependency
---------------------------------
uv add git+ssh://git@github.com/MM-CHAOS-AI/OTDefenderCommon.git

For Sync with latest code
-----------------------------------
uv lock --upgrade-package OTDefenderCommon

better command is uv sync --upgrade-package otdefendercommon


Script for running demo database localy
==============================================
cat runHSSQLD 
java -cp hsqldb-2.7.3.jar org.hsqldb.server.Server \
  --database.0 file:/home/user/Unix_Extra/OTDefender/DB_LOCAL/HSQLDB/HSSQLDB_FOLDER/otdef_demo_db \
  --dbname.0 otdef_demo_db


