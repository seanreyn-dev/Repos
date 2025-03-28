import sys
from typing import List, Optional
from datetime import datetime, timedelta

class Time:
    """Does time conversions for different timezones"""
    def __init__(self, zoneId: str, zoneOffset: int):
        self.zoneId = zoneId
        self.zoneOffset = zoneOffset

    def computeTime(self, dateTime: datetime, targetOffset: int) -> datetime:
        return dateTime + timedelta(hours=(targetOffset - self.zoneOffset))

class Theme:
    """Holds the theme settings for the app"""
    def __init__(self, name: str, colorScheme: str, fontStyle: str):
        self.name = name
        self.colorScheme = colorScheme
        self.fontStyle = fontStyle

class Settings:
    """General app settings stored"""
    def __init__(self, timeZone: Time, theme: Theme):
        self.timeZone = timeZone
        self.theme = theme

    def updateTimeZone(self, newTimeZone: Time):
        self.timeZone = newTimeZone

    def updateTheme(self, newTheme: Theme):
        self.theme = newTheme

class User:
    """Represents user and owned or shared calendars"""
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.calendars: List["Calendar"] = []
        self.sharedCalendars: List["Calendar"] = []

    def addCalendar(self, calendar: "Calendar"):
        if calendar not in self.calendars:
            self.calendars.append(calendar)

    def getCalendar(self, name: str) -> Optional["Calendar"]:
        for cal in self.calendars + self.sharedCalendars:
            if cal.calendarName.lower() == name.lower():
                return cal
        return None

class Event:
    """Defines events and their details"""
    def __init__(self, id: str, name: str, description: str, startTime: datetime, endTime: datetime):
        if startTime >= endTime:
            raise ValueError("Start time must be before end time, retry")
        self.id = id
        self.name = name
        self.description = description
        self.startTime = startTime
        self.endTime = endTime
        self.shared_with: List[User] = []

class Calendar:
    """Calendars hold events, stored for user"""
    def __init__(self, calendarName: str, owner: User):
        self.calendarName = calendarName
        self.events: List[Event] = []
        self.owner = owner

    def addEvent(self, event: Event):
        self.events.append(event)

    def removeEventByName(self, eventName: str) -> bool:
        for i, ev in enumerate(self.events):
            if ev.name.lower() == eventName.lower():
                del self.events[i]
                return True
        return False

class CalendarApp:
    """Manages user and app settings"""
    def __init__(self):
        self.users: List[User] = []
        self.settings = Settings(Time("UTC", 0), Theme("Default", "Light", "Sans"))

    def selectUser(self, username: str) -> Optional[User]:
        return next((u for u in self.users if u.username == username), None)

    def addUser(self, user: User):
        self.users.append(user)

class CalendarCLI:
    """Command-line interface for calendar placeholder UI/GUIX"""
    def __init__(self):
        self.app = CalendarApp()

    def menu(self):
        while True:
            print("\nCalendar App")
            print("1. Create User")
            print("2. Add Calendar")
            print("3. Add Event")
            print("4. Share Event")
            print("5. View Events")
            print("6. Update Timezone")
            print("7. Update Theme")
            print("8. Remove Event")
            print("9. Exit")

            choice = input("Choose an option: ").strip()
            self.handleChoice(choice)

    def handleChoice(self, choice):
        if choice == "1":
            self.addUser()
        elif choice == "2":
            self.addCalendar()
        elif choice == "3":
            self.addEvent()
        elif choice == "4":
            self.shareEvent()
        elif choice == "5":
            self.visualizeEvents()
        elif choice == "6":
            self.updateTimeZone()
        elif choice == "7":
            self.updateTheme()
        elif choice == "8":
            self.removeEvent()
        elif choice == "9":
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid choice, please try again with a proper number 1-9")

    def addUser(self):
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        self.app.addUser(User(username, password))
        print(f"User '{username}' created.")

    def addCalendar(self):
        username = input("Your username: ").strip()
        user = self.app.selectUser(username)
        if not user:
            print("User not found. Try again or create a new user.")
            return
        name = input("Calendar name: ").strip()
        calendar = Calendar(name, user)
        user.addCalendar(calendar)
        print(f"Calendar '{name}' added.")

    def addEvent(self):
        username = input("Your username: ").strip()
        user = self.app.selectUser(username)
        if not user:
            print("User not found.")
            return
        calendarName = input("Calendar name: ").strip()
        calendar = user.getCalendar(calendarName)
        if not calendar:
            print("Calendar doesn't exist.")
            return
        eventName = input("Event name: ").strip()
        description = input("Event details: ").strip()
        try:
            startTime = datetime.strptime(input("Start (Format:YYYY-MM-DD HH:MM) Make sure format matches exactly: "), "%Y-%m-%d %H:%M")
            endTime = datetime.strptime(input("End (Format:YYYY-MM-DD HH:MM) Make sure format matches exactly: "), "%Y-%m-%d %H:%M")
        except ValueError:
            print("Invalid date format.")
            return
        eventId = f"E{len(calendar.events) + 1}"
        calendar.addEvent(Event(eventId, eventName, description, startTime, endTime))
        print(f"Event '{eventName}' created and added!")

    def shareEvent(self):
        username = input("Your username: ").strip()
        user = self.app.selectUser(username)
        if not user:
            print("User not found.")
            return
        calendarName = input("Calendar name: ").strip()
        calendar = user.getCalendar(calendarName)
        if not calendar:
            print("Calendar doesn't exist.")
            return
        eventName = input("Event name to share: ").strip()
        targetUsername = input("User to share with: ").strip()
        targetUser = self.app.selectUser(targetUsername)
        if not targetUser:
            print("User not found.")
            return
        event = next((ev for ev in calendar.events if ev.name.lower() == eventName.lower()), None)
        if event:
            if targetUser not in event.shared_with:
                event.shared_with.append(targetUser)
            print(f"Event '{event.name}' shared with {targetUser.username}.")
        else:
            print("Event doesn't exist.")

    def visualizeEvents(self):
        username = input("Your username: ").strip()
        user = self.app.selectUser(username)
        if not user:
            print("User not found.")
            return
        calendarName = input("Calendar name: ").strip()
        calendar = user.getCalendar(calendarName)
        if not calendar:
            print("Calendar doesn't exist.")
            return
        print(f"Events in '{calendar.calendarName}':")
        for ev in calendar.events:
            print(f"- {ev.name}: {ev.startTime} to {ev.endTime}")

    def updateTimeZone(self):
        new_zoneId = input("Enter new timezone name: ").strip()
        try:
            new_zoneOffset = int(input("Enter new timezone offset (in hours): ").strip())
        except ValueError:
            print("Enter a normal integer please.")
            return
        old_offset = self.app.settings.timeZone.zoneOffset
        diff = new_zoneOffset - old_offset
        for u in self.app.users:
            for cal in u.calendars:
                for ev in cal.events:
                    ev.startTime += timedelta(hours=diff)
                    ev.endTime += timedelta(hours=diff)
            for cal in u.sharedCalendars:
                for ev in cal.events:
                    ev.startTime += timedelta(hours=diff)
                    ev.endTime += timedelta(hours=diff)
        self.app.settings.updateTimeZone(Time(new_zoneId, new_zoneOffset))
        print(f"Timezone changed to {new_zoneId} (offset: {new_zoneOffset}). All event times updated.")

    def updateTheme(self):
        themeName = input("Enter theme name: ").strip()
        colorScheme = input("Enter color scheme: ").strip()
        fontStyle = input("Enter font style: ").strip()
        self.app.settings.updateTheme(Theme(themeName, colorScheme, fontStyle))
        print(f"Theme changed to '{themeName}' with color '{colorScheme}' and font '{fontStyle}'.")

    def removeEvent(self):
        username = input("Your username: ").strip()
        user = self.app.selectUser(username)
        if not user:
            print("User not found.")
            return
        calendarName = input("Calendar name: ").strip()
        calendar = user.getCalendar(calendarName)
        if not calendar:
            print("Calendar not found.")
            return
        eventName = input("Enter the Event NAme to remove: ").strip()
        if calendar.removeEventByName(eventName):
            print(f"Event '{eventName}' removed.")
        else:
            print("Event not found.")

if __name__ == "__main__":
    CalendarCLI().menu()
