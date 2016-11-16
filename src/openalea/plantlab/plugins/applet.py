from openalea.core.plugin import PluginDef
from openalea.core.authors import cpradal

#from openalea.oalab.plugins.applets import PluginApplet


@PluginDef
class Viewer3D(object):

    name = 'Viewer3D'
    label = 'Viewer'
    icon = 'icon_viewer.png'

    authors = [cpradal]
    tags = ['3d']

    def __call__(self):
        # Load and instantiate graphical component that actually provide feature
        from openalea.plantlab.view3d import Viewer
        return Viewer

    def graft(self, **kwds):
        mainwindow = kwds['oa_mainwin'] if 'oa_mainwin' in kwds else None
        applet = kwds['applet'] if 'applet' in kwds else None
        if applet is None or mainwindow is None:
            return

        from openalea.oalab.service.plot import register_plotter

        self._fill_menu(mainwindow, applet)
        register_plotter(applet)
        mainwindow.add_applet(applet, self.alias, area='outputs')
