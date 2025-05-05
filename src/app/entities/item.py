from typing import Tuple
from ..errors.entity_errors import ParamNotValidated
from ..enums.item_type_enum import ItemTypeEnum


class Item:
    name: str
    price: float
    item_type: ItemTypeEnum
    admin_permission: bool = False
    
    def __init__(self, name: str=None, price: float=None, item_type: ItemTypeEnum=None, admin_permission: bool=None):
        validation_name = self.validate_name(name)
        if validation_name[0] is False:
            raise ParamNotValidated("name", validation_name[1])
        self.name = name
        
        # Vamos validar o preco para garantir que ele exista, seja um float e seja positivo

        validation_item_type = self.validate_item_type(item_type)
        if validation_item_type[0] is False:
            raise ParamNotValidated("item_type", validation_item_type[1])
        self.item_type = item_type
        
        #Vamos validar a permissao de admin para garantir que ela exista e seja um booleano
        
    @staticmethod
    def validate_name(name: str) -> Tuple[bool, str]:
        if name is None:
            return (False, "Name is required")
        if type(name) != str:
            return (False, "Name must be a string")
        if len(name) < 3:
            return (False, "Name must be at least 3 characters long")
        return (True, "")
    
    # Vamos criar um metodo para validar o preco do item, garantindo que ele exista, seja um float e seja positivo

    @staticmethod
    def validate_item_type(item_type: ItemTypeEnum) -> Tuple[bool, str]:
        if item_type is None:
            return (False, "Item type is required")
        if type(item_type) != ItemTypeEnum:
            return (False, "Item type must be a ItemTypeEnum")
        return (True, "")
    
    # Vamos criar um metodo para validar a permissao de admin, garantindo que ela exista e seja um booleano
        
    @staticmethod
    def validate_item_id(item_id: int) -> Tuple[bool, str]:
        if item_id is None:
            return (False, "Missing 'item_id' parameter")

        if type(item_id) != int:
            return (False, "Parameter 'item_id' must be an integer")
        
        if item_id < 0:
            return (False, "Parameter 'item_id' must be a positive integer")

        return (True, "")
    
        
    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "item_type": self.item_type.value,
            "admin_permission": self.admin_permission
        }
    
    def __eq__(self,other):
        return self.name == other.name and self.price == other.price and self.item_type == other.item_type and self.admin_permission == other.admin_permission
    
    def __repr__(self):
        return f"Item(name={self.name}, price={self.price}, item_type={self.item_type}, admin_permission={self.admin_permission})"