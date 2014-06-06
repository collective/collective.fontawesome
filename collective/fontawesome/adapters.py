from plone.app.layout.icons.icons import CatalogBrainContentIcon


class FontAwesomeIconReplacer(CatalogBrainContentIcon):
    """ Custom IContentIcon adapter. This is used by @@ploneview to
        determine which icons to render.

        We want to prevent the rendering of icons, so that FontAwesome fonts
        will render instead.

        For example, in folder listing. See
            Products.CMFPlone.skins.plone_content.folder_listing.pt
    """

    @property
    def url(self):
        return None
