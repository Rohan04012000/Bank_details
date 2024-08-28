# Bank_details
This project was implemented using PyCharm, Python, Flask and Pandas. PyCharm provides a virtual environment!.

## Endpoints to get the Bank List and its branch details for a specific branch, which is deployed on render.com: (Endpoint is suspended! No more deployed on Render.com)
https://bank-details-q9h7.onrender.com/get_bank_details

This endpoint should be entered in Postman with the method set to POST. Navigate to the body tab, select raw and choose json from the dropdown menu.<br>
Enter the following JSON object into the body section: <br/>
{<br/>
    "branch":"KANJUR"<br/>
}<br>

## The sequence through which this assignment was solved is as follows:
1. Created Flask app instance.
2. Loaded CSV data into Pandas DataFrame.
3. Defined a POST endpoint "/get_bank_details".
4. Checked request method.
5. Retrieved "branch" parameter from request payload.
6. Validated existence of branch parameter.
7. Converted branch name to lowercase.
8. Filtered DataFrame based on branch name using Pandas.
9. Converted filtered data to list of dictionaries.
10. Checked if records exist.
11. Returned appropriate response based on records existence.
12. Handled missing branch parameter case.
13. Handled unsupported HTTP methods.

## Test cases:
This code handles every possible edge cases and gives out proper response.
### Test case 1: The code handles cases where the entered branch name is in lowercase.
{<br/>
    "branch":"kanjur",<br/>
}<br>


# Detailed steps for deploying this project on an online service such as Render.com:
## 1. Create a requirements.txt file:
Write down all the dependencies that are used in the flask file.

## 2. Create a separate repository on GitHub:
Store the Flask code and the requirements.txt file in this repository.

## 3. Link the GitHub repository with Render.com:
Deploy the project by following these steps:<br/>
1. Sign in to your Render.com account.
2. Click on the "New" button and select "Web Service".
3. Connect your GitHub account and choose the repository you created.
4. Configure the deployment settings, such as the build command and the start command.
5. Click "Create Web Service" to deploy your project.<br/>
By following these steps, you will successfully deploy your project on Render.com.




