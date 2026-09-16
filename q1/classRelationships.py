class APPS:

 def __init__(self, name, developer, price, available, settings, profile):
  self.name = name
  self.developer = developer
  self.__settings = settings
  self.available = available
  self.profile = profile
  self.price = price

 def Launch(self):
    print(self.name, "has been launched.")

 def Updateversion(self, versionNumber, string):
    self.__settings = string
    print(self.name, "has been updated to version", versionNumber)

 def Download(self):
     if self.available:
        print(self.name, "is downloading.")
     else:
        print(self.name, "is not available for download.")

 def get_settings(self):
     return self.__settings


 def display_info(self):
     print("App Name:", self.name)
     print("Developer:", self.developer)
     print("Price:", self.price)
     print("Available:", self.available)
     print("Profile:", self.profile)

# Create Objects
object1 = APPS("Among Us", "Innersloth", 4.99, True, "Light mode", "Player467")
object2 = APPS("Minecraft", "Mojang", 6.99, True, "Dark Mode", "Gamergirl123")
object3 = APPS("Tiktok", "Zhang Yiming", 0, True, "Dark Mode", "Starrynights11")

#Implementing Methods
print("APPS")

print("--- BEFORE ---")

print("Object 1:")
object1.display_info()
print()

print("Object 2:")
object2.display_info()
print()

print("Object 3:")
object3.display_info()


# Using methods on Object 1
print("--- IMPLEMENTING METHODS ---")

print("Launching Object 1:")
object1.Launch()

print("Downloading Object 1:")
object1.Download()

print("Updating Object 1:")
object1.Updateversion("2.0", "Dark Mode")


# Show that only Object 1 changed
print("--- AFTER ---")

print("Object 1:")
object1.display_info()

print("Object 2:")
object2.display_info()

print("Object 3:")
object3.display_info()

class DEVICE:
 
    def __init__(self, device_name: str, device_type: str, brand: str, storage: int):
        self.device_name = device_name
        self.device_type = device_type
        self.brand = brand
        self.__storage = storage
        self.__APPS_LIST = []

    def ADD_APP(self, app: APPS):
        """Adds an app to the device."""
        self.__APPS_LIST.append(app)

    def REMOVE_APP(self, name: str):
        
        self.__APPS_LIST = [app for app in self.__APPS_LIST if app.name != name]

    def DISPLAY_DEVICE_DETAILS(self):
    
        print(f"Device Name: {self.device_name}")
        print(f"Device Type: {self.device_type}")
        print(f"Brand: {self.brand}")
        print(f"Storage: {self.__storage} GB")
        print(f"Total Apps: {len(self.__APPS_LIST)}")
        print()
        print("INSTALLED APPS:")

        for idx, app in enumerate(self.__APPS_LIST, 1):
            print(f"{idx}. {app.name} by {app.developer}")

Yes. If your DEVICE class needs exactly 4 attributes (states) and 3 functions (methods), you can make it simpler while keeping your original APPS class.

DEVICE class
class DEVICE:

 def __init__(self, deviceName, deviceType, brand, storage):
  self.deviceName = deviceName
  self.deviceType = deviceType
  self.brand = brand
  self.__storage = storage
  self.__apps = []

 def add_app(self, app):
  self.__apps.append(app)
  print(app.name, "has been added to", self.deviceName)

 def remove_app(self, app):
  if app in self.__apps:
   self.__apps.remove(app)
   print(app.name, "has been removed from", self.deviceName)
  else:
   print(app.name, "is not installed.")

 def display_info(self):
  print("Device Name:", self.deviceName)
  print("Device Type:", self.deviceType)
  print("Brand:", self.brand)
  print("Storage:", self.__storage)
  print("Number of Apps:", len(self.__apps))
4 Attributes / States
deviceName — name of the device
deviceType — type of device, such as smartphone or tablet
brand — brand of the device
__storage — storage capacity of the device (private attribute)
3 Functions / Methods
add_app() — adds an app to the device
remove_app() — removes an app from the device
display_info() — displays the device's information
Creating the DEVICE object
device1 = DEVICE("My Phone", "Smartphone", "Samsung", "128GB")

device1.add_app(object1)
device1.add_app(object2)

device1.display_info()

device1.remove_app(object2)

Note: __apps is also an attribute used internally to represent the relationship with APPS. If your teacher counts every attribute in the code, then the class technically has 5 attributes. If they require exactly 4 total attributes including the app relationship, we can instead make apps one of the four.

like this type but different concept class SONGS:
    def __init__(self, title, song_artist, duration, playlistName, total_Listening_time):
        self.title = title
        self.song_artist = song_artist
        self.duration = duration
        self.__total_Listening_time = total_Listening_time
        self.__playlistName = playlistName

    def calculate_total_listening_time(self):
        self.__total_Listening_time += self.duration * 60
        return self.__total_Listening_time

    def calculateTotalListeningTime(self):
        return self.calculate_total_listening_time()

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Artist: {self.song_artist}")
        print(f"Duration: {self.duration} minutes")
        print(f"Total Listening Time: {self.__total_Listening_time} seconds")
        print(f"Playlist: {self.__playlistName}")

    def displaySongDetails(self):
        self.display_details()

    def change_playlist_name(self, new_playlist_name: str):
        self.__playlistName = new_playlist_name
        print(f"Playlist name changed to: {self.__playlistName}")

    def changePlaylistName(self, new_playlist_name: str):
        self.change_playlist_name(new_playlist_name)

    def playSong(self):
        playsong(self)

    def pauseSong(self):
        pauseSong(self)


songs = SONGS

def calculateTotalListeningTime(song: SONGS):
    return song.calculate_total_listening_time()

def displaySongDetails(song: SONGS):
    song.display_details()

def changePlaylistName(song: SONGS, new_playlist_name: str):
    song.change_playlist_name(new_playlist_name)

def playsong(song: SONGS):
    print(f"Now playing: {song.title} by {song.song_artist}")

def pauseSong(song: SONGS):
    print(f"Paused: {song.title} by {song.song_artist}")

#Objects
object1 = SONGS("Merry Christmas, Please Don't Call", "Bleachers", 3.21, "Christmas", 192.6)
object2 = SONGS("Merry Christmas, i miss you", "Alex Crichton", 4.06, "Christmas", 243.6)
object3 = SONGS("Thinking of You", "Katy Perry", 4.06, "Pop", 243.6)
object4 = SONGS("La La Lost You", "NIKI", 3.20, "Indie", 192.0)
object5 = SONGS("All I Need To Hear", "The 1975", 3.30, "Alternative", 198.0)

#Implementing Methods
print("SONGS")

calculateTotalListeningTime(object1)
print("--BEFORE--")
displaySongDetails(object1)
print()
displaySongDetails(object2)
print()

changePlaylistName(object1, "Holiday Hits")

print("--AFTER--")
displaySongDetails(object1)
print()
displaySongDetails(object2)
print()

playsong(object3)
print()
pauseSong(object3)

class ALBUM:
    def __init__(self, album_title: str, album_artist: str, release_year: int):
        self.ALBUM_TITLE = album_title
        self.ALBUM_ARTIST = album_artist
        self.RELEASE_YEAR = release_year
        self.__SONGS_LIST = []

    def ADD_SONG(self, song: SONGS):
        """Adds a song to the album list."""
        self.__SONGS_LIST.append(song)

    def REMOVE_SONG(self, title: str):
        """Removes a song from the album list by title."""
        self.__SONGS_LIST = [song for song in self.__SONGS_LIST if song.title != title]

    def DISPLAY_ALBUM_DETAILS(self):
        """Displays the details of the album and its songs."""
        print(f"Album Title: {self.ALBUM_TITLE}")
        print(f"Artist: {self.ALBUM_ARTIST}")
        print(f"Release Year: {self.RELEASE_YEAR}")
        print(f"Total Tracks: {len(self.__SONGS_LIST)}")
        print()
        print("TRACKLIST:")
        for idx, song in enumerate(self.__SONGS_LIST, 1):
            print(f"{idx}. {song.title} by {song.song_artist} - {song.duration} minutes")

    def CALCULATE_TOTAL_DURATION(self) -> float:
        print()
        """Calculates the total duration of all songs in the album."""
        total_duration = sum(song.duration for song in self.__SONGS_LIST)
        return total_duration

def playsong(song: SONGS):
    print(f"Now playing: {song.title} by {song.song_artist}")

def pauseSong(song: SONGS):
    print(f"Paused: {song.title} by {song.song_artist}")

#OBJECTS

album1 = ALBUM("Nicole", "NIKI", 2022)

song1 = SONGS("La La Lost You", "NIKI", 3.20, "Indie", 192.0)
song2 = SONGS("I Like U", "NIKI", 4.23, "Pop", 263.0)
song3 = SONGS("Take A Chance With Me", "NIKI", 5.03, "Indie", 303.0)
song4 = SONGS("Newsflash", "NIKI", 3.34, "R&B", 214.0)
song5 = SONGS("Paths", "NIKI", 3.45, "Acoustic", 225.0)
song6 = SONGS("The Apartment We Won't Share", "NIKI", 2.29, "Indie", 149.0)

#TEST RUN

print("---BEFORE RELATIONSHIP---")
print(f"Album created: {album1.ALBUM_TITLE} by {album1.ALBUM_ARTIST}")
print("Songs created independently:")
print(f"  - {song1.title}")
print(f"  - {song2.title}")
print(f"  - {song3.title}")
print(f"  - {song4.title}")
print(f"  - {song5.title}")
print(f"  - {song6.title}")

print()

print("---BUILDING RELATIONSHIP---")
print(f"Adding songs to album: {album1.ALBUM_TITLE}")
album1.ADD_SONG(song1)
album1.ADD_SONG(song2)
album1.ADD_SONG(song3)
album1.ADD_SONG(song4)
album1.ADD_SONG(song5)
album1.ADD_SONG(song6)
print("Relationship established. Songs are now part of the album.")

print()

print("---AFTER RELATIONSHIP---")
print(f"Accessing song details through album: {album1.ALBUM_TITLE}")

album1.DISPLAY_ALBUM_DETAILS()
print()

print(f"Total Duration of Album: {album1.CALCULATE_TOTAL_DURATION():.2f} minutes")

print()

Yes, I understand. You want the DEVICE class to follow the same style as your ALBUM class: 4 attributes/states, 3 functions/methods, with a private list that creates the relationship with APPS.

You can use this:

class DEVICE:
    def __init__(self, device_name: str, device_type: str, brand: str, storage: int):
        self.device_name = device_name
        self.device_type = device_type
        self.brand = brand
        self.__storage = storage
        self.__APPS_LIST = []

    def ADD_APP(self, app: APPS):
        """Adds an app to the device."""
        self.__APPS_LIST.append(app)

    def REMOVE_APP(self, name: str):
        """Removes an app from the device by name."""
        self.__APPS_LIST = [
            app for app in self.__APPS_LIST
            if app.name != name
        ]

    def DISPLAY_DEVICE_DETAILS(self):
        """Displays the details of the device and its apps."""
        print(f"Device Name: {self.device_name}")
        print(f"Device Type: {self.device_type}")
        print(f"Brand: {self.brand}")
        print(f"Storage: {self.__storage} GB")
        print(f"Total Apps: {len(self.__APPS_LIST)}")
        print()
        print("INSTALLED APPS:")

        for idx, app in enumerate(self.__APPS_LIST, 1):
            print(f"{idx}. {app.name} by {app.developer}")

# OBJECTS
device1 = DEVICE("My Phone", "Smartphone", "Samsung", 128)

app1 = APPS("Among Us", "Innersloth", 4.99, True, "Light mode", "Player467")
app2 = APPS("Minecraft", "Mojang", 6.99, True, "Dark Mode", "Gamergirl1123")
app3 = APPS("Tiktok", "Zhang Yiming", 0, True, "Dark Mode", "Starrynights11")

# TEST RUN

print("--- BEFORE RELATIONSHIP ---")
print(f"Device created: {device1.device_name}")
print(f"Type: {device1.device_type}")
print(f"Brand: {device1.brand}")
print("Apps created independently:")
print(f"  - {app1.name}")
print(f"  - {app2.name}")
print(f"  - {app3.name}")

print()
print("--- BUILDING RELATIONSHIP ---")
print(f"Adding apps to device: {device1.device_name}")

device1.ADD_APP(app1)
device1.ADD_APP(app2)
device1.ADD_APP(app3)

print("Relationship established. Apps are now connected to the device.")
print()

print("--- AFTER RELATIONSHIP ---")
print(f"Accessing app details through: {device1.device_name}")

device1.DISPLAY_DEVICE_DETAILS()
print()

print("--- REMOVING APP ---")
device1.REMOVE_APP("Tiktok")
print()

print("--- AFTER REMOVING APP ---")
device1.DISPLAY_DEVICE_DETAILS()

print()

