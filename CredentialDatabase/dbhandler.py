import logging
from CredentialDatabase.db.connector import DBConnector
from CredentialDatabase.db.creator import DBCreator
from CredentialDatabase.db.fetcher import DBFetcher
from CredentialDatabase.db.inserter import DBInserter


class DBHandler:
    """ class DBHandler to provide database actions to subclasses

    USAGE:
            dbhandler = DBHandler()

    """
    def __init__(self, password_db, **dbparams):
        self.logger = logging.getLogger('CredentialDatabase')
        self.logger.info('create class DBHandler')

        self.password_db = password_db

        if ('host' and 'port' and 'username' and 'password' and 'dbname') in dbparams.keys():
            self.db_host = dbparams['host']
            self.db_port = dbparams['port']
            self.db_username = dbparams['username']
            self.db_password = dbparams['password']
            self.db_name = dbparams['dbname']
        else:
            self.logger.error("no database params provided!")

        DBConnector.connect_psycopg(host=self.db_host, port=self.db_port, username=self.db_username,
                                    password=self.db_password, dbname=self.db_name, minConn=1, maxConn=10)

        self.dbcreator = DBCreator()
        self.dbfetcher = DBFetcher()
        self.dbinserter = DBInserter()

        self.structure = '0123456789abcdefghijklmnopqrstuvwxyz'

    def create_schemas_and_tables(self):
        """ creates schemas and tables in database

        """
        self.logger.info("create schemas and tables in database")
        schema_list = list(self.structure)
        schema_list.append('symbols')

        for schema in schema_list:
            self.logger.info("create schema {}".format(schema))
            schema_sql = "create schema if not exists \"{}\"".format(schema)
            self.dbinserter.sql(sql=schema_sql)

            if schema == 'symbols':
                if self.password_db:
                    table_sql = "create table if not exists \"{}\".symbols (id bigint, password text primary key, length bigint, isNumber boolean, isSymbol boolean);".format(schema)
                else:
                    table_sql = "create table if not exists \"{}\".symbols (id bigint primary key, email text, password text, username text, provider text, sha1 varchar(40), sha256 varchar(64), sha512 varchar(128), md5 varchar(32));".format(schema)
                self.dbinserter.sql(sql=table_sql)

            else:
                for table in schema_list:
                    if self.password_db:
                        table_sql = "create table if not exists \"{}\".\"{}\" (id bigint, password text primary key, length bigint, isNumber boolean, isSymbol boolean);".format(schema, table)
                    else:
                        table_sql = "create table if not exists \"{}\".\"{}\" (id bigint primary key, email text, password text, username text, provider text, sha1 varchar(40), sha256 varchar(64), sha512 varchar(128), md5 varchar(32));".format(schema, table)
                    self.dbinserter.sql(sql=table_sql)
