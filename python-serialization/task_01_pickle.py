#!/usr/bin/python3

'''Serialize and deserialize custom Python objects using the pickle module'''

import pickle


class CustomObject:

    '''
    Class representing a custom object with name, age,
    and is_student attributes.
    '''

    def __init__(self, name, age, is_student):

        '''
        Initializes a new CustomObject.

        Args:
        name (str): The name of the object.
        age (int): The age of the object.
        is_student (bool): Indicates whether the object is a student (True)
        or not (False).
        '''

        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):

        '''
        Displays the object's attributes in the specified format.

        Example:
            Name: John
            Age: 25
            Is Student: True
        '''

        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):

        """
        Serializes the object and saves to a file.

        Args:
        filename (str): The name of the file where to save the serialized object.

        Reasons:
        FileNotFoundError: If the file does not exist.
        Exception: For any other error.
        """

        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
            print(f"Objet sérialisé enregistré dans {filename}")
        except FileNotFoundError:
            print(f"Erreur : Fichier '{filename}' introuvable.")
        except Exception as e:
            print(f"Erreur : {e}")

    @classmethod
    def deserialize(cls, filename):

        '''
        Deserializes an object from a file.

        Args:
        filename (str): The name of the file containing the serialized object.

        Returns:
        CustomObject: The deserialized object or None if an error occurs.

        Reasons:
        FileNotFoundError: If the file does not exist.
        Exception: For any other error.
        '''

        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
                return obj
        except FileNotFoundError:
            print(f"Error : File '{filename}' not found.")
        except Exception as e:
            print(f"Error : {e}")
            return None
