import xlsxwriter


def generate_excel_output(stripped_file_name, tax_bill_list, declaration_form_list, tax_ID_list, tax_amount_list):
    # prepare spread sheet list, which stores row lists of
    # elements, tax_bill_list, declaration_form_list, tax_ID_list
    # and tax_amount_list
    spread_sheet = []
    row = []
    for i in range(0, len(tax_bill_list)):
        row.append(declaration_form_list[i])
        row.append(tax_bill_list[i])
        row.append(tax_ID_list[i])
        row.append(tax_amount_list[i])
        spread_sheet.append(row)
        row = []
#    print(spread_sheet)
    generate_excel(stripped_file_name, spread_sheet)


def generate_excel(stripped_file_name, spread_sheet):
    workbook = xlsxwriter.Workbook(stripped_file_name + "xlsx")
    worksheet = workbook.add_worksheet()

    tax_bill_column = ""
    customs_bill_column = ""
    tax_ID_column = ""
    tax_amount_column = ""

    row = 0
    col = 0

    for tax_bill_column, customs_bill_column, tax_ID_column, tax_amount_column in spread_sheet:
        worksheet.write(row, col, tax_bill_column)
        worksheet.write(row, col+1, customs_bill_column)
        worksheet.write(row, col+2, tax_ID_column)
        worksheet.write(row, col+3, tax_amount_column)
        row += 1

    workbook.close()
    # print("產出彙總稅單清單轉檔(.xslx):" + stripped_file_name + "xlsx")
