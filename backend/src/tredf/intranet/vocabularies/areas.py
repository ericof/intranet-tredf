from plone.app.vocabularies.catalog import StaticCatalogVocabulary
from plone.dexterity.content import DexterityContent
from zope.interface import provider
from zope.schema.interfaces import IVocabularyFactory


@provider(IVocabularyFactory)
def vocab_areas(context: DexterityContent) -> StaticCatalogVocabulary:
    """Áreas do TRE-DF."""
    return StaticCatalogVocabulary({
        "portal_type": ["Area"],
        "sort_on": "sortable_title",
    })
