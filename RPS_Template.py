import cv2
from keras.models import load_model
import numpy as np
import random
import time


class Game:

    def __init__(self):
        self.input_value=['Rock','Paper','Scissors','Nothing']          
        self.computer_score = 0
        self.user_score = 0
        self.model = load_model('keras_model.h5')
        self.cap = cv2.VideoCapture(0)      
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)                                

    def get_computer_choice(self) :
        self.computer_choice = random.choice(self.input_value[0:3])
        return self.computer_choice
    
    def get_prediction(self) :
        data_dictionary = {0:"Rock", 1:"Paper", 2:"Scissors", 3:"Nothing"}
        end_time = time.time() + 5

        while time.time() < end_time: 
            ret, frame = self.cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 
            self.data[0] = normalized_image
            prediction = self.model.predict(self.data)
            cv2.imshow('frame', frame)
            print(max(prediction[0]))
            ind_predict=np.argmax(prediction[0])
            self.manual_input=data_dictionary[ind_predict]
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        return self.manual_input

    def countdown(self):
            max = 5
            start = time.time()
            while max > 0:
                
                cv2.waitKey(1000)
                max -= 1
            print("Start the game ")
            self.get_winner()

    def get_human_choice(self):    
        self.human_choice = self.get_prediction()
        return self.human_choice
    
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

def play():
    rps = Game ()
    while  rps.computer_score < 4  or rps.user_score  < 4:
        rps.countdown()
        ret, frame = rps.cap.read()                                   
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1   
        rps.data[0] = normalized_image
        cv2.imshow('frame', frame)

        if rps.computer_score == 3:
            print(f'Computer wins! with: {rps.computer_score} to User score : {rps.user_score}')
            exit()
        elif rps.user_score == 3:
            print(f'User wins! with: {rps.user_score} to computer score: {rps.computer_score}')
            exit()
        else:
            print(f'The computer score is: {rps.computer_score} and the user_score is: {rps.user_score}')

            if cv2.waitKey(2) & 0xFF == ord('q'):        
            
                break 
            
        
    rps.cap.release()
    cv2.destroyAllWindows()
    
play()





