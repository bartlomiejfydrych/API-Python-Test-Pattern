from datetime import datetime


def log_extra_response_info(r):
    print(f"\nTIMESTAMP: {datetime.now().replace(microsecond=0)}")
    print(f"STATUS CODE: {r.status_code} {r.reason}")
    print(f"RESPONSE BODY:\n{r.text[0:200] + ('...' if (len(r.text) > 200) else '')}")


"""
NOTES: --------------------------------------------------------------------------------------------------------------

datetime.now() - podaje aktualną, pełną datę i godzinę z microsekundami
dlatego dodane jest
.replace(microsecond=0), aby były one ucięte

"""
