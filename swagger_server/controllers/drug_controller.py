import connexion
import six

from swagger_server.models.drug import Drug  # noqa: E501
from swagger_server.models.error import Error  # noqa: E501
from swagger_server import util


def createdrug(body):  # noqa: E501
    """Метод добавления нового льготного лекарства в каталог

    Метод предназначен для сохранения в БД данных по новому льготному лекарству. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Drug
    """
    if connexion.request.is_json:
        body = Drug.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def deletedrug_by_id(id):  # noqa: E501
    """Метод удаления льготного лекарства по идентификатору

     # noqa: E501

    :param id: Идентификатор льготного лекарства
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def getdrug_by_id(id):  # noqa: E501
    """Метод получения льготного лекарства по идентификатору

     # noqa: E501

    :param id: Идентификатор льготного лекарства
    :type id: str

    :rtype: Drug
    """
    return 'do some magic!'


def getdrug_byexpiration(expiration):  # noqa: E501
    """Метод получения льготных лекарств по сроку годности

     # noqa: E501

    :param expiration: Срок годности льготного лекарства
    :type expiration: str

    :rtype: List[Drug]
    """
    return 'do some magic!'


def getdrugs():  # noqa: E501
    """Метод получения списка льготных лекарств

    Метод предназначен для получения списка всех льготных лекарств, сохраненных в БД. # noqa: E501


    :rtype: List[Drug]
    """
    return 'do some magic!'


def updatedrug(body, id):  # noqa: E501
    """Метод обновления льготного лекарства в каталоге

    Метод предназначен для обновления в БД данных по имеющемуся льготнму лекарству. # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param id: Идентификатор льготного лекарства
    :type id: str

    :rtype: Drug
    """
    if connexion.request.is_json:
        body = Drug.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
