from utils import get_data, get_filtred_data, get_last_values, get_formatted_data


def main():
    OPERATIONS_URL = "https://s3.us-west-2.amazonaws.com/secure.notion-static.com/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230209T141538Z&X-Amz-Expires=86400&X-Amz-Signature=e775e3c0cecb05e082b1c557a7348ccd0f91e75d9e29d3c74c8dba729c3c4c34&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22operations.json%22&x-id=GetObject"
    FILTERED_EMPTY_FROM = True
    COUNT_LAST_VALUES = 5


    data, info = get_data(OPERATIONS_URL)
    if not data:
        exit(info)
    else:
        print(info)

    data = get_filtred_data(data, filtred_empty_from=FILTERED_EMPTY_FROM)
    data = get_last_values(data, COUNT_LAST_VALUES)
    data = get_formatted_data(data)

    print("INFO: Вывод данных")
    for row in data:
        print(row, end='\n\n')


if __name__ == "__main__":
    main()