import pytest

from .service import ServiceError
from .production_service import ProductionService


def test_ok():
    instance_a = ProductionService('One')
    instance_b = ProductionService('One')
    instance_c = ProductionService('Two')

    instance_a.do_some_work('sub_key')
    instance_b.do_some_work('key')

    with pytest.raises(ServiceError):
        instance_c.do_some_work('test')
