from src import Aspectable

from .service import Service

from .aspects import life_aspect, deprecation_aspect_factory


deprecation_aspect = deprecation_aspect_factory([
    'test', 'sub_key'
])


class ProductionService(Service, metaclass=Aspectable, aspect_set=[
    life_aspect, deprecation_aspect
]):
    pass
