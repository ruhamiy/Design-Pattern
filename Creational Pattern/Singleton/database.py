class DatabaseConnection:
    _instance = None  

    def __new__(cls):
        
        if cls._instance is None:
            print("Creating new database connection...")
            cls._instance = super().__new__(cls)
            cls._instance._connected = False
        else:
            print("Using existing database connection...")
        return cls._instance

    def connect(self):
        if not self._connected:
            print("Connecting to database...")
            self._connected = True
        else:
            print("Already connected to database.")

    def disconnect(self):
        if self._connected:
            print("Disconnecting from database...")
            self._connected = False
        else:
            print("Database already disconnected.")

    def status(self):
        return "Connected" if self._connected else "Disconnected"


# CLIENT CODE

if __name__ == "__main__":

    db1 = DatabaseConnection()
    db1.connect()
    print("DB1 Status:", db1.status())

    print("\nCreating another reference...\n")

    db2 = DatabaseConnection()
    print("DB2 Status:", db2.status())

    print("\nAre db1 and db2 the same object?")
    print(db1 is db2)  