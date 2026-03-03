# Document your edge case here
- To get marks for this section you will need to explain to your tutor:
1) The edge case you identified
What happens when inserting a student with an empty name or course (the spec specifies mark is optional, but nothing for name or course)
2) How you have accounted for this in your implementation
- I decided it doesn't make sense to store records of marks that don't belong to a student and / or to a course
- Therefore, I have checked if name and course actually exist in create_student
- if either doesn't exist, rather than creating the student I return an error
