import cv2
from keras.models import load_model
import numpy as np
import random
import time


class Game:

    def __init__(self,input_value):
        self.input_value=['Rock','Paper','Scissors']
        self.computer_score = 0
        self.user_score = 0

    def get_computer_choice(self) :
        self.computer_choice = random.choice(self.input_value)
        return self.computer_choice
    
    def get_prediction(self) :
        model = load_model('keras_model.h5')
        self.cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        data_dictionary = {0:"Rock", 1:"Paper", 2:"Scissors", 3:"Nothing"}
        end_time = time.time() + 5

        while True: 
            ret, frame = self.cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)
            cv2.imshow('frame', frame)
            # Press q to close the window
            print(max(prediction[0]))
            ind_predict=prediction[0].argmax()
            self.manual_input=data_dictionary[ind_predict]
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        return self.manual_input

    def get_human_choice(self):    
        self.human_choice = self.get_prediction()
        return self.human_choice
        pass
    
    def get_winner(self) :
        self.computer_choice = self.get_computer_choice()
        self.human_choice = self.get_human_choice()
        if self.human_choice == self.computer_choice:
            print("It's a tie!")

        elif (self.human_choice == 'Rock' and self.computer_choice == 'Paper') or \
             (self.human_choice == 'Scissors' and self.computer_choice == 'Rock') or \
             (self.human_choice == 'Paper' and self.computer_choice == 'Scissors' ):
                self.computer_score += 1
                print("The computer wins!")
        else:
            self.user_score += 1
            print("You win!")

       

    def play(self):
        
        while self.computer_score < 3 or self.user_score < 3:
            self.get_winner()

        if self.computer_score == 3:
            print(f'Computer wins! with {self.computer_score} to {self.user_score}')
        elif self.user_score == 3:
            print(f'User wins! with {self.user_score} to {self.computer_score}')
        else:
            print(f'The score is {self.computer_score} and the user_score    is {self.user_score}')

            #After the loop release the cap object
        self.cap.release()
                    # Destroy all the windows
        cv2.destroyAllWindows()



rps = Game(['Rock','Paper','Scissors','Nothing'])
rps.play()
