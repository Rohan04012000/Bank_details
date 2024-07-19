from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

#Read the csv file into a DataFrame using pandas.
banks_data = pd.read_csv("bank_branches.csv")

#Rest Api, to fetch the details of bank based on Branch Name.
@app.route("/get_bank_details", methods = ['GET'])
def bank_details_func():
    if request.method == "GET":
        branch_name = request.get_json().get('branch')

        #if there exist a key branch and data corresponding to the key, sent through payload request.
        if branch_name:
            branch_name.lower()
            #The code from lines 22 to 31 works the same as the following two lines, but using pandas takes less time
            filtered_data = banks_data[banks_data['branch'].str.lower() == branch_name]
            final_list_of_banks = filtered_data.to_dict(orient = 'records')

            """fetched_records = []
            for index, row in banks_data.iterrows():
                branch_value = str(row['branch']).lower()
                if branch_value == branch_name:
                    fetched_records.append(row)
            if fetched_records:
                filtered_data = pd.DataFrame(fetched_records)
                final_list_of_banks = filtered_data.to_dict(orient='records')
            else:
                final_list_of_banks = []"""

            if not final_list_of_banks:
                return "No records found for the given Branch name!", 400
            else:
                return jsonify(final_list_of_banks)
        else:
            return "Column name should be branch!", 400
    else:
        return "Method is not supported!.", 405


#if __name__ == "__main__":
    #app.run(debug = True)


