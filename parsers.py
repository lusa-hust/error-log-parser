import parse


FORMAT_STRING = {
    'HAPROXY':
'{ip}:{port} \
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
{{{other}}} "{http_request}"',

    'LIGHTTPD':
'{ip} \
[{time}] \
"{http_request}" \
{status_code} \
{byte_sent} \
\"{referer}\" \
\"{user_agent}\" \
{byte_in} \
{byte_out} \
{time_used} \
{request_hostname}',

    'NGINX':
'{ip} \
{http_x_forwarded_for} \
[{time}] \
{http_host} \
\"{http_request}\" \
{status_code} \
{bytes_sent} \
"{http_referer}" \
{http_user_agentt}',

    'ATS':
"{time} RESPONSE: sent \
{ip} status \
{status_code} \
({accelerator}) for \
'{http_referer}'",

    'HAPROXY2':
'{ip}:{port} \
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
"{http_request}"'
}


def log_parsers(mode, input_string):

    if mode == 1:
        format_string_s = FORMAT_STRING['HAPROXY']
    elif mode == 2:
        format_string_s = FORMAT_STRING['LIGHTTPD']
    elif mode == 3:
        format_string_s = FORMAT_STRING['NGINX']
    elif mode == 4:
        format_string_s = FORMAT_STRING['ATS']
    elif mode == 5:
        format_string_s = FORMAT_STRING['HAPROXY2']
    else:
        raise 'Unknown mode', mode

    detail = parse.parse(format_string_s, input_string)
    if detail is not None:
        return detail.named
    else:
        return None


def processing_log(mode, input_string):

    error_info = log_parsers(mode, input_string)

    if error_info is None and mode is 1:
        error_info = log_parsers(5, input_string)

    if error_info is None:
        raise 'Wrong log format', input_string

    return error_info
