import ai21
ai21.api_key = '4dQi4MQDfnINYIthRMZc1ieFwuABrBCP'

ai21.Completion.execute(
  model="j2-ultra",
  prompt="Review:"
Extremely old cabinets, phone was half broken and full of dust. Bathroom door was broken, bathroom floor was dirty and yellow. Bathroom tiles were falling off. Asked to change my room and the next room was in the same conditions.
The most out of date and least maintained hotel i ever been on.
Extracted sentiment:
{“Cleaning”: “Negative”, “Hotel Facilities”: “Negative”, “Room Quality”: “Negative”}
##
Review:
Great experience for two teenagers. We would book again. Location good.
Extracted sentiment:
{“Location”: “Positive”}
##
Review:
Pool area was definitely a little run down and did not look like the pics online at all. Bathroom in the double room was kind of dumpy.
Extracted sentiment:
{“Pool”: “Negative”, “Room Quality”: “Negative”}
##
Review:
Roof top’s view is gorgeous and the lounge area is comfortable. The staff is very courteous and the location is great. The hotel is outdated and the shower need to be clean better. The air condition runs all the time and cannot be control by the temperature control setting.
Extracted sentiment:
{“Cleaning”: “Negative”, “AC”: “Negative”, “Room Quality”: “Negative”, “Service”: “Positive”, “View”: “Positive”, “Hotel Facilities”: “Positive”}
##
Review:
First I was placed near the elevator where it was noises, the TV is not updated, the toilet was coming on and off. There was no temp control and my shower curtain smelled moldy. Not sure what happened to this place but only thing was a great location.
Extracted sentiment:
{“Cleaning”: “Negative”, “AC”: “Negative”, “Room Quality”: “Negative”, “Location”: “Positive”}
##
Review:
This is a very well located hotel and it’s nice and clean. Would stay here again.
Extracted sentiment:
{“Cleaning”: “Positive”, “Location”: “Positive”}
##
Review:
Hotel is horrendous. The room was dark and dirty. No toilet paper in the bathroom. Came here on a work trip and had zero access to WiFi even though their hotel claims to have WiFi service. I will NEVER return.
Extracted sentiment:
{“Cleaning”: “Negative”, “WiFi”: “Negative”, “Room Quality”: “Negative”, “Service”: “Negative”}
##
Review:
The rooms are small but clean and comfortable. The front desk was really busy and the lines for check-in were very long but the staff handled each person in a professional and very pleasant way. We will stay there again.
Extracted sentiment:
{“Cleaning”: “Positive”, “Service”: “Positive”}
##
Review:
The stay was very nice would stay again. The pool closes at 7 pm and doesn’t open till 11am m. That sucked. Also our wifi went out the entire last day we were there. Thats sucked too. Overall was a nice enough stay and I love the location.
Extracted sentiment:
",
  numResults=1,
  maxTokens=50,
  temperature=0,
  topKReturn=0,
  topP=1,
  countPenalty={
    "scale": 0,
    "applyToNumbers": False,
    "applyToPunctuations": False,
    "applyToStopwords": False,
    "applyToWhitespaces": False,
    "applyToEmojis": False
  },
  frequencyPenalty={
      "scale": 0,
      "applyToNumbers": False,
      "applyToPunctuations": False,
      "applyToStopwords": False,
      "applyToWhitespaces": False,
      "applyToEmojis": False
  },
  presencePenalty={
      "scale": 0,
      "applyToNumbers": False,
      "applyToPunctuations": False,
      "applyToStopwords": False,
      "applyToWhitespaces": False,
      "applyToEmojis": False
  },
  stopSequences=["##"]
)