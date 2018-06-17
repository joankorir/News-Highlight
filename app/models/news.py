class News:
    '''
    News class to define news highlight Objects
    '''

    def  __init__(self,id,title,overview,image,timeCreated):
        self.id =id
        self.title = title
        self.overview = overview
        self.image = 'https://image.tmdb.org/t/p/w500/'+image
        self.timeCreated = timeCreated