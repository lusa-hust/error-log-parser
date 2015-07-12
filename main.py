import sys
import parsers
import sentry

LOG_TYPE =['HAProxy', 'lighttpd', 'nginx', 'ATS'] 
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

    # initialize connection to sentry server
    client = sentry.initialize_connection(
        "http://ea8723b06f824d55b49031a702caa2c6:20fdb8b37c354c05b9c5c6ae1807c4a7@sentry.platform.vn/11"
    )
    
    type_of_log = LOG_TYPE[mode - 1]
    
    with open(sys.argv[2]) as f:
        for line in f:
            detail_dict = parsers.processing_log(mode, line.strip())
            try:
                if detail_dict['status_code'] == '200' or detail_dict['status_code'] == '404':
                    message_send = type_of_log + " " + detail_dict['status_code']
                    sentry.push_to_sentry(client, message_send, detail_dict)
            except Exception, e:
                print e
                
