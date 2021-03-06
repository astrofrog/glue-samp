from __future__ import print_function, division, absolute_import

from glue.config import menubar_plugin
from glue.utils.qt import get_qapp

from glue_samp.samp_state import SAMPState
from glue_samp.samp_receiver import SAMPReceiver
from glue_samp.qt.samp_options import SAMPOptions
from glue_samp.qt.layer_actions import add_samp_layer_actions

# Here we describe what we want the behavior to be under different scenarios.
# First we consider the case of another application sending a SAMP message to
# Glue
#
# table.load.votable, table.load.fits, and image.load.fits: load data if not
# already loaded (based on table-id or image-id)
#
# table.select.rowList: update subset or create new subset based on currently
#                       selected subset in glue (as if external application was
#                       just another viewer)
#
# table.highlight.row: should have an option that if enabled will treat this as
#                      a selection (but by default not?)
#
# Next we define what messages we can emit from glue:
#
# table.load.votable, table.load.fits, and image.load.fits: we should be able to
# send this by control-clicking on datasets in the data collection. Doing this
# could assign a table-id or image-id in the Data.meta.
#
# Table.select.rowList: we should be able to send this by control-clicking on
# subset groups or subsets in the data collection. Only subsets for datasets
# that have a table-id or image-id should be sent.
#
# A full list of 'standard' mtypes can be found here:
#
# http://wiki.ivoa.net/twiki/bin/view/IVOA/SampMTypes#table_load

# Main to-dos:
#
# - Develop a SAMP widget from where we can start the hub, and see messages
#   sent/received. This could potentially be developed in a glue-agnostic way.
# - Make it so that we can add arbitrary layer actions
# - Implement layer actions to send data/subsets
# - Implement image loading

samp_widget = None


@menubar_plugin("Open SAMP plugin")
def samp_plugin(session, data_collection):

    global samp_widget

    if samp_widget is None:

        state = SAMPState()
        receiver = SAMPReceiver(state=state, data_collection=data_collection)
        samp_widget = SAMPOptions(state=state, receiver=receiver)

        # We now add actions to the data collection - however we don't use
        # the @layer_action framework because we want to be able to add
        # sub-menus. TODO: expand @layer_action framework to allow sub-menus.

        add_samp_layer_actions(session, state)

    samp_widget.show()
    samp_widget.raise_()

    app = get_qapp()
    app.aboutToQuit.connect(state.stop_samp)
