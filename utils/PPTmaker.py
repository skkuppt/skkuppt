from openai import OpenAI


def gpt_pptmaker(topic, details, apikey):
    client = OpenAI(
        api_key=apikey,
    )

    # prompt
    prompt = f"""
    make a powerpoint presentation about {topic} with the following details:
    {details}
    In the structure of:
    Slide 1:
    Title:
    Content:
    Slide 2:
    Title:
    Content:
    ...  
    Slide n:
    Title:
    Content:
    Only write the title of the slides and its content. 
    """

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are making ppt for the class, skilled in making index and its belongings.\
              showing only the title and content of the slides without other flowery words or summary."},
            {"role": "user", "content": prompt}
        ],
    )

    # get the response content only
    print(completion.choices[0].message.content)
    slides = completion.choices[0].message.content.split("Slide")
    slides = slides[1:]

    slides = ["Slide" + slide.strip() for slide in slides]
    return slides



if __name__ == '__main__':
    topic = "What is the meaning of life?"
    details = "The meaning of life is to be happy and useful."
    apikey = ""
    print(gpt_pptmaker(topic, details, apikey))
    