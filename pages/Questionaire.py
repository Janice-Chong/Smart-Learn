import streamlit as st
import pandas as pd
import joblib


# Function to create a questionnaire page
def questionnaire():
    st.title("Which Learning Objects Suits Me Best?", anchor=False)
    st.write("Please answer the following questions. There are 2 parts. Part 1 consist of 3 questions on your peronal details while Part 2 consist of 30 questions which will determines your learning style based on the VAK learning style.")

    demographics_questions = {
        'Gender': ["Male", "Female"],
        'Level of Study': ['Postgraduate', 'Undergraduate', 'Certificate/Diploma'],
        'Household Income': ['Less than RM4,849', 'RM 4,850 – RM10,959', 'More than RM10,960']
    }
    
    vak_questions = {
        '1. When operating new equipment for the first time I prefer to': ['Read the instructions', 'Listen to or ask for an explaination', 
                                                                           'Have a go and learn by \"trial and error\"'],
        '2. When seeking travel directions I': ['Look at a map', 'Ask for spoken directions', 'Follow my nose or maybe use a compass'],
        '3. When cooking a new dish I': ['Follow a recipe', 'Call a friend for explaination', 'Follow my instinct, tasting as I cook'],
        '4. To teach someone something I': ['Write Instructions', 'Explain verbally', 'Demonstrate and let them have a go'],
        '5. I tend to say ': ['I see what you mean', 'I hear what you are saying', 'I know how you feel'],
        '6. I tend to say ': ['Show me', 'Tell me', 'Let me try'],
        '7. I tend to say ': ['Watch how I do it', 'Listen to me explain', 'You have a go'],
        '8. Complaining about faulty goods I tend to': ['Write a letter', 'Phone', 
                                                        'Go back to the store, or send the faulty item to the head office'],
        '9. I prefer these leisure activities': ['Museums or galleries', 'Music or conversation', 'Physical activities or making things'],
        '10. When shopping generally I tend to': ['Look and decide', 'Discuss with shop staff', 'Try on, handle or test'],
        '11. Choosing a holiday I': ['Read the brochures', 'Listen to recommendations', 'Imagine the experience'],
        '12. Choosing a new car I': ['Read the reviews', 'Discuss with friends', 'Test-drive what you fancy'],
        '13. Learning a new skill': ['I watch what the teacher is doing', 
                                     'I talk through with the teacher exactly what I am supposed to do', 
                                     'I like to give it a try and work it out as I go along by doing it'],
        '14. Choosing from a restaurant menu': ['I imagine what the food will look like', 'I talk through the options in my head', 
                                                'I imagine what  the food will taste like'],
        '15. When listening to a band': ['I sing along to the lyrics (in my head or out loud)', 
                                         'I listen to the lyrics and the beats', 'I move in time with the music'],
        '16. When concentrating I': ['Focus on the words or pictures in front of me', 
                                     'Discuss the problem and possible solutions in my head', 
                                     'Move around a lot, fiddle with pens and pencils and touch unrelated things'],
        '17. I remember things best by': ['Writing notes or keeping printed details', 
                                          'Saying them aloud or repeating words and key points in my head', 
                                          'Doing and practicing the activity or imagining it being done'],
        '18. My first memory is of': ['Looking at something', 'Being spoken to', 'Doing something'],
        '19. When anxious I': ['Visualize the worst case scenarios', 'Talk over in my head what worries me most', 
                               'Can\'t sit still, fiddle and move around constantly'],
        '20. I feel especially connected to others because of': ['How they look', 'What they say to me', 'How they make me'],
        '21. When I revise for an exam, I': ['Write lots of revision notes', 'I talk over my notes, to myself or to other people', 
                                             'Imagine making the movement or creating the formula'],
        '22. When explaining something to someone, I tend to': ['Show them what I mean', 
                                                                'Explain to them in different ways until they understand', 
                                                                'Encourage them to try and talk them through the idea as they try'],
        '23. My main interests are': ['Photography or watching films or people watching', 
                                      'Listening to music or listening to the radio or talking to friends', 
                                      'Physical/sports activities or fine wines, fine foods or dancing'],
        '24. Most of my free time is spent': ['Watching television', 'Talking to friends', 'Doing physical activity or making things'],
        '25. When I first contact a new person': ['I arrange a face to face meeting', 'I talk to them on the telephone', 
                                                  'I try to get together to share an activity'],
        '26. I first notice how people': ['Look and dress', 'Sound and speak', 'Stand and move'],
        '27. If I am very angry': ['I keep replaying in my mind what it is that has upset me', 'I shout lots and tell people how I feel', 
                                   'I stomp about, slam doors and throw things'],
        '28. I find it easiest to remember': ['Faces', 'Names', 'Things I have done'],
        '29. I think I can tell someone is lying because': ['They avoid looking at you', 'Their voice changes', 
                                                            'The vibes I get from them'],
        '30. When I\'m meeting with an old friend': ['I say \"it\'s great to see you!\"', 'I say "it\'s great to hear your voice!"', 
                                                     'I give them a hug or a handshake']
    }
    # Function to check if any question is unanswered
    def check_unanswered_questions():
        unanswered_questions = []
        for question in demographics_questions.keys():
            if question not in responses.keys() or not responses[question]:
                unanswered_questions.append(question)
    
        for question in vak_questions.keys():
            if question not in responses.keys() or not responses[question]:
                unanswered_questions.append(question)
    
        return unanswered_questions

    # User responses
    responses = {}

    st.subheader('Part 1: Personal Details', anchor=False)
    # Collect user responses
    for question, options in demographics_questions.items():
        response = st.radio(question, options, index=None) # No default selection
#         response = st.radio(question, options)
        responses[question] = response
    
    # Multiple selection question
    response = st.multiselect("Preferred learning mode", ["Face to Face", "Synchronous Online Learning (Real Time)",
                                                          "Asynchronous Online Learning (On your own time)"])
#     st.text('Select all options that apply. You can select more than 1 option')

    # Check if there's a response
    if not response:
        st.error("Please select at least one option for Preferred Learning Mode.")
    else:
        # Join the selected options if there's a response
        response_text = ', '.join(response)
        responses['Preferred learning mode'] = response_text
        
        st.subheader('Part 2: VAK Learning Style Test', anchor=False)
        
        # Collect user responses for each VAK question
        for question, options in vak_questions.items():
            response = st.radio(question, options, index=None) # No default selection
#             response = st.radio(question, options)
            responses[question] = response

        # Submit button to save responses
        if st.button("Submit"):
            # Check for unanswered questions
            unanswered = check_unanswered_questions()
            if unanswered:
                st.warning("Please answer the following questions: " + ', '.join(unanswered))
            else:

                # Save responses to a DataFrame
                df_responses = pd.DataFrame([responses])

                # Save responses to a CSV file
                df_responses.to_csv("user_responses.csv", index=False)
                # Mark that the CSV file already exists
                st.session_state.csv_exists = True

                st.success("Responses saved successfully!")

            # Append responses to the existing CSV file
            # df_responses.to_csv("all_user_responses.csv", mode="a", header=not st.session_state.get('csv_exists'), index=False)

                # Get the dominant VAK
                df_responses = dom_vak(df_responses, vak_questions)

#                 # For checking purpose only --> can remove afterwards
#                 df_responses.to_csv("user_responses_withdomVAK.csv", index=False)
#                 # Mark that the CSV file already exists
#                 st.session_state.csv_exists = True
#                 show_user_responses()
                
                st.subheader('Dominant VAK Learning Style', anchor=False)
                display_domVAK(df_responses)

                # Encode responses
                df_responses = encode_res(df_responses, demographics_questions, vak_questions)

                # Merge the data to the format that suit the model
                df_responses = final_df(df_responses)

                # Model
                st.subheader('Recommended Learning Objects', anchor=False)
                model_predict(df_responses)

#         # Append responses to an existing CSV file or create a new one
#         if not st.session_state.get('df_all_responses'):
#             st.session_state.df_all_responses = df_responses
            
#         else:
#             st.session_state.df_all_responses = st.session_state.df_all_responses.append(df_responses, ignore_index=True)

#         # Save all responses to a CSV file
#         st.write("Saving responses...")
#         st.session_state.df_all_responses.to_csv("all_user_responses.csv", index=False)
#         st.write("Responses saved successfully!")


# Function to load user responses for checking purpose only --> remove after finalised
def show_user_responses():
    st.title("User Responses", anchor=False)

#     # Load all user responses
#     df_all_responses = st.session_state.get('df_all_responses')

#     if df_all_responses is not None and not df_all_responses.empty:
#         st.write("All User Responses:")
#         st.write(df_all_responses)
#     else:
#         st.write("No responses recorded yet.")
        
    # Load user responses
    df_responses = pd.read_csv("user_responses_withdomVAK.csv")

    # Display user responses
    st.write("User Responses:")
    st.write(df_responses)
    
# Determine the dominant VAK
def dom_vak(df_responses, vak_questions):
    # Define answers options
    visual_keywords = ["Read the instructions", 
                   "Look at a map", 
                   "Follow a recipe", 
                   "Write Instructions",
                   "I see what you mean",
                   "Show me",
                   "Watch how I do it",
                   "Write a letter",
                   "Museums or galleries",
                   "Look and decide",
                   "Read the brochures",
                   "Read the reviews",
                   "I watch what the teacher is doing",
                   "I imagine what the food will look like",
                   "I sing along to the lyrics (in my head or out loud)",
                   "Focus on the words or pictures in front of me",
                   "Writing notes or keeping printed details",
                   "Looking at something",
                   "Visualize the worst case scenarios",
                   "How they look",
                   "Write lots of revision notes",
                   "Show them what I mean",
                   "Photography or watching films or people watching",
                   "Watching television",
                   "I arrange a face to face meeting",
                   "Look and dress",
                   "I keep replaying in my mind what it is that has upset me",
                   "Faces",
                   "They avoid looking at you",
                   "I say \"it's great to see you!\""
                      ]

    auditory_keywords = ["Listen to or ask for an explaination", 
                     "Ask for spoken directions", 
                     "Call a friend for explaination",
                     "Explain verbally",
                     "I hear what you are saying",
                     "Tell me",
                     "Listen to me explain",
                     "Phone",
                     "Music or conversation",
                     "Discuss with shop staff",
                     "Listen to recommendations",
                     "Discuss with friends",
                     "I talk through with the teacher exactly what I am supposed to do",
                     "I talk through the options in my head",
                     "I listen to the lyrics and the beats",
                     "Discuss the problem and possible solutions in my head",
                     "Saying them aloud or repeating words and key points in my head",
                     "Being spoken to",
                     "Talk over in my head what worries me most",
                     "What they say to me",
                     "I talk over my notes, to myself or to other people",
                     "Explain to them in different ways until they understand",
                     "Listening to music or listening to the radio or talking to friends",
                     "Talking to friends",
                     "I talk to them on the telephone",
                     "Sound and speak",
                     "I shout lots and tell people how I feel",
                     "Names",
                     "Their voice changes",
                     "I say \"it's great to hear your voice!\""
                    ]

    kinesthetic_keywords = ["Have a go and learn by \"trial and error\"", 
                        "Follow my nose or maybe use a compass", 
                        "Follow my instinct, tasting as I cook",
                        "Demonstrate and let them have a go",
                        "I know how you feel",
                        "Let me try",
                        "You have a go",
                        "Go back to the store, or send the faulty item to the head office",
                        "Physical activities or making things",
                        "Try on, handle or test",
                        "Imagine the experience",
                        "Test-drive what you fancy",
                        "I like to give it a try and work it out as I go along by doing it",
                        "I imagine what  the food will taste like", #double spacing here
                        "I move in time with the music",
                        "Move around a lot, fiddle with pens and pencils and touch unrelated things",
                        "Doing and practicing the activity or imagining it being done",
                        "Doing something",
                        "Can't sit still, fiddle and move around constantly",
                        "How they make me",
                        "Imagine making the movement or creating the formula",
                        "Encourage them to try and talk them through the idea as they try",
                        "Physical/sports activities or fine wines, fine foods or dancing",
                        "Doing physical activity or making things",
                        "I try to get together to share an activity",
                        "Stand and move",
                        "I stomp about, slam doors and throw things",
                        "Things I have done",
                        "The vibes I get from them",
                        "I give them a hug or a handshake" 
                           ]
    
    # Extract columns E to AH to access the VAK questions columns only
    responses_df = df_responses.iloc[:, 4:34]
    
    # Initialize a list to store the dominant VAK preferences for each respondent
    dominant_preferences = []

    # Iterate the rows (each row represents a respondent)
    for index, row in responses_df.iterrows():
        visual_count = 0
        auditory_count = 0
        kinesthetic_count = 0

        # Iterate the columns (each column is a question)
        for column in responses_df.columns:
            response = row[column].lower()
        
            # Compare keywords with the response
            # Count the number of visual/auditory/kinesthetic answers chosen
            for keyword in visual_keywords:
                if keyword.lower() in response:
                    visual_count += 1

            for keyword in auditory_keywords:
                if keyword.lower() in response:
                    auditory_count += 1

            for keyword in kinesthetic_keywords:
                if keyword.lower() in response:
                    kinesthetic_count += 1

        # Determine the dominant VAK preference for this respondent using the max count
        preferences = {
            "Visual": visual_count,
            "Auditory": auditory_count,
            "Kinesthetic": kinesthetic_count
        }

        dominant_preference = max(preferences, key=preferences.get)
        dominant_preferences.append(dominant_preference)

    
    # Add the list of dominant preferences as a new column in the DataFrame (df)
    df_responses['Dominant_VAK'] = dominant_preferences
    
    return df_responses
    
def display_domVAK(df_responses):
    dom_vak_lst = df_responses['Dominant_VAK'].tolist()
    for i in dom_vak_lst:
        st.write(i)
    
# Encoding responses    
def encode_res(df_responses, demographics_questions, vak_questions):
    # Splitting column by ', ' with multiple options
    df_responses['Preferred learning mode'] = df_responses['Preferred learning mode'].str.split(', ')

    # Exploding the columns to separate rows for each value
    df_responses = df_responses.explode('Preferred learning mode').reset_index(drop=True)
    
    # Define your custom mapping
    custom_mapping = {
        "Male": 1,
        "Female": 2,
        "Postgraduate": 1,
        "Undergraduate": 2,
        "Certificate/Diploma": 3,
        "Less than RM4,849": 1,
        "RM 4,850 – RM10,959": 2, 
        "More than RM10,960": 3
    }

    # Perform ordinal encoding using the defined mapping
    for question, option in demographics_questions.items():
        df_responses[question] = df_responses[question].map(custom_mapping)
        
    # Get the vak questions columns (column E to column AH)
    qcolumns_df = df_responses.iloc[:, 4:34]
    
    # Encode categorical variables (one-hot encoding)
    df_responses = pd.get_dummies(df_responses, columns=qcolumns_df.columns, prefix=qcolumns_df.columns)
    
    # Define your custom mapping
    custom_mapping = {
        "Visual": 1,
        "Auditory": 2,
        "Kinesthetic": 3
    }

    # Perform ordinal encoding using the defined mapping
    df_responses['Dominant_VAK'] = df_responses['Dominant_VAK'].map(custom_mapping)
    
    prefered_columns = ['Preferred learning mode']
    # Encode categorical variables (one-hot encoding)
    df_responses = pd.get_dummies(df_responses, columns=prefered_columns, prefix=prefered_columns)
    
    df_responses.to_csv("encoded_responses_withdomVAK.csv", index=False)
    # Mark that the CSV file already exists
    st.session_state.csv_exists = True
    
    return df_responses

# Dataframe that suit the model format
def final_df(df_responses):
    # Read an empty DataFrame with only column names (with the correct arrangement)
    empty_df = pd.read_csv('empty_df.csv')
    
    # Iterate over columns and fill in the data based on response df
    for col in df_responses.columns:
        if col in empty_df.columns:
            empty_df[col] = df_responses[col]
    
    # Replace NaN values with 'FALSE'
    merged_df = empty_df.fillna(False)
    
    merged_df.to_csv("merged_withdomVAK.csv", index=False)
    # Mark that the CSV file already exists
    st.session_state.csv_exists = True
    
    return merged_df

# Predictions
def model_predict(df_responses):
    svm_model = joblib.load("Model/svm_model_withQues.joblib")
    predictions = pd.DataFrame({col: classifier.predict(df_responses) for col, classifier in svm_model.items()})
    
    predictions.to_csv("predictions.csv", index=False)
    # Mark that the CSV file already exists
    st.session_state.csv_exists = True
#     # Get column names where values are equal to 1 (original code)
#     selected_columns = predictions.columns[predictions.iloc[0] == 1].tolist()

    # Due to exploding of 'Preferred learning mode' column, there may be >1 rows of predictions
    # So, we will get all unique column names and put them into a df 
    # Get all column names where the value is equal to 1 for all rows
    selected_columns = predictions.apply(lambda row: predictions.columns[row == 1].tolist(), axis=1)

    # Flatten the list of column names
    all_selected_columns = [col for sublist in selected_columns for col in sublist]

    # Convert the list into a DataFrame and then into a Series to remove duplicates
    df_selected_columns = pd.DataFrame({'Selected_Columns': all_selected_columns})
    unique_selected_columns = df_selected_columns['Selected_Columns'].drop_duplicates()

    # Convert the unique values back to a DataFrame
    df_unique_selected_columns = pd.DataFrame({'Selected_Columns': unique_selected_columns})

    # Save the unique columns into a CSV file
    df_unique_selected_columns.to_csv("selected_columns.csv", index=False)
    # Mark that the CSV file already exists
    st.session_state.csv_exists = True

    # Define your custom mapping
    custom_mapping = {
        'Learning Objects [Slide presentation]': 'Slide Presentation',
        'Learning Objects [Book]': 'Book',
        'Learning Objects [Lecture Note]': 'Lecture Notes',
        'Learning Objects [Educational game]': 'Educational Game',
        'Learning Objects [Video]': 'Video',
        'Learning Objects [Audio-recorded lecture]': 'Audio-Recorded Lecture',
        'Learning Objects [Animated instruction]': 'Animated Instruction',
        'Learning Objects [Real object model]': 'Real Object Model',
        'Learning Objects [Mind Map]': 'Mind Map',
        'Learning Objects [Multimedia content]': 'Multimedia Content',
        'Learning Objects [Interactive Tool]': 'Interactive Tool',
        'Learning Objects [Technology-supported learning include computer-based training systems]': 'Technology-Supported Learning Include Computer-Based Training Systems',
        'Learning Objects [Intelligent computer-aided instruction systems]': 'Intelligent Computer-Aided Instruction Systems'
    }

#     # Perform mapping for selected column names
#     selected_columns_mapped = [custom_mapping.get(col, col) for col in selected_columns]
    
#     # Display selected column names as a table using st.dataframe()
#     data = {'Learning Objects': selected_columns_mapped}
#     df_selected_columns = pd.DataFrame(data, index=range(1, len(selected_columns) + 1))
#     st.dataframe(df_selected_columns)
    
    # Perform mapping for selected column names
    selected_columns_mapped = [custom_mapping.get(col, col) for col in df_unique_selected_columns['Selected_Columns']]

    # Display selected column names as a table using st.dataframe()
    data = {'Learning Objects': selected_columns_mapped}
    df_selected_columns = pd.DataFrame(data, index=range(1, len(selected_columns_mapped) + 1))
    st.dataframe(df_selected_columns)
    
#     return predictions


# Run the questionaire (driver code)
if __name__ == "__main__":
    questionnaire()
