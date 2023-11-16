import openai
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
    Slide 2:
    ...  
    Slide n:  
    """

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {"role": "system", "content": "You are making ppt for the class, skilled in making index and its belongings."},
            {"role": "user", "content": prompt}
        ],

    )
    # get the response content only
    print(completion.choices[0].message)
    return completion.choices[0].message



if __name__ == '__main__':
    topic = "What is the meaning of life?"
    details = "The meaning of life is to be happy and useful."
    apikey = ""
    gpt_pptmaker(topic, details, apikey)
    