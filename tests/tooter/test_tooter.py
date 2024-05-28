import pytest
import sys
import os


sys.path.append(os.path.dirname("ccdexplorer_fundamentals"))
from ccdexplorer_fundamentals.tooter import Tooter, TooterChannel, TooterType
from rich import print


@pytest.fixture
def tooter():
    return Tooter()


@pytest.mark.asyncio
async def test_send_async_relay(tooter: Tooter):
    await tooter.async_relay(
        TooterChannel.NOTIFIER,
        "Test async body",
        TooterType.INFO,
        "Test async Title",
        913126895,
    )


def test_send_relay(tooter: Tooter):
    tooter.relay(
        TooterChannel.NOTIFIER,
        "Test regular body",
        TooterType.INFO,
        "Test regular Title",
        913126895,
    )
