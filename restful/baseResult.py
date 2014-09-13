class BaseResult(object):
    
    status = 0
    msg = ''
    serializable = True
        
    def __init__(self):
        super(BaseResult, self).__init__()
        self.status = 0
        self.msg = ''
        self.serializable = True