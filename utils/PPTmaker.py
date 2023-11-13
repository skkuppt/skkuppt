import openai



def gpt_pptmaker(topic, details, apikey):
    openai.api_key = apikey

    # maximum PPt length (token issue)
    MAX_PPT_LENGTH = 1000
    # prompt
    prompt = f"""
    make a powerpoint presentation about {topic} with the following details:
    {details}    
    """

    # get response from GPT-3.5 using the prompt
    response = openai.ChatCompletion.create(
        engine="text-davinci-003",
        messeges=[prompt],
        max_tokens=MAX_PPT_LENGTH,
        n=1
    )
    print(response.choices[0].text)
    return response.choices[0].text



if __name__ == '__main__':
    topic = "What is the meaning of life?"
    details = "The meaning of life is to be happy and useful."
    apikey = "YOUR_API_KEY"
    gpt_pptmaker(topic, details, apikey)
    