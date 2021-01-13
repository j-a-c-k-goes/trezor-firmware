# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

from .Memo import Memo

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class TxAckPaymentRequest(p.MessageType):
    MESSAGE_WIRE_TYPE = 37

    def __init__(
        self,
        *,
        recipient_name: str,
        hash_outputs: bytes,
        amount: int,
        signature: bytes,
        memos: List[Memo] = None,
        nonce: bytes = None,
    ) -> None:
        self.memos = memos if memos is not None else []
        self.recipient_name = recipient_name
        self.hash_outputs = hash_outputs
        self.amount = amount
        self.signature = signature
        self.nonce = nonce

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('recipient_name', p.UnicodeType, p.FLAG_REQUIRED),
            2: ('hash_outputs', p.BytesType, p.FLAG_REQUIRED),
            3: ('amount', p.UVarintType, p.FLAG_REQUIRED),
            4: ('memos', Memo, p.FLAG_REPEATED),
            5: ('nonce', p.BytesType, None),
            6: ('signature', p.BytesType, p.FLAG_REQUIRED),
        }