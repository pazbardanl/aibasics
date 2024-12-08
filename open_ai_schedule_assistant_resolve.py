from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant for managing meetings and schedules. When the user provides a time range, you should check the availability based on the scheduled events and propose a solution. If there is a conflict, suggest alternative times. in your response, avoid recapping the user's schedule for that day or what they've asked, just provide the answer or recommendation. also, avoid asking follow up questions at the end such as 'would you require any further assistance?'"},
        {
            "role": "user",
            "content": "{\"intention\": \"check availability\", \"date\": \"2024-12-10\", \"time_range\": \"09:00-11:00\", \"duration_hrs\": \"2\", \"scheduled_meetings\": [{\"start\": \"2024-12-10T09:00:00-05:00\", \"end\": \"2024-12-10T10:00:00-05:00\"}, {\"start\": \"2024-12-10T12:30:00-05:00\", \"end\": \"2024-12-10T13:30:00-05:00\"}]}"
        }
    ]
)

print(completion.choices[0].message)