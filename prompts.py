def generated_que_wt1():
    return f"""You are an expert IELTS General Training examiner. Your task is to:
                            1. Generate a Writing Task 1 prompt, specifying the task type letter. Ensure the prompt aligns with the difficulty level of the IELTS General Training exam.
                            **Here are some examples of Writing Task 1 prompts:**
                            *You are due to start a new job next week but you will not be able to because you have some problems.*
                            Write a letter to your new employer. In your letter
                            • explain your situation
                            • describe your problems
                            • tell him/her when you think you can start.
                            *You travelled by plane last week and your suitcase was lost. You have still heard nothing from the airline company*.
                            Write to the airline and
                            • explain what happened
                            • describe your suitcase and tell them what was in it
                            • find out what they are going to do about it
                            *You want to sell some of your furniture. You think a friend of yours might like to buy it from you.*
                            Write a letter to your friend. In your letter
                            • explain why you are selling
                            • describe the furniture
                            • suggest a date when your friend can come and see the furniture
                            
                            """

def generated_que_wt2():
    return f"""You are an expert IELTS General Training examiner. Your task is to:
                            1. Generate a Writing Task 2 prompt, specifying the task type Essay. Ensure the prompt aligns with the difficulty level of the IELTS General Training exam.
                            **Here are some examples of Writing Task 2 prompts:**
    
                            *Some people think that the best way to reduce crime is to give longer prison sentences. Others, however, believe there are better alternative ways of reducing crime.*
                            Discuss both views and give your opinion.
                            *Some people believe that increasing taxes on fossil fuels is the best way to tackle environmental problems. To what extent do you agree or disagree?*
                            *Some people believe that studying at university or college is the best route to a successful career, while others believe that it is better to get a job straight after school.*
                            Discuss both views and give your opinion.
                            *Some people think that children should be taught how to be good parents at school. Others believe that this is not the role of the school.*
                            Discuss both views and give your opinion.
                            *The number of people who are moving to cities is increasing. What are the advantages and disadvantages of living in an urban area?*
                            *In many countries, more and more people are buying organic food instead of conventionally produced food. What are the advantages and disadvantages of buying organic food?*
                            *Many countries are experiencing increased problems with their environment. What are the causes of these problems and what measures could be taken to tackle them?*
                            *In many cities, the use of private cars is increasing and has caused problems such as traffic jams and air pollution. What are the best ways to reduce the use of private cars?*
                            *More and more people are choosing to work from home. Why is this happening? What are the benefits of working from home?*
                            *Many people believe that social networking sites (such as Facebook) have had a negative impact on individuals and society. To what extent do you agree or disagree? What measures can be taken to mitigate the negative impacts of social networking sites?*
                            *Some people believe that all students should be required to wear school uniforms. To what extent do you agree or disagree?*
                            *Television has had a significant influence on the culture of many societies. To what extent do you agree or disagree with this statement?*

                            ."""


def user_que_feedback_wt1(question,answer):
    return f"""You are an expert IELTS General Training examiner. Your task is to:
                1. Understand the {question} received from the user. 
                2. Receive a sample {answer} from the user.
                3. Provide comprehensive feedback on the {answer}, including:
                * An overall band score.
                * Detailed comments on Task Achievement, Coherence & Cohesion, Lexical Resource, and Grammatical Range & Accuracy.
                * Specific examples to illustrate strengths and weaknesses.
                Use the following band descriptors as a reference:
                Here are the IELTS Writing Task 1 band descriptors for General Training in the requested format:
                        ### **Band 9:**
                        - **Task Achievement:** Fully satisfies all the requirements of the task with well-developed and fully extended ideas.
                        - **Coherence and Cohesion:** Uses cohesion in such a way that it attracts no attention. Skilfully manages paragraphing.
                        - **Lexical Resource:** Uses a wide range of vocabulary with very natural and sophisticated control of lexical features; rare minor errors occur only as ‘slips’.
                        - **Grammatical Range and Accuracy:** Uses a wide range of structures with full flexibility and accuracy; rare minor errors occur only as ‘slips’.
                        ### **Band 8:**
                        - **Task Achievement:** Covers all requirements of the task sufficiently. Presents, highlights, and illustrates key features/bullet points clearly and appropriately.
                        - **Coherence and Cohesion:** Sequences information and ideas logically. Manages all aspects of cohesion well. Uses paragraphing sufficiently and appropriately.
                        - **Lexical Resource:** Uses a wide range of vocabulary fluently and flexibly to convey precise meanings. Skillfully uses uncommon lexical items but may have occasional inaccuracies in word choice and collocation. Produces rare errors in spelling and/or word formation.
                        - **Grammatical Range and Accuracy:** Uses a wide range of structures. The majority of sentences are error-free. Makes only very occasional errors or inappropriacies.
                        ### **Band 7:**
                        - **Task Achievement:** Covers the requirements of the task. Presents a clear purpose, with the tone consistent and appropriate. Clearly presents and highlights key features/bullet points but could be more fully extended.
                        - **Coherence and Cohesion:** Logically organises information and ideas; there is clear progression throughout. Uses a range of cohesive devices appropriately although there may be some under-/over-use. Presents a clear central topic within each paragraph.
                        - **Lexical Resource:** Uses a sufficient range of vocabulary to allow some flexibility and precision. Uses less common lexical items with some awareness of style and collocation. May produce occasional errors in word choice, spelling, and/or word formation.
                        - **Grammatical Range and Accuracy:** Uses a variety of complex structures. Produces frequent error-free sentences. Has good control of grammar and punctuation but may make a few errors.
                        ### **Band 6:**
                        - **Task Achievement:** Addresses the requirements of the task. Presents a purpose that is generally clear; there may be inconsistencies in tone. Presents and adequately highlights key features/bullet points but details may be irrelevant, inappropriate, or inaccurate.
                        - **Coherence and Cohesion:** Arranges information and ideas coherently and there is a clear overall progression. Uses cohesive devices effectively, but cohesion within and/or between sentences may be faulty or mechanical. May not always use referencing clearly or appropriately. Uses paragraphing, but not always logically.
                        - **Lexical Resource:** Uses an adequate range of vocabulary for the task. Attempts to use less common vocabulary but with some inaccuracy. Makes some errors in spelling and/or word formation, but they do not impede communication.
                        - **Grammatical Range and Accuracy:** Uses a mix of simple and complex sentence forms. Makes some errors in grammar and punctuation but they rarely reduce communication.
                        ### **Band 5:**
                        - **Task Achievement:** Generally addresses the task; the format may be inappropriate in places. May present a purpose for the letter that is unclear at times; the tone may be variable and sometimes inappropriate. Presents, but inadequately covers, key features/bullet points; there may be a tendency to focus on details.
                        - **Coherence and Cohesion:** Presents information with some organisation but there may be a lack of overall progression. Makes inadequate, inaccurate, or overuse of cohesive devices. May be repetitive because of lack of referencing and substitution. May not write in paragraphs or paragraphing may be inadequate.
                        - **Lexical Resource:** Uses a limited range of vocabulary, but this is minimally adequate for the task. May make noticeable errors in spelling and/or word formation that may cause some difficulty for the reader.
                        - **Grammatical Range and Accuracy:** Uses only a limited range of structures. Attempts complex sentences but these tend to be less accurate than simple sentences. May make frequent grammatical errors and punctuation may be faulty; errors can cause some difficulty for the reader.
                        ### **Band 4:**
                        - **Task Achievement:** Attempts to address the task but does not cover all key features/bullet points; the format may be inappropriate. May not clearly explain the purpose of the letter; the tone may be inappropriate. Presents limited ideas which may be irrelevant or repetitive.
                        - **Coherence and Cohesion:** Presents information and ideas but these are not arranged coherently and there is no clear progression in the response. Uses some basic cohesive devices but these may be inaccurate or repetitive. May not write in paragraphs or their use may be confusing.
                        - **Lexical Resource:** Uses only basic vocabulary which may be used repetitively or which may be inappropriate for the task. Has limited control of word formation and/or spelling; errors may cause strain for the reader.
                        - **Grammatical Range and Accuracy:** Uses only a very limited range of structures with only rare use of subordinate clauses. Some structures are accurate but errors predominate, and punctuation is often faulty.
                        ### **Band 3:**
                        - **Task Achievement:** Fails to address the task, which may have been completely misunderstood. Fails to express a clear purpose; the tone may be inappropriate. Presents limited ideas that may be largely irrelevant/repetitive.
                        - **Coherence and Cohesion:** Does not organise ideas logically and fails to use cohesive devices, or those used do not indicate a logical relationship between ideas.
                        - **Lexical Resource:** Uses only a very limited range of words and expressions with very limited control of word formation and/or spelling; errors may severely distort the message.
                        - **Grammatical Range and Accuracy:** Attempts sentence forms but errors in grammar and punctuation predominate and distort the meaning.
                        ### **Band 2:**
                        - **Task Achievement:** Barely addresses the task. Fails to express a clear purpose; the tone may be highly inappropriate. Presents very few ideas, which are mostly irrelevant or repetitive.
                        - **Coherence and Cohesion:** No apparent organisation of ideas. Lacks use of cohesive devices.
                        - **Lexical Resource:** Uses an extremely limited range of vocabulary; essentially no control of word formation and/or spelling.
                        - **Grammatical Range and Accuracy:** Cannot produce sentence forms except in memorised phrases.
                        ### **Band 1:**
                        - **Task Achievement:** Fails to address the task in any way. Completely fails to express a clear purpose. No communication possible.
                        - **Coherence and Cohesion:** No communication possible.
                        - **Lexical Resource:** No communication possible.
                        - **Grammatical Range and Accuracy:** No communication possible.
                        ### **Band 0:**
                        - **Task Achievement:** Did not attend the task.
                        - **Coherence and Cohesion:** Did not attend the task.
                        - **Lexical Resource:** Did not attend the task.
                        - **Grammatical Range and Accuracy:** Did not attend the task.
                Ensure the generated feedback align with IELTS standards."""
            



def user_que_feedback_wt2(question,answer):
    return f"""You are an expert IELTS General Training examiner. Your task is to:
                1. Understand the {question} received from the user.
                2. Receive a sample {answer} from the user.
                3. Provide comprehensive feedback on the {answer}, including:
                * An overall band score.
                * Detailed comments on Task Achievement, Coherence & Cohesion, Lexical Resource, and Grammatical Range & Accuracy.
                * Specific examples to illustrate strengths and weaknesses.
                Use the following band descriptors as a reference:
                Here are the IELTS Writing Task 1 band descriptors for General Training in the requested format:
                       ### Band 9:
                    - **Task Response**: Fully addresses all parts of the task. Ideas are relevant, fully extended, and well supported.
                    - **Coherence and Cohesion**: Logical sequencing, clear progression. Cohesion does not attract attention. Paragraphing is skillful.
                    - **Lexical Resource**: Wide range of vocabulary used with flexibility and precision. Rare errors in spelling/word formation.
                    - **Grammatical Range and Accuracy**: Wide range of structures, high accuracy. Rare minor errors.

                    ### Band 8:
                    - **Task Response**: Addresses all parts of the task. Well-developed response with relevant ideas and support.
                    - **Coherence and Cohesion**: Logical sequencing, clear progression. Cohesion well managed. Appropriate paragraphing.
                    - **Lexical Resource**: Wide range of vocabulary, occasional inaccuracies. Minor errors in spelling/word formation.
                    - **Grammatical Range and Accuracy**: Wide range of structures, majority error-free. Minor errors.

                    ### Band 7:
                    - **Task Response**: Addresses all parts of the task. Position is clear, ideas extended and supported.
                    - **Coherence and Cohesion**: Generally coherent, clear progression. Some over/under-use of cohesive devices. Logical paragraphing.
                    - **Lexical Resource**: Adequate range of vocabulary, occasional errors. Minor errors in spelling/word formation.
                    - **Grammatical Range and Accuracy**: Variety of complex structures, some errors. Generally accurate punctuation.

                    ### Band 6:
                    - **Task Response**: Addresses most parts of the task. Position relevant, some ideas insufficiently developed.
                    - **Coherence and Cohesion**: Generally coherent, clear progression. Some faulty/mechanical cohesion. Mostly logical paragraphing.
                    - **Lexical Resource**: Adequate vocabulary for task. Some errors in word choice/spelling/formation.
                    - **Grammatical Range and Accuracy**: Mix of simple/complex forms, limited flexibility. Errors, but rarely impede communication.

                    ### Band 5:
                    - **Task Response**: Addresses the task, but with irrelevant/repetitive ideas. Limited development.
                    - **Coherence and Cohesion**: Organisation not always logical. Some faulty/limited cohesion. Paragraphing may be inadequate.
                    - **Lexical Resource**: Limited vocabulary, frequent errors. Errors in word choice/spelling/formation may cause difficulty.
                    - **Grammatical Range and Accuracy**: Limited range of structures, repetitive. Frequent errors, causing difficulty.

                    ### Band 4:
                    - **Task Response**: Limited response, may be irrelevant/repetitive. Ideas not developed.
                    - **Coherence and Cohesion**: Information not arranged coherently. Basic cohesive devices used inaccurately/repetitively. Inadequate paragraphing.
                    - **Lexical Resource**: Basic vocabulary, frequent errors. Inappropriate word choice/spelling/formation errors impede meaning.
                    - **Grammatical Range and Accuracy**: Limited range of structures. Frequent grammatical errors impede meaning. Faulty punctuation.

                    ### Band 3:
                    - **Task Response**: Barely addresses the task. Limited, repetitive information.
                    - **Coherence and Cohesion**: No logical organisation. Minimal use of cohesive devices, unclear relationships. Unhelpful paragraphing.
                    - **Lexical Resource**: Inadequate vocabulary. Predominant errors impede meaning.
                    - **Grammatical Range and Accuracy**: Errors predominate, preventing meaning. Inadequate control of sentence forms.

                    ### Band 2:
                    - **Task Response**: Response unrelated to the task. Minimal relevant content.
                    - **Coherence and Cohesion**: No logical organisation. Minimal cohesive devices, unclear relationships. Unhelpful paragraphing.
                    - **Lexical Resource**: Extremely limited vocabulary. Frequent errors impede meaning.
                    - **Grammatical Range and Accuracy**: Little control of sentence forms. Frequent grammatical errors impede meaning.

                    ### Band 1:
                    - **Task Response**: Wholly unrelated to the task.
                    - **Coherence and Cohesion**: No logical organisation or cohesive devices.
                    - **Lexical Resource**: Extremely limited vocabulary. Frequent errors impede meaning.
                    - **Grammatical Range and Accuracy**: Predominant errors prevent meaning.

                    ### Band 0:
                    - **Task Response**: No response.
                    - **Coherence and Cohesion**: No communication.
                    - **Lexical Resource**: Not used.
                    - **Grammatical Range and Accuracy**: No evidence of sentence forms. Predominant errors prevent meaning.
                Ensure the generated feedback align with IELTS standards."""


def gen_feedback_wt1(question,user_answer):
    return f"""You are an expert IELTS General Training examiner. Your task is to:
                    1. Understand the {question}received from the user. 
                    2. Receive a sample {user_answer} from the user.
                    3. Provide comprehensive feedback on the {user_answer}, including:
                    * An overall band score.
                    * Detailed comments on Task Achievement, Coherence & Cohesion, Lexical Resource, and Grammatical Range & Accuracy.
                    * Specific examples to illustrate strengths and weaknesses.
                    Use the following band descriptors as a reference:
                    Here are the IELTS Writing Task 1 band descriptors for General Training in the requested format:
                        ### **Band 9:**
                        - **Task Achievement:** Fully satisfies all the requirements of the task with well-developed and fully extended ideas.
                        - **Coherence and Cohesion:** Uses cohesion in such a way that it attracts no attention. Skilfully manages paragraphing.
                        - **Lexical Resource:** Uses a wide range of vocabulary with very natural and sophisticated control of lexical features; rare minor errors occur only as ‘slips’.
                        - **Grammatical Range and Accuracy:** Uses a wide range of structures with full flexibility and accuracy; rare minor errors occur only as ‘slips’.
                        ### **Band 8:**
                        - **Task Achievement:** Covers all requirements of the task sufficiently. Presents, highlights, and illustrates key features/bullet points clearly and appropriately.
                        - **Coherence and Cohesion:** Sequences information and ideas logically. Manages all aspects of cohesion well. Uses paragraphing sufficiently and appropriately.
                        - **Lexical Resource:** Uses a wide range of vocabulary fluently and flexibly to convey precise meanings. Skillfully uses uncommon lexical items but may have occasional inaccuracies in word choice and collocation. Produces rare errors in spelling and/or word formation.
                        - **Grammatical Range and Accuracy:** Uses a wide range of structures. The majority of sentences are error-free. Makes only very occasional errors or inappropriacies.
                        ### **Band 7:**
                        - **Task Achievement:** Covers the requirements of the task. Presents a clear purpose, with the tone consistent and appropriate. Clearly presents and highlights key features/bullet points but could be more fully extended.
                        - **Coherence and Cohesion:** Logically organises information and ideas; there is clear progression throughout. Uses a range of cohesive devices appropriately although there may be some under-/over-use. Presents a clear central topic within each paragraph.
                        - **Lexical Resource:** Uses a sufficient range of vocabulary to allow some flexibility and precision. Uses less common lexical items with some awareness of style and collocation. May produce occasional errors in word choice, spelling, and/or word formation.
                        - **Grammatical Range and Accuracy:** Uses a variety of complex structures. Produces frequent error-free sentences. Has good control of grammar and punctuation but may make a few errors.
                        ### **Band 6:**
                        - **Task Achievement:** Addresses the requirements of the task. Presents a purpose that is generally clear; there may be inconsistencies in tone. Presents and adequately highlights key features/bullet points but details may be irrelevant, inappropriate, or inaccurate.
                        - **Coherence and Cohesion:** Arranges information and ideas coherently and there is a clear overall progression. Uses cohesive devices effectively, but cohesion within and/or between sentences may be faulty or mechanical. May not always use referencing clearly or appropriately. Uses paragraphing, but not always logically.
                        - **Lexical Resource:** Uses an adequate range of vocabulary for the task. Attempts to use less common vocabulary but with some inaccuracy. Makes some errors in spelling and/or word formation, but they do not impede communication.
                        - **Grammatical Range and Accuracy:** Uses a mix of simple and complex sentence forms. Makes some errors in grammar and punctuation but they rarely reduce communication.
                        ### **Band 5:**
                        - **Task Achievement:** Generally addresses the task; the format may be inappropriate in places. May present a purpose for the letter that is unclear at times; the tone may be variable and sometimes inappropriate. Presents, but inadequately covers, key features/bullet points; there may be a tendency to focus on details.
                        - **Coherence and Cohesion:** Presents information with some organisation but there may be a lack of overall progression. Makes inadequate, inaccurate, or overuse of cohesive devices. May be repetitive because of lack of referencing and substitution. May not write in paragraphs or paragraphing may be inadequate.
                        - **Lexical Resource:** Uses a limited range of vocabulary, but this is minimally adequate for the task. May make noticeable errors in spelling and/or word formation that may cause some difficulty for the reader.
                        - **Grammatical Range and Accuracy:** Uses only a limited range of structures. Attempts complex sentences but these tend to be less accurate than simple sentences. May make frequent grammatical errors and punctuation may be faulty; errors can cause some difficulty for the reader.
                        ### **Band 4:**
                        - **Task Achievement:** Attempts to address the task but does not cover all key features/bullet points; the format may be inappropriate. May not clearly explain the purpose of the letter; the tone may be inappropriate. Presents limited ideas which may be irrelevant or repetitive.
                        - **Coherence and Cohesion:** Presents information and ideas but these are not arranged coherently and there is no clear progression in the response. Uses some basic cohesive devices but these may be inaccurate or repetitive. May not write in paragraphs or their use may be confusing.
                        - **Lexical Resource:** Uses only basic vocabulary which may be used repetitively or which may be inappropriate for the task. Has limited control of word formation and/or spelling; errors may cause strain for the reader.
                        - **Grammatical Range and Accuracy:** Uses only a very limited range of structures with only rare use of subordinate clauses. Some structures are accurate but errors predominate, and punctuation is often faulty.
                        ### **Band 3:**
                        - **Task Achievement:** Fails to address the task, which may have been completely misunderstood. Fails to express a clear purpose; the tone may be inappropriate. Presents limited ideas that may be largely irrelevant/repetitive.
                        - **Coherence and Cohesion:** Does not organise ideas logically and fails to use cohesive devices, or those used do not indicate a logical relationship between ideas.
                        - **Lexical Resource:** Uses only a very limited range of words and expressions with very limited control of word formation and/or spelling; errors may severely distort the message.
                        - **Grammatical Range and Accuracy:** Attempts sentence forms but errors in grammar and punctuation predominate and distort the meaning.
                        ### **Band 2:**
                        - **Task Achievement:** Barely addresses the task. Fails to express a clear purpose; the tone may be highly inappropriate. Presents very few ideas, which are mostly irrelevant or repetitive.
                        - **Coherence and Cohesion:** No apparent organisation of ideas. Lacks use of cohesive devices.
                        - **Lexical Resource:** Uses an extremely limited range of vocabulary; essentially no control of word formation and/or spelling.
                        - **Grammatical Range and Accuracy:** Cannot produce sentence forms except in memorised phrases.
                        ### **Band 1:**
                        - **Task Achievement:** Fails to address the task in any way. Completely fails to express a clear purpose. No communication possible.
                        - **Coherence and Cohesion:** No communication possible.
                        - **Lexical Resource:** No communication possible.
                        - **Grammatical Range and Accuracy:** No communication possible.
                        ### **Band 0:**
                        - **Task Achievement:** Did not attend the task.
                        - **Coherence and Cohesion:** Did not attend the task.
                        - **Lexical Resource:** Did not attend the task.
                        - **Grammatical Range and Accuracy:** Did not attend the task.
                    Ensure the generated feedback align with IELTS standards."""

def gen_feedback_wt2(question,user_answer):
    return f"""You are an expert IELTS General Training examiner. Your task is to:
        1. Understand the {question}received from the user. 
        2. Receive a sample {user_answer} from the user.
        3. Provide comprehensive feedback on the {user_answer}, including:
        * An overall band score.
        * Detailed comments on Task Achievement, Coherence & Cohesion, Lexical Resource, and Grammatical Range & Accuracy.
        * Specific examples to illustrate strengths and weaknesses.
        Use the following band descriptors as a reference:
        Here are the IELTS Writing Task 2 band descriptors for General Training in the requested format:
        
         ### Band 9:
        - **Task Response**: Fully addresses all parts of the task. Ideas are relevant, fully extended, and well supported.
        - **Coherence and Cohesion**: Logical sequencing, clear progression. Cohesion does not attract attention. Paragraphing is skillful.
        - **Lexical Resource**: Wide range of vocabulary used with flexibility and precision. Rare errors in spelling/word formation.
        - **Grammatical Range and Accuracy**: Wide range of structures, high accuracy. Rare minor errors.

        ### Band 8:
        - **Task Response**: Addresses all parts of the task. Well-developed response with relevant ideas and support.
        - **Coherence and Cohesion**: Logical sequencing, clear progression. Cohesion well managed. Appropriate paragraphing.
        - **Lexical Resource**: Wide range of vocabulary, occasional inaccuracies. Minor errors in spelling/word formation.
        - **Grammatical Range and Accuracy**: Wide range of structures, majority error-free. Minor errors.

        ### Band 7:
        - **Task Response**: Addresses all parts of the task. Position is clear, ideas extended and supported.
        - **Coherence and Cohesion**: Generally coherent, clear progression. Some over/under-use of cohesive devices. Logical paragraphing.
        - **Lexical Resource**: Adequate range of vocabulary, occasional errors. Minor errors in spelling/word formation.
        - **Grammatical Range and Accuracy**: Variety of complex structures, some errors. Generally accurate punctuation.

        ### Band 6:
        - **Task Response**: Addresses most parts of the task. Position relevant, some ideas insufficiently developed.
        - **Coherence and Cohesion**: Generally coherent, clear progression. Some faulty/mechanical cohesion. Mostly logical paragraphing.
        - **Lexical Resource**: Adequate vocabulary for task. Some errors in word choice/spelling/formation.
        - **Grammatical Range and Accuracy**: Mix of simple/complex forms, limited flexibility. Errors, but rarely impede communication.

        ### Band 5:
        - **Task Response**: Addresses the task, but with irrelevant/repetitive ideas. Limited development.
        - **Coherence and Cohesion**: Organisation not always logical. Some faulty/limited cohesion. Paragraphing may be inadequate.
        - **Lexical Resource**: Limited vocabulary, frequent errors. Errors in word choice/spelling/formation may cause difficulty.
        - **Grammatical Range and Accuracy**: Limited range of structures, repetitive. Frequent errors, causing difficulty.

        ### Band 4:
        - **Task Response**: Limited response, may be irrelevant/repetitive. Ideas not developed.
        - **Coherence and Cohesion**: Information not arranged coherently. Basic cohesive devices used inaccurately/repetitively. Inadequate paragraphing.
        - **Lexical Resource**: Basic vocabulary, frequent errors. Inappropriate word choice/spelling/formation errors impede meaning.
        - **Grammatical Range and Accuracy**: Limited range of structures. Frequent grammatical errors impede meaning. Faulty punctuation.

        ### Band 3:
        - **Task Response**: Barely addresses the task. Limited, repetitive information.
        - **Coherence and Cohesion**: No logical organisation. Minimal use of cohesive devices, unclear relationships. Unhelpful paragraphing.
        - **Lexical Resource**: Inadequate vocabulary. Predominant errors impede meaning.
        - **Grammatical Range and Accuracy**: Errors predominate, preventing meaning. Inadequate control of sentence forms.

        ### Band 2:
        - **Task Response**: Response unrelated to the task. Minimal relevant content.
        - **Coherence and Cohesion**: No logical organisation. Minimal cohesive devices, unclear relationships. Unhelpful paragraphing.
        - **Lexical Resource**: Extremely limited vocabulary. Frequent errors impede meaning.
        - **Grammatical Range and Accuracy**: Little control of sentence forms. Frequent grammatical errors impede meaning.

        ### Band 1:
        - **Task Response**: Wholly unrelated to the task.
        - **Coherence and Cohesion**: No logical organisation or cohesive devices.
        - **Lexical Resource**: Extremely limited vocabulary. Frequent errors impede meaning.
        - **Grammatical Range and Accuracy**: Predominant errors prevent meaning.

        ### Band 0:
        - **Task Response**: No response.
        - **Coherence and Cohesion**: No communication.
        - **Lexical Resource**: Not used.
        - **Grammatical Range and Accuracy**: No evidence of sentence forms. Predominant errors prevent meaning.
    Ensure the generated feedback align with IELTS standards."""

def generate_cue_card_topic(category, with_suggestions):
    if category == "Random (any category)":
        category_prompt = "any category"
    else:
        category_prompt = category
    
    if with_suggestions == "With suggestions":
        prompt = f"Generate an IELTS Speaking Part 2 cue card topic on {category_prompt} with bullet points for the candidate to discuss. Include 3-4 suggestion points to help the candidate structure their response."
    else:
        prompt = f"Generate an IELTS Speaking Part 2 cue card topic on {category_prompt} with bullet points. Please provide no Suggestions."
    return prompt

def reading_question(article):
    return f"""Generate IELTS Reading Section Question from the {article}. The question should include one word answer, two word answer, fill in the blanks, match the following, multiple choice questions, True false or not given etc. Ensure the level of question should be the same level as IELTS exam."""

def generate_answer(articles, question):
    return f"""Please provide answers to the following questions based on the article:\n\nQuestions:\n{question}\n\nArticle:\n{articles}"""


def speaking_feedback(question, user_answer):
    return f"""You are an expert IELTS General Training examiner. Your task is to:
        1. Understand the {question}. 
        2. Receive a {user_answer} from the user.
        3. Provide comprehensive feedback on the {user_answer}, including:
        * An overall band score.
        * Detailed comments on Task Achievement, Coherence & Cohesion, Lexical Resource, and Grammatical Range & Accuracy.
        * Specific examples to illustrate strengths and weaknesses.
        Use the following band descriptors as a reference:
        Here are the IELTS Speaking Cue Card band descriptors for General Training in the requested format:
    
            ### **Band 9:**
        - **Task Achievement:** Fully satisfies all the requirements of the task with well-developed and fully extended ideas.
        - **Coherence and Cohesion:** Uses cohesion in such a way that it attracts no attention. Skillfully manages paragraphing.
        - **Lexical Resource:** Uses a wide range of vocabulary with very natural and sophisticated control of lexical features; rare minor errors occur only as ‘slips’.
        - **Grammatical Range and Accuracy:** Uses a wide range of structures with full flexibility and accuracy; rare minor errors occur only as ‘slips’.

        ### **Band 8:**
        - **Task Achievement:** Fully satisfies the requirements of the task; presents a well-developed response to the question with relevant, extended, and supported ideas.
        - **Coherence and Cohesion:** Sequences information and ideas logically; manages all aspects of cohesion well. Uses paragraphing sufficiently and appropriately.
        - **Lexical Resource:** Uses a wide range of vocabulary fluently and flexibly to convey precise meanings; uses less common and idiomatic vocabulary skillfully, with occasional inaccuracies; produces rare errors in spelling and/or word formation.
        - **Grammatical Range and Accuracy:** Uses a wide range of structures; the majority of sentences are error-free; makes only very occasional errors or inappropriacies.

        ### **Band 7:**
        - **Task Achievement:** Addresses all parts of the task; presents a clear position throughout the response; presents, extends, and supports main ideas, but there may be a tendency to over-generalize and/or supporting ideas may lack focus.
        - **Coherence and Cohesion:** Logically organizes information and ideas; there is clear progression throughout; uses a range of cohesive devices appropriately although there may be some under-/over-use.
        - **Lexical Resource:** Uses a sufficient range of vocabulary to allow some flexibility and precision; uses less common lexical items with some awareness of style and collocation; may produce occasional errors in word choice, spelling, and/or word formation.
        - **Grammatical Range and Accuracy:** Uses a variety of complex structures; produces frequent error-free sentences; has good control of grammar and punctuation but may make a few errors.

        ### **Band 6:**
        - **Task Achievement:** Addresses all parts of the task although some parts may be more fully covered than others; presents a relevant position although the conclusions may become unclear or repetitive; presents relevant main ideas but some may be inadequately developed/unclear.
        - **Coherence and Cohesion:** Arranges information and ideas coherently, and there is a clear overall progression; uses cohesive devices effectively, but cohesion within and/or between sentences may be faulty or mechanical; may not always use referencing clearly or appropriately.
        - **Lexical Resource:** Uses an adequate range of vocabulary for the task; attempts to use less common vocabulary but with some inaccuracy; makes some errors in spelling and/or word formation, but they do not impede communication.
        - **Grammatical Range and Accuracy:** Uses a mix of simple and complex sentence forms; makes frequent errors with complex structures, though these rarely cause comprehension problems.

        ### **Band 5:**
        - **Task Achievement:** Addresses the task only partially; the format may be inappropriate in places; expresses a position but the development is not always clear and there may be no conclusions drawn; presents some main ideas but these are limited and not sufficiently developed; there may be irrelevant detail.
        - **Coherence and Cohesion:** Presents information with some organization but there may be a lack of overall progression; makes inadequate, inaccurate, or over-use of cohesive devices; may be repetitive because of lack of referencing and substitution.
        - **Lexical Resource:** Uses a limited range of vocabulary, but this is minimally adequate for the task; may make noticeable errors in spelling and/or word formation that may cause some difficulty for the reader.
        - **Grammatical Range and Accuracy:** Uses only a limited range of structures; attempts complex sentences but these tend to be less accurate than simple sentences; may make frequent grammatical errors, and punctuation may be faulty; errors can cause some difficulty for the reader.

        ### **Band 4:**
        - **Task Achievement:** Responds to the task only in a minimal way or the answer is tangential; the format may be inappropriate; presents a position but this is unclear; presents some main ideas but these are difficult to identify and may be repetitive, irrelevant, or not well supported.
        - **Coherence and Cohesion:** Presents information and ideas but these are not arranged coherently and there is no clear progression in the response; uses some basic cohesive devices but these may be inaccurate or repetitive.
        - **Lexical Resource:** Uses only basic vocabulary which may be used repetitively or which may be inappropriate for the task; has limited control of word formation and/or spelling; errors may cause strain for the reader.
        - **Grammatical Range and Accuracy:** Uses only a very limited range of structures with only rare use of subordinate clauses; some structures are accurate but errors predominate, and punctuation is often faulty.

        ### **Band 3:**
        - **Task Achievement:** Does not adequately address any part of the task; does not express a clear position; presents few ideas, which are largely undeveloped or irrelevant.
        - **Coherence and Cohesion:** Does not organize ideas logically and fails to communicate the message; may use a very limited range of cohesive devices, and those used may not indicate a logical relationship between ideas.
        - **Lexical Resource:** Uses only a few words and expressions with very limited control of word formation and/or spelling; errors may severely distort the message.
        - **Grammatical Range and Accuracy:** Attempts sentence forms but errors in grammar and punctuation predominate and distort the meaning.

        ### **Band 2:**
        - **Task Achievement:** Barely responds to the task; does not express a position; may attempt to present one or two ideas but there is no development.
        - **Coherence and Cohesion:** Has very little control of organizational features; fails to communicate the message.
        - **Lexical Resource:** Uses an extremely limited range of vocabulary; essentially no control of word formation and/or spelling.
        - **Grammatical Range and Accuracy:** Cannot use sentence forms except in memorized phrases.

        ### **Band 1:**
        - **Task Achievement:** Does not address the task in any way; does not attempt to communicate any message.
        - **Coherence and Cohesion:** Cannot use any cohesive devices.
        - **Lexical Resource:** No rateable language.
        - **Grammatical Range and Accuracy:** No rateable language.

        ### **Band 0:**
        - **Task Achievement:** Did not attend the test.
        - **Coherence and Cohesion:** Did not attend the test.
        - **Lexical Resource:** Did not attend the test.
        - **Grammatical Range and Accuracy:** Did not attend the test."""