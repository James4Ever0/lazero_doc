import pywalk
def klean(node):
    am = []
    # real shit to make things work.
    @pywalk.walk(node)
    # what the fuck?
    # what if it is about some big, huge nodes?
    # we do not talk about it.
    def ak(node):
        # dir(node),
        # what is that is_leaf func?
        # use yleid?
        try:
            am.append((node.value, node.level, node.path))
            # print
            return True
        except:
            return None
        # print(">>>report", node.value, node.is_leaf,
            # node.is_root, node.key, node.level, node.path)
    # am=[]
    try:
        for x in ak(node):
            try:
                if x is not None:
                    # am.append(x)
                    pass
                else:
                    return am
                    # break
            except:
                return am
                # break
    except:
        return am
    return am