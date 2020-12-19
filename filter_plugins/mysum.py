def mysum(list):
    return ( sum(list) + 10 ) 


class FilterModule(object):
    def filters(self):
        return {
            'mysum': mysum
        }