import configparser

class DBPropertyUtil:
    @staticmethod
    def get_connection_string(file_name):
        config = configparser.ConfigParser()
        config.read(file_name)

        section = config['DEFAULT']
        driver = section['driver']
        server = section['server']
        database = section['database']
        trusted_connection = section.get('trusted_connection', 'no')

        conn_str = (
            f"DRIVER={driver};"
            f"SERVER={server};"
            f"DATABASE={database};"
            f"Trusted_Connection={trusted_connection}"
        )

        return conn_str
