class JsonUtils:
    @staticmethod
    def serialize(obj):
        json = {}
        for eachProp in obj.__dict__:
            val = obj.__dict__[eachProp]
            if isinstance(val, (list, tuple)):
                vlist = []
                for vv in val:
                    vvjson = JsonUtils.serialize(vv)
                    vlist.append(vvjson)
                json[eachProp] = vlist
                continue
            if hasattr(val, 'serializable'):
                json[eachProp] = JsonUtils.serialize(val)
                continue
            if eachProp == 'serializable':
                continue
            json[eachProp] = val
        return json