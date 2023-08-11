from flask import Flask, render_template, request
import polars as pl

app = Flask(__name__)

df = pl.read_parquet('oracle_data_dictionary.parquet')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        table_1 = request.form['table_1']
        table_2 = request.form['table_2']
        if table_1 and table_2:
            filtered_df = df.filter(pl.col('RELATIONSHIPS').str.contains(table_1))
            filtered_df = filtered_df.filter(pl.col('RELATIONSHIPS').str.contains(table_2))
            matching_columns = set(filtered_df['COLUMN_NAME'].to_list())
            if matching_columns:
                matching_columns_str = ', '.join(matching_columns)
                return render_template('result.html', matching_columns=matching_columns_str, table_1=table_1, table_2=table_2)
            else:
                return render_template('result.html', message='No matching columns found.', table_1=table_1, table_2=table_2)
        else:
            return render_template('result.html', message='Please enter both table names.')
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

# ! search feature on TABLE_NAME
# ! search feature on COLUMN_NAME
# ! fuzzy matching on COLUMN_NAME