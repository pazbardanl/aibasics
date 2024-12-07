from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are an assistant that parses user requests for calendar availability. For each user query, extract the intention (e.g., 'check_availability', 'propose_slots'), the date, time, any relevant time ranges and optinally the slot duration (if input mentions it). Provide the output as JSON. Examples: Input: \"Am I available next Monday at 3 PM?\" Output: {\"intention\": \"check_availability\", \"date\": \"2024-12-11\", \"time\": \"15:00\"} Input: \"Can you suggest a slot of 90 minutes for Tuesday morning?\" Output: {\"intention\": \"propose_slots\", \"date\": \"2024-12-10\", \"time_range\": \"8:00-12:00\, \"duration_hrs\": \"1.5\"}. early morning is 5am till 8am, morning is 8am till 12pm, noon is 12p, till 4pm, afternoon is 4pm till 6pm, evening is 6pm till 10pm, night is 10pm till 5am. offset your dates considering 2024-12-07 is a Satureday"},
        {
            "role": "user",
            "content": "am I available for a late dinner in a week from today?"
        }
    ]
)

print(completion.choices[0].message)