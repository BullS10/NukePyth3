############### copy this in menu.py########################

# import Dots
# toolbar = nuke.toolbar("Nodes")
# toolbar.addCommand('Other/DotU', 'Dots.DotU()', 'shift+`')
# toolbar.addCommand('Other/DotD', 'Dots.DotD()', 'ctrl+`')

############################################################

import nuke

# Create dot on upper side
def DotU():
    selected = nuke.selectedNodes()
    if len(selected) < 2:
        nuke.message("Select at least two nodes")
        return

    one = selected[0]
    two = selected[1]

    dot = nuke.nodes.Dot()

    nxs = two.screenWidth()
    nys = one.screenHeight()

    nxp = int(two.xpos() + nxs / 2)
    nyp = int(one.ypos() + nys / 2)

    dot.setXpos(nxp)
    dot.setYpos(nyp)
    dot.setInput(0, one)
    nuke.autoplaceSnap(dot)

    dot_class_inputs = {
        "merge2", "channelmerge", "shufflecopy", "keymix", "addmix",
        "copybbox", "switch", "dissolve", "blend", "copy"
    }

    if two.Class().lower() in dot_class_inputs:
        two.setInput(1, dot)
    else:
        two.setInput(0, dot)

    # Select all involved nodes
    for sel in [one, two, dot]:
        sel['selected'].setValue(True)


# Create dot on lower side
def DotD():
    selected = nuke.selectedNodes()
    if len(selected) < 2:
        nuke.message("Select at least two nodes")
        return

    one = selected[0]
    two = selected[1]

    dot = nuke.nodes.Dot()

    nxs = one.screenWidth()
    nys = two.screenHeight()

    nxp = int(one.xpos() + nxs / 2)
    nyp = int(two.ypos() + nys / 2)

    dot.setXpos(nxp)
    dot.setYpos(nyp)
    dot.setInput(0, one)
    nuke.autoplaceSnap(dot)

    dot_class_inputs = {
        "merge2", "channelmerge", "shufflecopy", "keymix", "addmix",
        "copybbox", "switch", "dissolve", "blend", "copy"
    }

    if two.Class().lower() in dot_class_inputs:
        two.setInput(1, dot)
    else:
        two.setInput(0, dot)

    # Select all involved nodes
    for sel in [one, two, dot]:
        sel['selected'].setValue(True)
