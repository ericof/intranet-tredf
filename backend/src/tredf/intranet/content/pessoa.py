from plone.autoform import directives
from plone.dexterity.content import Container
from plone.supermodel import model
from tredf.intranet import _
from z3c.relationfield.schema import RelationChoice
from zope import schema
from zope.interface import implementer


class IPessoa(model.Schema):
    """Definição de uma Pessoa."""

    cargo = schema.Choice(
        title=_("Cargo"),
        description=_("Selecione qual o cargo dessa pessoa no TRE-DF."),
        vocabulary="tredf.intranet.vocabulary.cargos",
        required=False,
    )

    area = RelationChoice(
        title=_("Área"),
        description=_("Selecione qual a área dessa pessoa no TRE-DF."),
        vocabulary="tredf.intranet.vocabulary.areas",
        required=False,
    )
    directives.widget("area", frontendOptions={"widget": "select"})


@implementer(IPessoa)
class Pessoa(Container):
    """Uma Pessoa colaboradora do TRE-DF."""
