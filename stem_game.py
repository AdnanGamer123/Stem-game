import tkinter as tk
from tkinter import messagebox
import os
import random


# Define conversion functions
def arabic_to_western(number_str):
    arabic_digits = '٠١٢٣٤٥٦٧٨٩'
    western_digits = '0123456789'
    translation_table = str.maketrans(arabic_digits, western_digits)
    return number_str.translate(translation_table)


def western_to_arabic(number_str):
    arabic_digits = '٠١٢٣٤٥٦٧٨٩'
    western_digits = '0123456789'
    translation_table = str.maketrans(western_digits, arabic_digits)
    return number_str.translate(translation_table)


# Define questions and answers
questions_and_answers = {
    'Science': (
        ["ماذا نسمي الماء في حالته الصلبة؟", "ما هو المصدر الرئيسي للضوء خلال النهار?",
         "أي عضو يساعدنا على التنفس?", "أي كوكب هو الأقرب إلى الشمس?",
         "ماذا يحدث للماء عندما يصبح ساخنًا جدًا?", "ما اسم اللبنات الأساسية لجميع الكائنات الحية?",
         "ما نوع الصخور التي تأتي من الصخور المنصهرة؟", "ما هو المكان الذي تعيش فيه النباتات والحيوانات؟",
         "ما هي الكلمة الأخرى للملح؟", "ماذا نحتاج أن نأكل للحصول على الطاقة?"],
        ["الجليد", "الشمس", "الرئتين", "عطارد", "يتحول إلى بخار", "الخلايا", "الصخر الناري", "الموطن", "الملح",
         "الطعام"]
    ),
    'Technology': (
        ["ماذا تعني 'CPU'؟", "ماذا يفعل لوحة المفاتيح؟", "ما اسم الآلة التي تطبع الأوراق؟",
         "ماذا نستخدم لتحريك المؤشر على الشاشة؟", "ما هو الجزء الرئيسي من الكمبيوتر الذي ترى فيه الشاشة؟",
         "ماذا نطلق على الجهاز الذي يتيح لك الاتصال بالإنترنت لاسلكيًا؟", "ماذا تعني 'USB'؟",
         "ما هو اللابتوب؟", "ماذا نطلق على بطاقة الذاكرة الصغيرة المستخدمة في الكاميرات والهواتف؟",
         "ما الجهاز الذي تستخدمه للاستماع إلى الموسيقى أو الأصوات من الكمبيوتر؟"],
        ["وحدة المعالجة المركزية", "يكتب الحروف والأرقام", "طابعة", "فأرة", "شاشة", "واي فاي",
         "النقل التسلسلي العالمي", "كمبيوتر محمول", "بطاقة SD", "مكبرات الصوت"]
    ),
    'Engineering': (
        ["ماذا تعني 'CAD' في الهندسة؟", "ما الغرض الأساسي من الجسر؟",
         "ما المادة التي تستخدم عادةً في صنع التروس؟", "ماذا تعني 'HVAC' في أنظمة البناء؟",
         "ما نوع الهندسة الذي يركز على تصميم الآلات؟", "ما هو الغرض الرئيسي من قاطع الدائرة؟",
         "ما وحدة القوة في النظام المتري؟", "ما المصطلح المستخدم للقوة التي تعارض الحركة في السوائل؟",
         "ما دراسة القوى وتأثيراتها على المواد؟", "ما وحدة المقاومة الكهربائية الأساسية؟"],
        ["تصميم بمساعدة الكمبيوتر", "لدعم وتمكين المرور فوق العوائق", "الفولاذ",
         "التدفئة والتهوية وتكييف الهواء", "الهندسة الميكانيكية",
         "لحماية الدوائر الكهربائية من التحميل الزائد", "نيوتن", "السحب", "الميكانيكا", "أوم"]
    ),
    'Math': (
        ['10 × 8', '10 × 5', "7 + 5", "12 - 4", "9 × 3", "20 ÷ 4", "15 + 6", "18 - 7", "8 × 2", "30 ÷ 5"],
        [80, 50, 12, 8, 27, 5, 21, 11, 16, 6]
    )
}

# Initialize global variables
lives = 5
score = 0
current_questions = []
current_answers = []
current_index = 0
TRACK_FILE = 'user_tracker.txt'
training_question = ""
training_answer = ""
selected_language = 'English'  # Default language


def check_first_time():
    """Check if this is the first time the user is running the program."""
    return not os.path.exists(TRACK_FILE)


def mark_user_as_seen():
    """Create a file to mark the user as having run the program before."""
    with open(TRACK_FILE, 'w') as file:
        file.write('')


def get_random_training_question(category):
    """Get a random training question and answer from the selected category."""
    questions, answers = questions_and_answers[category]
    index = random.randint(0, len(questions) - 1)
    return questions[index], western_to_arabic(str(answers[index]))


def show_training_content(category):
    """Display training content for the selected category."""
    global training_question, training_answer
    training_question, training_answer = get_random_training_question(category)

    def check_training_answer():
        user_answer = training_entry.get()
        if arabic_to_western(user_answer) == arabic_to_western(training_answer):
            messagebox.showinfo("Training", "Correct! You can now start the quiz.")
            mark_user_as_seen()
            main_menu()
        else:
            messagebox.showinfo("Training", f"Incorrect. The correct answer is {training_answer}.")

    def close_program():
        root.destroy()

    training_label.config(text=training_question)
    training_label.pack(pady=20)
    training_entry.pack(pady=5)
    training_submit_button.config(command=check_training_answer)
    training_submit_button.pack(pady=10)

    exit_button = tk.Button(root, text="Close Program", command=close_program, bg='lightcoral', fg='white',
                            font=('Arial', 14))
    exit_button.pack(pady=10)

    training_button.pack_forget()


def start_quiz_window():
    """Initialize the quiz window after training or if not the first time."""
    start_button.config(state=tk.NORMAL)
    answer_entry.config(state=tk.NORMAL)
    submit_button.config(state=tk.NORMAL)


def start_quiz(category):
    global current_questions, current_answers, current_index, lives, score
    current_questions, current_answers = questions_and_answers[category]
    current_index = 0
    lives = 5
    score = 0
    display_question()


def display_question():
    global current_index
    if current_index < len(current_questions):
        question_label.config(text=current_questions[current_index])
        answer_entry.config(state=tk.NORMAL)
        answer_entry.delete(0, tk.END)
        answer_entry.focus_set()
    else:
        end_quiz()


def check_answer(event=None):
    global current_index, lives, score
    answer = answer_entry.get()
    correct_answer = western_to_arabic(str(current_answers[current_index]))

    if answer == correct_answer:
        score += 5
        result_label.config(text=f"Correct! Your score is {western_to_arabic(str(score))}")
    else:
        lives -= 1
        result_label.config(
            text=f"Incorrect. You have {lives} attempts left.\nYour score is {western_to_arabic(str(score))}")

    current_index += 1
    if lives <= 0:
        end_quiz()
    else:
        display_question()


def end_quiz():
    if current_index >= len(current_questions):
        result_label.config(text=f"You've finished all questions! Your final score is {western_to_arabic(str(score))}.")
    else:
        result_label.config(text=f"Game over! Your final score is {western_to_arabic(str(score))}.")
    start_button.config(state=tk.NORMAL)
    answer_entry.config(state=tk.DISABLED)
    submit_button.config(state=tk.DISABLED)


def start_game(category):
    start_quiz(category)
    start_button.config(state=tk.DISABLED)
    answer_entry.config(state=tk.NORMAL)
    submit_button.config(state=tk.NORMAL)


def on_start_science():
    if check_first_time():
        show_training_content('Science')
    else:
        start_game('Science')


def on_start_technology():
    if check_first_time():
        show_training_content('Technology')
    else:
        start_game('Technology')


def on_start_engineering():
    if check_first_time():
        show_training_content('Engineering')
    else:
        start_game('Engineering')


def on_start_math():
    if check_first_time():
        show_training_content('Math')
    else:
        start_game('Math')


def show_about_us():
    """Toggle the visibility of the About Us information."""
    if about_frame.winfo_ismapped():
        about_frame.pack_forget()
    else:
        about_frame.pack(pady=20)


def exit_application():
    """Confirm and close the application."""
    if messagebox.askokcancel("Confirm", "Do you really want to exit?"):
        root.destroy()


def select_language(language):
    global selected_language
    selected_language = language
    language_selection_frame.pack_forget()
    main_menu()


def main_menu():
    global question_label, answer_entry, submit_button, result_label, start_button, training_button, about_button

    # Create main menu widgets
    question_label = tk.Label(root, text="", bg='gray', fg='white', font=('Arial', 16))
    answer_entry = tk.Entry(root, font=('Arial', 14))
    submit_button = tk.Button(root, text="Submit", command=check_answer, bg='lightgreen', fg='black',
                              font=('Arial', 14))
    result_label = tk.Label(root, text="", bg='gray', fg='white', font=('Arial', 16))
    start_button = tk.Button(root, text="Start", command=lambda: start_game('Science'), bg='lightblue', fg='black',
                             font=('Arial', 14))

    # Define the training button
    training_button = tk.Button(root, text="Training", command=lambda: show_training_content('Science'),
                                bg='lightcoral', fg='white', font=('Arial', 14))

    # Define the About Us button
    about_button = tk.Button(root, text="About Us", command=show_about_us, bg='lightgoldenrodyellow', fg='black',
                             font=('Arial', 14))

    # Define the Exit button
    exit_button = tk.Button(root, text="Exit", command=exit_application, bg='lightcoral', fg='white',
                            font=('Arial', 14))

    # Remove previous widgets
    for widget in root.winfo_children():
        widget.pack_forget()

    # Create the main menu
    tk.Label(root, text="Welcome to the STEM Game!", bg='gray', fg='white', font=('Arial', 24)).pack(pady=20)

    tk.Button(root, text="Science", command=on_start_science, bg='tomato', fg='white', font=('Arial', 14),
              width=30).pack(pady=10, fill=tk.X, padx=50)
    tk.Button(root, text="Technology", command=on_start_technology, bg='mediumseagreen', fg='white', font=('Arial', 14),
              width=30).pack(pady=10, fill=tk.X, padx=50)
    tk.Button(root, text="Engineering", command=on_start_engineering, bg='deepskyblue', fg='white', font=('Arial', 14),
              width=30).pack(pady=10, fill=tk.X, padx=50)
    tk.Button(root, text="Math", command=on_start_math, bg='gold', fg='black', font=('Arial', 14), width=30).pack(
        pady=10, fill=tk.X, padx=50)

    # Define and place the training button
    training_button.config(command=lambda: show_training_content('Science'))
    training_button.pack(pady=10, fill=tk.X, padx=50)

    # Define and place the About Us button
    about_button.pack(pady=10, fill=tk.X, padx=50)

    # Define and place the Exit button
    exit_button.pack(pady=10, fill=tk.X, padx=50)

    # Define the About Us frame
    about_frame = tk.Frame(root, bg='gray')
    about_label = tk.Label(about_frame,
                           text="About Us:\nThis is an educational STEM game developed to test your knowledge in various fields.",
                           bg='gray', fg='white', font=('Arial', 14))
    about_label.pack(pady=20)
    about_frame.pack_forget()

    # Widgets for question and answer
    question_label.pack(pady=20)
    answer_entry.pack(pady=10, padx=20, fill=tk.X)
    submit_button.pack(pady=10)
    result_label.pack(pady=20)
    start_button.pack(pady=20)


# Create the main window
root = tk.Tk()
root.title("STEM Game")
root.configure(bg='gray')
root.geometry('800x900')  # Width x Height

# Create and display the language selection frame
language_selection_frame = tk.Frame(root, bg='gray')
tk.Label(language_selection_frame, text="Select Language / اختر اللغة", bg='gray', fg='white', font=('Arial', 24)).pack(
    pady=20)

tk.Button(language_selection_frame, text="العربية", command=lambda: select_language('Arabic'), bg='lightcoral',
          fg='white', font=('Arial', 14), width=30).pack(pady=10, fill=tk.X, padx=50)
tk.Button(language_selection_frame, text="English", command=lambda: select_language('English'), bg='lightseagreen',
          fg='white', font=('Arial', 14), width=30).pack(pady=10, fill=tk.X, padx=50)

language_selection_frame.pack(pady=20)

# Define and place training widgets
training_label = tk.Label(root, text="", bg='gray', fg='white', font=('Arial', 14))
training_entry = tk.Entry(root, font=('Arial', 14))
training_submit_button = tk.Button(root, text="Submit Training Answer", bg='lightsteelblue', fg='black',
                                   font=('Arial', 14))

# Bind the Enter key to the check_answer function
root.bind('<Return>', check_answer)

# Run the application
root.mainloop()
