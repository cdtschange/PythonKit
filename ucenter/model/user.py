class User(object):
    uid = ''
    name = ''
    serializable = True
    
    
    def __init__(self):
        super(User, self).__init__()
        self.uid = ''
        self.name = ''
        self.serializable = True