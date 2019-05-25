# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class OntologyOntIdRegister(p.MessageType):

    def __init__(
        self,
        ont_id: str = None,
        public_key: bytes = None,
    ) -> None:
        self.ont_id = ont_id
        self.public_key = public_key

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('ont_id', p.UnicodeType, 0),
            2: ('public_key', p.BytesType, 0),
        }