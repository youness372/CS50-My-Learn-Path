## $${\color{blue}Welcome \space } $$     

* Artificial intelligence (AI) is providing new advancements and excitement in computer science and the wide world!
* While AI provides huge advancements, sometimes eliminating the human bottlenecks that can slow down processes, being able to understand, create, and organize code allows you to be a driver, a pilot, an empowered creator through programming.
* Therefore, rather than thinking about AI as a way to remove the need to learn the fundamentals, consider how you knowing the fundamentals and being further empowered by AI will lead to whole new opportunities for you and those you serve.

##  $${\color{blue} Visual  \space  Studio  \space  Code  \space  and  \space  chat.py}$$   

* VS Code is an IDE or integrated development environment, where one can create code.
* To give you taste of what is to come, we could program our own chatbot called chat.py.
* On a system already configured for using OpenAI’s libraries, we could program as follows.
* In the text editor, one could type in the following code:

```py 
from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    input="In one sentence, what is CS50?",
    model="gpt-5"
)

print(response.output_text)
```

<img width="1449" height="514" alt="image" src="https://github.com/user-attachments/assets/4af9195b-1fea-4d51-b740-eb83a4f0a5ea" />


### *We could improve upon this code by allowing the user to ask a question. Modify your code as follow:*

```py 
from openai import OpenAI

client = OpenAI()

prompt = input("Prompt: ")

response = client.responses.create(
    input=prompt,
    model="gpt-5"
)

print(response.output_text)
```

Notice that prompt is now created, allowing the user to ask a question.

### *Even more, this program can be improved by providing a system_prompt to provide some further context and instructions to the chatbot:*   
```py 
from openai import OpenAI

client = OpenAI()

user_prompt = input("Prompt: ")
system_prompt = "Limit your answer to one sentence. Pretend you're a cat."

response = client.responses.create(
    input=user_prompt,
    instructions=system_prompt,
    model="gpt-5"
)

print(response.output_text)
```
Notice how system_prompt is used to provide further context and instructions.

* With programming, you have the ability in ten lines of text to build very powerful programs!
* We have created our own rubber duck, the CS50 Duck, to get help in your work in this course.
* Keep in mind our Academic Honesty Policy, which prohibits the use of any AI tool besides the CS50 Duck.
