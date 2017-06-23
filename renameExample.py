from maya import cmds   

selection = cmds.ls(selection=True)

if len(selection) == 0:
    selection = cmds.ls(dag=True, long=True)

selection.sort(key=len, reverse=True)    

for obj in selection:
    shortName = obj.split("|")[-1]

    children = cmds.listRelatives(obj, children=True, fullPath=True) or []
    
    if len(children) == 1:
        child = children [0]
        objType = cmds.objectType(child)
    else:
        objType = cmds.objectType(obj)
        
    if objType == "mesh":
        suffix = "geo"
    elif objType == "joint":
        suffix = "jnt"
    elif objType == "transform":
        suffix = "grp"
    elif objType == "camera":
        print "skipping camera"
        continue
    else:
        suffix = "grp"
        
    newName = shortName + "_" + suffix
    
    
    cmds.rename(obj, newName)