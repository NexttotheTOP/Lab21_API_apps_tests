import ai21

ai21.api_key = '4dQi4MQDfnINYIthRMZc1ieFwuABrBCP'

prompt = 'how was Last day was in school ? '

response = ai21.Completion.execute(
    model='j1-large',
    prompt=prompt,
    temperature=0.65,
    minTokens=4,
    maxTokens=32,
    numResults=1
)