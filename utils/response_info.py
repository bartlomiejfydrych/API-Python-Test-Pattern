from datetime import datetime


class ResponseInfo:

    @staticmethod
    def log_extra_response_info(r):
        print(f"\nTIMESTAMP: {datetime.now().replace(microsecond=0)}")
        print(f"STATUS CODE: {r.status_code}")
        print(f"RESPONSE BODY:\n{r.text[0:200] + ('...' if (len(r.text) > 200) else '')}")


"""
NOTES: --------------------------------------------------------------------------------------------------------------

datetime.now() - podaje aktualną, pełną datę i godzinę z microsekundami
dlatego dodane jest
.replace(microsecond=0), aby były one ucięte

"""
