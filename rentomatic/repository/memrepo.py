import dataclasses

from rentomatic.domain.room import Room


@dataclasses.dataclass
class MemRepo:
    data: list

    def list(self):
        return [Room.from_dict(d) for d in self.data]
