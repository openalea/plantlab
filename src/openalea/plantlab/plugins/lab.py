from openalea.oalab.plugin.builtin.lab.default import DefaultLab
from openalea.core.plugin import PluginDef


@PluginDef
class PlantLab(DefaultLab):
    name = 'plant'
    alias = 'Plant'
    label = 'Plant'
    applets = DefaultLab.applets
    icon = 'icon_plantlab.png'

    connections = []
    def __call__(self, mainwin=None):
        if mainwin is None:
            return self.__class__
        # Load, create and place applets in mainwindow
        for name in self.applets:
            mainwin.add_plugin(name=name)
        # Initialize all applets
        mainwin.initialize()
