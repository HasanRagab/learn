class TV:
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print("TV is ON")

    def turn_off(self):
        self.is_on = False
        print("TV is OFF")

class SoundSystem:
    
    def __init__(self):
        self.__volume = 5

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def set_volume(self, volume):
        self.__volume = volume
        print(f"Volume set to {volume}")

class BluRayPlayer:
    
    def __init__(self):
        self.__movie = None

    @property
    def movie(self):
        return self.__movie

    @movie.setter
    def play_movie(self, movie):
        self.__movie = movie
        print(f"Playing {movie}")
        
class HomeTheaterFacade:
    def __init__(self, tv: TV, sound_system: SoundSystem, blu_ray: BluRayPlayer):
        self.tv = tv
        self.sound_system = sound_system
        self.blu_ray = blu_ray

    def watch_movie(self, movie):
        if not self.tv.is_on:
            self.tv.turn_on()
        if self.sound_system.volume < 10:
            self.sound_system.set_volume = 10
        self.blu_ray.play_movie = movie
        
home_theater = HomeTheaterFacade(TV(), SoundSystem(), BluRayPlayer())

print(home_theater.tv.is_on, home_theater.sound_system.volume, home_theater.blu_ray.movie)
print("###")
home_theater.watch_movie("Inception")
print("###")
print(home_theater.tv.is_on, home_theater.sound_system.volume, home_theater.blu_ray.movie)
