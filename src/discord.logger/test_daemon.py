import pytest
import daemon


def test_noenv():
    with pytest.raises(EnvironmentError):
        daemon._main(None)
