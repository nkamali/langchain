import argparse
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

def main(text):
    llm = OpenAI()
    chat_model = ChatOpenAI()

    llm_prediction = llm.predict(text)
    chat_model_prediction = chat_model.predict(text)

    print("Prediction from llm.predict:", llm_prediction)
    print("Prediction from chat_model.predict:", chat_model_prediction)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Make predictions using OpenAI and ChatOpenAI models.')
    parser.add_argument('--text', type=str, help='The input text for prediction')

    args = parser.parse_args()

    # main(text)
    main(args.text)
