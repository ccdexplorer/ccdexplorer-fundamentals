import pytest
from ccdexplorer_fundamentals.cis import CIS, MetadataUrl


@pytest.fixture
def cis():
    return CIS()


def test_cis3_nonce_event(cis: CIS):
    # from hash d4cc213b54b10b0dfa2c6a95e4e850ed9b92d465f45082bf59014e1830375f7f
    hex = "fa0e00000000000000c18c1cb58a9208343b67a3b9abadf542bf61c7527124e22092ed4bc1895166c4"
    parsed_result = cis.nonceEvent(hex)
    assert parsed_result.tag == 250
    assert parsed_result.nonce == "14"  # Nonce can become too big, so store as str.
    assert (
        parsed_result.sponsoree == "4Qz5oPgm1Vah9kCGTzBaeCrJ9BjeYXnchEu5Vrh1aMqQgLtqHd"
    )
    # TODO: need to find a suitable test tx
    pass
    # from hash 5382e43c9fe252d66b56b00a7ce84168531336118cf37c6fa09d21b3c79e1db6
    # hex = "fe04619d104201005a398a949d41d7569a48051d34795ffa945dcf0afa4501689421c255a327d2db"
    # parsed_result = cis.nonceEvent(hex)
    # assert parsed_result.tag == 250
