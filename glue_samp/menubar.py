from __future__ import print_function, division, absolute_import

from glue.config import menubar_plugin
from glue.utils.qt import get_qapp

from glue_samp.samp_state import SAMPState
from glue_samp.qt.samp_client import QtSAMPClient
from glue_samp.qt.layer_actions import add_samp_layer_actions

samp_widget = None


@menubar_plugin("Open SAMP plugin")
def samp_plugin(session, data_collection):

    global samp_widget

    if samp_widget is None:

        state = SAMPState()
        samp_widget = QtSAMPClient(state=state, data_collection=data_collection)

        # We now add actions to the data collection - however we don't use
        # the @layer_action framework because we want to be able to add
        # sub-menus. TODO: expand @layer_action framework to allow sub-menus.

        add_samp_layer_actions(session, state)

    samp_widget.show()
    samp_widget.raise_()

    app = get_qapp()
    app.aboutToQuit.connect(samp_widget.stop_samp)
