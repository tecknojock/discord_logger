import pytest
import discord.logger.daemon as daemon


def test_noenv():
    with pytest.raises(EnvironmentError):
        daemon._main(None)
