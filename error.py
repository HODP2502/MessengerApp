from datetime import datetime
from enum import Enum
from typing import Any, Dict


class Error(Enum):
    """Коды ошибок анализатора."""
    INVALID_METHOD_PARAMS = 1
    INVALID_TIME_PERIOD = 2
    SOURCE_IS_NOT_READY = 3
    UNKNOWN_SOURCE = 4
    UNKNOWN_MODEL = 5
    UNKNOWN_ERROR = 6

# NOTE: Определяем базовое исключение ошибок анализатора.
class AnalyzerError(Exception):
    def __init__(self, error_code=Error.UNKNOWN_ERROR):
        self.__error_code = error_code

    @property
    def error_code(self) -> Error:
        return self.__error_code

    @property
    def details(self) -> Dict[str, Any]:
        return {}


class InvalidMethodParameter(AnalyzerError):
    def __init__(self, param: str):
        super().__init__(Error.INVALID_METHOD_PARAMS)
        self.__param = param

    @property
    def details(self) -> Dict[str, Any]:
        return {
            'required param': self.__param
        }


class InvalidTimePeriod(AnalyzerError):
    def __init__(self, begin: datetime, end: datetime):
        super().__init__(Error.INVALID_TIME_PERIOD)
        self.__begin = begin
        self.__end = end

    @property
    def details(self) -> Dict[str, Any]:
        return {
            'begin': self.__begin,
            'end': self.__end,
        }


class DataSourceIsNotReady(AnalyzerError):
    def __init__(self, source: str):
        super().__init__(Error.SOURCE_IS_NOT_READY)
        self.__source = source

    @property
    def details(self) -> Dict[str, Any]:
        return {
            'source': self.__source
        }


class UnknownDataSource(AnalyzerError):
    def __init__(self, source: str):
        super().__init__(Error.UNKNOWN_SOURCE)
        self.__source = source

    @property
    def details(self) -> Dict[str, Any]:
        return {
            'source': self.__source
        }


class UnknownModel(AnalyzerError):
    def __init__(self, model: str):
        super().__init__(Error.UNKNOWN_MODEL)
        self.__model = model

    @property
    def details(self) -> dict:
        return {
            'model': self.__model
        }


if __name__ == '__main__':
    try:
        raise InvalidTimePeriod(datetime.now(), datetime.now())
    # NOTE: Обрабатываем ошибки анализатора штатным образом, любые другие - пропускаем.
    except AnalyzerError as error:
        print(error.error_code)
        print(error.details)