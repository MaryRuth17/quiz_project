
# questions for the quiz
quiz_questions = [
    {
        "question": "How do you handle challenges?",
        "choices": [
            "a. I face them head-on with courage.",
            "b. I analyze the situation and plan carefully.",
            "b. I look for creative ways to outmaneuver the problem.",
            "c. I stay persistent and work hard until I overcome it."
            ]
    },
    {
        "question": "What’s your biggest strength?",
        "choices": [
            "a. My bravery and determination.",
            "b. My intelligence and insight.",
            "c. My cunning and adaptability.",
            "d. My loyalty and dependability."
        ]
    },
    {
        "question": "How do you approach teamwork?",
        "choices": [
            "a. I take the lead and inspire others.",
            "b. I offer innovative ideas and think ahead.",
            "c. I strategize to ensure we get the best outcome.",
            "d. I support everyone and make sure no one is left behind."
        ]
    },
    {
        "question": "What motivates you most?",
        "choices": [
            "a. Adventure and doing what’s right.",
            "b. Learning and personal growth.",
            "c. Achieving my goals and proving myself.",
            "d. Helping others and making a difference."
        ]
    },
    {
        "question": "How do you react to failure?",
        "choices": [
            "a. I see it as a chance to be bold and try again.",
            "b. I learn from it and improve.",
            "c. I see it as a lesson to refine my approach.",
            "d. I accept it, regroup, and keep going."
        ]
    },
    {
        "question": "How do others describe you?",
        "choices": [
            "a. Brave and daring.",
            "b. Wise and insightful.",
            "c. Ambitious and resourceful.",
            "d. Kind and reliable."
        ]
    },
    {
        "question": "Which place feels most like home to you?",
        "choices": [
            "a. Somewhere vibrant, adventurous, and full of action.",
            "b. A library, classroom, or anywhere I can learn.",
            "c. A quiet place where I can plan and strategize.",
            "d. Somewhere warm, welcoming, and full of good company."
        ]
    },
    {
        "question": "What’s your greatest fear?",
        "choices": [
            "a. Not being able to protect others.",
            "b. Being misunderstood or underestimated.",
            "c. Losing control over my destiny.",
            "d. Letting someone down."
        ]
    },
    {
        "question": "What’s your ideal way to spend a free day?",
        "choices": [
            "a. Trying something exciting or new.",
            "b. Reading, studying, or exploring something interesting.",
            "c. Planning for the future or building something meaningful.",
            "d. Relaxing with friends and family."
        ]
    },
    {
        "question": "If you could have one magical ability, what would it be?",
        "choices": [
            "a. The strength to defend against any danger.",
            "b. The ability to instantly learn any skill or knowledge.",
            "c. The power to persuade and charm anyone.",
            "d. The gift to heal and comfort others."
        ]
    }
]

# the result animal in the choices
spirit_animal = [
    {
        "name": "LION",
        "description": "The lion embodies courage, leadership, and a strong sense of justice. Those aligned with the lion are bold and fearless in the face of challenges, often stepping forward to protect others or take charge in uncertain times. Lions thrive in dynamic, action-packed environments where their bravery and determination can shine. Their greatest strength is their unyielding resolve, and they are deeply motivated by adventure, honor, and doing what’s right. Lions fear failing to protect the people they care about and take great pride in their ability to inspire and lead."
    },
    {
        "name": "EAGLE",
        "description": "The eagle symbolizes intelligence, vision, and the pursuit of knowledge. Individuals connected to the eagle are insightful, thoughtful, and driven by a desire for self-improvement and discovery. They approach challenges with careful analysis and use their sharp minds to craft innovative solutions. Eagles are often found in places where they can learn, think ahead, and develop new ideas. They are motivated by growth and understanding, but they fear being underestimated or misunderstood. Eagles value wisdom, clarity, and soaring above obstacles with precision and purpose."
    },
    {
        "name": "SNAKE",
        "description": "The snake represents cunning, adaptability, and resourcefulness. People who resonate with the snake are strategic and clever, always looking for creative ways to overcome challenges and achieve their goals. They excel at reading situations, spotting opportunities, and navigating complexity with finesse. Snakes thrive in quiet, focused spaces where they can plan and strategize. They are motivated by ambition and the drive to control their destiny but fear losing that control. Known for their charisma and ability to adapt, snakes turn setbacks into stepping stones with their ingenuity."
    },
    {
        "name": "BADGER",
        "description": "The badger symbolizes perseverance, loyalty, and kindness. Those who identify with the badger are grounded, dependable, and deeply committed to helping others. They approach challenges with hard work and persistence, ensuring no one is left behind. Badgers thrive in warm, welcoming environments surrounded by family and friends. Their biggest motivation is making a positive difference in the lives of others, and they fear letting people down. With their nurturing and reliable nature, badgers are the heart of any community, providing support and strength to those around them."
    }
]

# Function to determine your spirit animal
def get_spirit_animal(answers):
    animal_scores = {"a": "LION", "b": "EAGLE", "c": "SNAKE", "d": "BADGER"}
    score_count = {"LION": 0, "EAGLE": 0, "SNAKE": 0, "BADGER": 0}

    for answer in answers: # counting the choices
        if answer in animal_scores:
            score_count[animal_scores[answer]] += 1

    highest_score = max(score_count.values()) # finding the highest choice
    
    result_animals = []
    for animal, score in score_count.items():
        if score == highest_score:
            result_animals.append(animal)

    return result_animals

# Get user input while displaying questions
user_answers = []
for q in quiz_questions:
    print(q["question"])
    for choice in q["choices"]:
        print(choice)
    
    while True:
        answer = input("Enter your answer (a, b, c, or d): ").strip().lower()
        if answer in ["a", "b", "c", "d"]:
            user_answers.append(answer)
            break
        else:
            print("Invalid input. Please enter a, b, c, or d.")

# Get and display the result
result = get_spirit_animal(user_answers)
print("Your spirit animal(s):", " ".join(result))