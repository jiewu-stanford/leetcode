<h3>Motivation:</h3>

1. provide a one-stop reference site for people preparing for coding interview

2. emphasize on idea and code comprehension instead of code optimization

3. introduce alternative solutions to help coders become more versatile and more open-minded

4. show relationship between different problems to focus on transferrable tools, techniques and ways of thinking




<h3>Note:</h3>

1. The solutions selected are not at all the fastest (in terms of time) or most efficient (in terms of memory) or most concise (in terms of the number of lines of code) but are the most comprehensible. In many instances the code is intentionally lengthened to avoid one-liners (which are put aside as comment sometimes). In addition regular expression trick is avoided whenever possible although it is important and you are encouraged to pick it up once you successfully passed the interview. The emphasis here is on pedagogy not performance.

2. I have strived to write solutions of related problems and alternative solutions of a single problem using the same template i.e. same name for variables/functions and same flowchart/layout/steps for ease of comparison (the most salient example being the use of stack and queue). Sometimes parts of the related solution are put alongside to highlight the difference.

3. I have strived to write related parts within a solution using the same names for variables/functions and same flowchart/layout/steps for ease of understanding and highlighting the similarity and difference between blocks of code ('coding aesthetics').

4. Solutions without reference link are my own solutions which are in my opinion so trivial that a lot of people can come up with thus do not merit the assignment of credit to a specific person. I have strived to include all relevant references but due to the large volume of the problems I may have omitted some. Please accept my apology for the omission.

5. For premium problems (marked by three \$ sign) I tried to find Lintcode OJ for the same problem. If Lintcode has it then the problem link in Lintcode is given as well and the solutions are tested against Lintcode OJ. If Lintcode does not have the problem either then the solutions are untested.

6. Helper functions are named 'helper' throughout unless they warrant a particular name to indicate their purpose (e.g. binarySearch, isCyclic) or for distinguishing approaches (e.g. dfs vs. bfs).

7. For problems that I deem unclearly stated or better classified as a math problem or too trivial to try a three X sign is given next to the problem title.

8. I have tested every solution to ensure that it is correct by the time of writing. However LeetCode does change problems from time to time. Hence if I am not able to capture the change promptly please modify the solution by yourself should the problem be changed such that the solution does not pass the test.




<h3>Suggestion on how to prepare for coding interview:</h3>

1. week 1 to week 3: \
Go over the solutions of the first 400 or the most important 250 problems (ref: https://cspiration.com/leetcodeClassification) by typing line-by-line (not cut and paste!). Try to understand each line while typing out the solutions. Challenge yourself by asking whether you can further optimize the code or at least give better names to the variables/functions.\
Go through problems category by category and try to compare the solutions of related problems which are intentionally put alongside with each other (e.g. Best Time to Buy and Sell Stock I, II, III, IV, with cooldown). See if you can modify the solution of one problem to solve another. For problems with multiple solutions you should select and type the majority of them instead of being complacent by having one. In addition because the sample template is used for multiple solutions you can directly modify the previous solution to get the current one to appreciate the changes made.

2. week 4 to week 9: \
Close your typed solution book and go back to LeetCode OJ to attempt the same problems and test your grasp of the solutions. You now also have to pay attention to the nitty-gritty details such as +1 or index bound. This time you should not go through problems category by category. Instead you should randomly pick a problem from one category (say array) and then attempt a randomly picked problem from another category (say string) and so on until you have gone through all categories (the last being design). After that come back to the first category (which is array) and start the iteration again.

3. week 10+: (if you still have time) \
Attempt the remaining 700+ problems in LeetCode. This time attempt directly in LeetCode OJ. Set up a time limit for yourself according to the level of difficulty of the problem. Be disciplined and refrain from searching for solutions until the time is up. When you finish (either by coming up with your own solution or found a solution from the web) try to insert the solution to your previously typed solutions of the first 400 problems. Do not simply append the solution to the end. Instead you should try to find the problem that is most closely related and insert next to it. This forces you to compare the problems and solutions ane reinforces your understanding gained from the training on the first 400 problems.\
In this way although your coding skills may not improve dramatically within 2 months, your coding interview skills will.




<h3>List of abbreviations used to name variables are:</h3>

2 in between alphabets means conversion to -> \
d = dictionary \
dp = default variable for dynamic programming \
indx = index \
ni = new i \
nj = new j \
ox = old x \
oy = old y \
l = left \
r = right \
pos = position \
r = number of rows (the full 'rows' are used when r is used to represent right) \
c = number of columns (the full 'cols' are used when c is used to represent character) \
c = character (in string or word) \
s = string \
arr = array \
dir = direction \
lst = list \
curr = current \
prev = previous \
acc = accumulated \
cum = cumulative \
comb = combination \
dif = difference \
rem = remaining \
rev = reverse \
val = value \
res = result




Comments and suggestions (errors, better solutions) are very much welcome. Please send to my hotmail account named 'physics-math'