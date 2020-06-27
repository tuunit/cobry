class Flag:
    def __init__(
            self,
            typ,
            name,
            value,
            usage=None,
            def_value=None,
            shorthand=None,
            no_opt_def_val=None,
            changed=False,
            deprecated=False,
            hidden=False):
        self.typ = typ
        self.name = name
        self.shorthand = shorthand
        self.usage = usage
        self.value = value
        self.def_value = def_value
        self.no_opt_def_val = no_opt_def_val
        self.changed = changed
        self.deprecated = deprecated
        self.hidden = hidden

    def get_value(self):
        return self.value

    def set_value(self, value):
        try:
            if self.typ == bool:
                self.value = bool(value)
            elif self.typ == float:
                self.value = float(value)
            elif self.typ == int:
                self.value = int(value)
            else:
                self.value = str(value)
            return None
        except (ValueError, TypeError):
            # TODO
            print('ValueError Warning')
            self.value = str(value)
            return ValueError()
