def simple_chatbot(user_input):
    user_input = user_input.lower()
    if any(word in user_input for word in ["hello", "hi", "hey", "greetings"]):
        return "Hi there!" # Respond with a greeting
    elif "how are you" in user_input:
        return "I'm doing well, thanks for asking!" # Respond to "how are you"
    elif any(word in user_input for word in ["bye", "goodbye", "see you"]):
        return "Good Bye" # Respond to farewells
    elif any(word in user_input for word in ["thank you", "thanks"]):
        return "You're welcome!" # Respond to thank you
    elif any(word in user_input for word in ["what's up", "how's it going"]):
        return "Not much, just a chatbot!" # Respond to casual greetings
    else:
        return "I don't understand that." # Default response

from ipywidgets import Text, Output, Button, VBox, HBox
from IPython.display import display


input_box = Text(placeholder='Enter your message:', layout={'width': '300px'})
submit_button = Button(description="Submit", layout={'width': 'auto'})
output_area = Output()


input_area = HBox([input_box, submit_button])

chat_interface = VBox([input_area, output_area])

display(chat_interface)


def handle_submit(button): # The function will be triggered by the button click
    user_message = input_box.value # Get the value directly from the input_box

    with output_area:
        print(f"You: {user_message}")
        chatbot_response = simple_chatbot(user_message) # Assuming simple_chatbot is defined in a previous cell
        print(f"Chatbot: {chatbot_response}")
    input_box.value = "" # Clear the input box after submission

# Link the button's click event to the handle_submit function
submit_button.on_click(handle_submit)

