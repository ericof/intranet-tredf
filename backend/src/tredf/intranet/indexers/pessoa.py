from plone import api
from plone.indexer import indexer
from tredf.intranet.content.pessoa import IPessoa
from tredf.intranet.content.pessoa import Pessoa


@indexer(IPessoa)
def area_indexer(obj: Pessoa) -> str | None:
    """Retorna o UUID da área relacionada à pessoa para indexação."""
    if area_rel := obj.area:
        area = area_rel.to_object
        return api.content.get_uuid(area)


@indexer(IPessoa)
def cargo_indexer(obj: Pessoa) -> str | None:
    """Retorna o cargo da pessoa para indexação."""
    return obj.cargo if obj.cargo else None
