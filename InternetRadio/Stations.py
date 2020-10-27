class Stations:
    def __init__(self):
        self.data = self.pinguin()

    @staticmethod
    def pinguin():
        return {
            'Indie': {
                'logo': 'indie.png',
                'genre': 'indie',
                'url': 'https://streams.pinguinradio.com/PinguinRadio192.mp3'
            },
            'Classic': {
                'logo': 'classic.png',
                'genre': 'classic',
                'url': 'http://streams.pinguinradio.com/PinguinClassics192.mp3'
            },
            'Rock': {
                'logo': 'rock.png',
                'genre': 'rock',
                'url': 'https://streams.pinguinradio.com/PinguinOnTheRocks192.mp3'
            },
            'Pop': {
                'logo': 'pop.png',
                'genre': 'pop',
                'url': 'https://samcloud.spacial.com/api/listen?sid=98586&m=sc&rid=174409'
            },
            'Grooves': {
                'logo': 'grooves.png',
                'genre': 'groove',
                'url': 'https://samcloud.spacial.com/api/listen?sid=98587&m=sc&rid=174412'
            },
            'Pluche': {
                'logo': 'pluche.png',
                'genre': 'pluche',
                'url': 'https://samcloud.spacial.com/api/listen?sid=98569&m=sc&rid=174384'
            },
            'Aardschok': {
                'logo': 'aardschok.png',
                'genre': 'progressive',
                'url': 'http://streams.pinguinradio.com/Aardschok192.mp3'
            },
            'Fiësta': {
                'logo': 'fiesta.png',
                'genre': 'fiësta/party',
                'url': 'https://19293.live.streamtheworld.com/SP_R2292843_SC'
            },
            'Blues': {
                'logo': 'blues.png',
                'genre': 'blues',
                'url': 'https://samcloud.spacial.com/api/listen?sid=93462&m=sc&rid=168006'
            },
            'World': {
                'logo': 'world.png',
                'genre': 'world',
                'url': 'https://samcloud.spacial.com/api/listen?sid=98570&m=sc&rid=174387'
            },
            'Showcase': {
                'logo': 'showcase.png',
                'genre': 'experimental',
                'url': 'https://samcloud.spacial.com/api/listen?sid=110690&m=sc&rid=190799'
            },
            '': {
                'logo': 'sleep.png',
                'genre': '',
                'url': ''
            }

        }