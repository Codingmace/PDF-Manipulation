import os

class UserData:
    '''Class for storing current user's application data'''

    def __init__(self):
        self.__user_data_path = os.path.join(DATA_DIR, 'data.json')
        self.__data_defaults = {
            'filedialog_path': USER_DIR,
            'number_of_processed_files': 0,
        }
        self.__user_data = self.__get_user_data()

    @property
    def filedialog_path(self):
        '''The last directory the user visited while opening or saving a file
        using a Tk File Dialog.

        The getter will first try to return the value stored in the
        instance, then try to read it out of the user data file, and if all else fails,
        set it to the user's home directory and return that value.

        The setter will set the according class instance property and save that property to
        a user data file. If no such file exists yet, one will be created.
        '''
        return self.__user_data.get('filedialog_path', self.__get_user_data()['filedialog_path'])

    @filedialog_path.setter
    def filedialog_path(self, val):
        self.__user_data['filedialog_path'] = val
        self.__save_user_data()

    @property
    def number_of_processed_files(self):
        '''Simple counter of PDF produced with PyPDF Builder

        The getter will first try to return the value stored in the state of the
        instance, then try to read it out of the user data file, and if all else fails,
        set it to 0 and return that value.

        The setter will set the according class instance property and save that property to
        a user data file. If no such file exists yet, one will be created.
        '''
        return self.__user_data.get('number_of_processed_files', self.__get_user_data()['number_of_processed_files'])

    @number_of_processed_files.setter
    def number_of_processed_files(self, val):
        self.__user_data['number_of_processed_files'] = val
        self.__save_user_data()

    def __get_user_data(self):
        '''Method to retrieve current user's data

        Return:
            dict: Dictionary of user data with keys:
                * `filedialog_path`: last accessed file path
                * `number_of_processed_files`: number of processed files
        '''
        try:
            with (open(self.__user_data_path, 'r')) as datafile:
                user_data = json.load(datafile)
            # make sure all values are returned. If a key is non-existant, fill it with default value
            for key, val in self.__data_defaults.items():
                if key not in user_data:
                    user_data[key] = val
        except FileNotFoundError:
            user_data = self.__data_defaults
        return user_data

    def __save_user_data(self):
        if not os.path.exists(os.path.dirname(self.__user_data_path)):
            plPath(os.path.dirname(self.__user_data_path)).mkdir(parents=True, exist_ok=True)
        try:
            with (open(self.__user_data_path, 'w')) as datafile:
                json.dump(self.__user_data, datafile)
        except FileNotFoundError:
            print('Something went horribly wrong while trying to save your current user data.')
