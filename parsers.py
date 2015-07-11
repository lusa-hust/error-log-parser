import parse
import sys


FORMAT_STRING = {'haproxy': "{ip}:{port} \
[{times}] \
{frontend_name_transport} \
{backend_name}/{server_name} \
{tq}/{tw}/{tc}/{tr}/{tt} \
{status_code} \
{bytes_sent} \
{captured_request_cookie} \
{captured_response_cookie} \
{country} \
{actconn}/{feconn}/{beconn}/{srv_conn}/{retries} \
{srv_queue}/{backend_queue} \
{{{other}}} \"{http_request}\"", 'lighttpd': "{ip} \
[{time}] \
\"{http_request}\" \
{status_code} \
{byte_sent} \
\"{referer}\" \
\"{user_agent}\" \
{byte_in} \
{byte_out} \
{time_used} \
{request_hostname}", 'nginx': "{ip} \
{http_x_forwarded_for} \
[{time}] \
{http_host} \
\"{http_request}\" \
{status_code} \
{bytes_sent} \
\"{http_referer}\" \
{http_user_agentt}", 'ATS': "{time} RESPONSE: sent \
{ip} status \
{status_code} \
({accelerator}) for \
\'{http_referer}\'", 'haproxy2': "{ip}:{port} \
[{times}] \
{frontend_name_transport} \
{backend_name}/{server_name} \
{tq}/{tw}/{tc}/{tr}/{tt} \
{status_code} \
{bytes_sent} \
{captured_request_cookie} \
{captured_response_cookie} \
{country} \
{actconn}/{feconn}/{beconn}/{srv_conn}/{retries} \
{srv_queue}/{backend_queue} \
\"{http_request}\""}


def parser_function(mode, string):

    if mode == 1:
        format_string_s = FORMAT_STRING['haproxy']
    if mode == 2:
        format_string_s = FORMAT_STRING['lighttpd']
    if mode == 3:
        format_string_s = FORMAT_STRING['nginx']
    if mode == 4:
        format_string_s = FORMAT_STRING['ATS']
    if mode == 5:
        format_string_s = FORMAT_STRING['haproxy2']

    detail = parse.parse(format_string_s, string)
    if detail is not None:
        return detail.named
    else:
        return None


def processing_log(mode, string):

    detail_dict = parser_function(mode, string)

    if detail_dict is None and mode is 1:
        detail_dict = parser_function(5, string)
        # print detail_dict # test

    if detail_dict is not None:
        # print detail_dict # test
        print
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
