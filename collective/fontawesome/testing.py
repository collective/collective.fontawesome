from plone.app.testing import (
    PloneWithPackageLayer,
    IntegrationTesting,
    FunctionalTesting
)
import collective.fontawesome


FIXTURE = PloneWithPackageLayer(
    zcml_filename="configure.zcml",
    zcml_package=collective.fontawesome,
    additional_z2_products=[],
    gs_profile_id='collective.fontawesome:default',
    name="collective.fontawesome:FIXTURE"
)

INTEGRATION = IntegrationTesting(
    bases=(FIXTURE,), name="collective.fontawesome:Integration"
)

FUNCTIONAL = FunctionalTesting(
    bases=(FIXTURE,), name="collective.fontawesome:Functional"
)
