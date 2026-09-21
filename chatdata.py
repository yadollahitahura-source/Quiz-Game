import json

class ChatAnalyzer:
    def __init__(self, file_name):
        self.file_name = file_name
        self.messages = None

    def load_data(self):
        with open(self.file_name, "r", encoding="utf-8") as file:
            self.messages = json.load(file)
        return self.messages

    def total_messages(self):
        return len(self.messages)

    def messages_by_person(self):
        people = {}

        for item in self.messages:
            name = item["from"]

            if name not in people:
                people[name] = 0

            people[name] += 1

        return people

    def percentage_by_person(self, message_counts):
        result = {}
        total = self.total_messages()

        for name, count in message_counts.items():
            percent = (count / total) * 100
            result[name] = round(percent, 1)

        return result

    def busiest_hour(self):
        hours = {}

        for item in self.messages:
            hour = item["time"].split(":")[0]

            if hour not in hours:
                hours[hour] = 0

            hours[hour] += 1

        busiest = max(hours, key=hours.get)

        return busiest, hours[busiest]

    def average_message_length(self):
        total_characters = {}
        message_counts = self.messages_by_person()

        for item in self.messages:
            name = item["from"]

            if name not in total_characters:
                total_characters[name] = 0

            total_characters[name] += len(item["text"])

        averages = {}

        for name in total_characters:
            averages[name] = round(
                total_characters[name] / message_counts[name], 1
            )

        return averages


file_name = "chat.json"

chat = ChatAnalyzer(file_name)

chat.load_data()

counts = chat.messages_by_person()
percentages = chat.percentage_by_person(counts)
busy_hour, busy_count = chat.busiest_hour()
averages = chat.average_message_length()

print("تعداد پیام‌های هر نفر:")
print(counts)

print("\nدرصد پیام‌های هر نفر:")
print(percentages)

print("\nشلوغ‌ترین ساعت:")
print(busy_hour + ":00")
print("تعداد پیام‌ها:", busy_count)

print("\nمیانگین طول پیام هر نفر:")
print(averages)