import pytest

from .base import Advice


@pytest.fixture
def instance():
    return Advice()


def test_get_proxy_ok(instance):
    def _get_runtime(args, kwargs):
        pass

    instance._get_runtime = _get_runtime

    assert instance.get_proxy(lambda x: x)


def test_get_runtime_error_not_implemented(instance):
    with pytest.raises(NotImplementedError):
        instance._get_runtime([], {})
