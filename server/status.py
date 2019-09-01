from enum import Enum


class Status(Enum):
    QUEUE = 'в очереди'
    IN_PROGRESS = 'выполняется'
    COMPLETED = 'выполнено'

