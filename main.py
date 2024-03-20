from db import students
import openai
import json

if __name__ == '__main__':
    student_custom_functions = [
        {
            'name': 'extract_student_info',
            'descriptions': 'Get the student information from the body of the input text',
            'parameters': {
                'type': 'object',
                'properties': {
                    'Firstname': {
                        'type': 'string',
                        'description': 'first name of the student',
                    },
                    'Address': {
                        'type': 'string',
                        'description': 'address of the student'
                    },
                    'City': {
                        'type': 'string',
                        'description': 'city of the student'
                    },
                    'phone number': {
                        'type': 'string',
                        'description': 'phone number of the student'
                    }
                }
            }

        }
    ]

    for student in students:
        response = openai.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=[{'role': 'user', 'content': f'extract the details for each {student}'}],
            functions=student_custom_functions,
            function_call='auto'
        )
        json_response = json.loads(response.choices[0].message.function_call.arguments)
        print(json_response)
