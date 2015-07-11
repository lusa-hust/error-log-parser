import parse
import sys


def parser_lighttpd(string):

    format_string = "{ip} \
[{time}] \
\"{request}\" \
{status} {bytesent} \
\"{referer}\" \
\"{uagent}\" \
{bytein} \
{byteout} \
{timeused} \
{rhostname}"
    detail = parse.parse(format_string, string)
    if detail is not None:
        return detail.named
    else:
        return None


def parser_nginx(string):

    format_string = "{ip} \
{http_x_forwarded_for} \
[{time}] \
{http_host} \
\"{request}\" \
{status} \
{bytes_sent} \
\"{http_referer}\" \
{http_user_agentt}"
    detail = parse.parse(format_string, string)
    if detail is not None:
        return detail.named
    else:
        return None


def parser_nginx(string):

    format_string = "{ip} \
{http_x_forwarded_for} \
[{time}] \
{http_host} \
\"{request}\" \
{status} \
{bytes_sent} \
\"{http_referer}\" \
{http_user_agentt}"
    detail = parse.parse(format_string, string)
    if detail is not None:
        return detail.named
    else:
        return None


def parser_ats(string):

    format_string = "{time} RESPONSE: sent \
{ip} status \
{status} \
({accelerator}) for \
\'{http_referer}\'"
    detail = parse.parse(format_string, string)
    if detail is not None:
        return detail.named
    else:
        return None


def processing_log(mode, string):

    if mode == 2:
        detail_dict = parser_lighttpd(string)
    if mode == 3:
        detail_dict = parser_nginx(string)

    if detail_dict is not None:
        print detail_dict # test
        # send to sentry..


if __name__ == '__main__':

    if len(sys.argv) != 3:
        print "Wrong format\npython {} [mode] [file-log]".format(sys.argv[0])
        exit("mode :\n1. HAProxy\n2. lighttpd\n3. nginx\n4. ATS")

    mode = int(sys.argv[1])

    if mode < 1 or mode > 4:
        exit("""Wrong Mode please choose mode
        1. HAProxy
        2. lighttpd
        3. nginx
        4. ATS""")

    with open(sys.argv[2]) as f:
        for line in f:
            processing_log(mode, line.strip())
