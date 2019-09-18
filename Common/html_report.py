#!/usr/bin/env python
#############################################################################################################################################
__filename__ = "html_report.py"
__description__ = "contains functions to write html Report"
__author__ = "Chethana S R"
__copyright__ = "Copyright 2019"
__credits__ = ["Chethana S R"]
__version__ = "1.0"
__maintainer__ = "Chethana"
__email__ = "rchethana@shravas.com"
__status__ = "Developing Stage"
#############################################################################################################################################
#Import Packages

import socket
import getpass
import platform
import time
from Common import config
from Common.config import *
from Tests.Metadata import *


#########################################################################################################################################
# #Funtion to get the error status
# print config.tc_result
# def get_test_status():
#     if config.tc_result == "PASS":
#         config.bln_critical_error_found = False
#         config.bln_sucess = True
#     else:
#         config.bln_critical_error_found = True
#         config.bln_sucess = False
#         #criticalerror= "UNEXPECTED INTRUPTION"
#
# get_test_status()
###############################################################################################################################################
#Function to write header of html Page
def html_header():
    intTC_SlNo = 0
    html_file = open( config.html_report_path, 'w' )
    #print config.html_report_path
    #print total_testcase_count

    message = "<table border=1 width=100%><tr><td colspan=4><font size=6 face=Cambria color=green><center>"" \
    ""<b>SDK Automation Testing</b></center></font></td></tr>""<html><head><meta name=""generator"" content="" "">"" \
    ""<title>SDK Regression</title><meta http-equiv=""refresh"" content=""150"">"" \
    ""<style type=""text/css"">div.c1 {text-align: left}</style></head><body>"" \
    ""<div class=""c1""><img src=""http://www.ceicdata.com/images/CEIC_Logo.gif""></div>"

    html_file.write(message)

    #Write System Name - & Operating System
    message = "<table border=1 width=100%><tr><td width=20%><font size=""3.5 face=""Cambria color=""green""><b>System Name:</td>"" \
    ""<td width=30%><font size=""3.5 face=""Cambria color=""brown><b>" + socket.gethostname() + "\\" + getpass.getuser() + "</b></font></td>""<td width=18%><font size=""3.5 face=""Cambria color=""green""><b>Operating System:</b></font></td>"" \
             ""<td width=32%><font size=""3.5 face=""Cambria color=""brown><b>" + platform.platform() + "</b></font></td></tr>"
    html_file.write( message )

    # Write Excel version - & EDGE Version
    message = "<tr><td width=20%><font size=""3.5 face=""Cambria color=""green><b>Excel Version:</b></font></td>"" \
    ""<td width=30%><font size=""3.5 face=""Cambria color=""brown><b>"+" " +"</b></font></td>"" \
    ""<td width=18%><font size=""3.5 face=""Cambria color=""green><b>SDK Version/Build:</b></font></td>"" \
    ""<td width=32%><font size=""3.5 face=""Cambria color=""brown><b>" + " " + "</b></font></td></tr>"

    html_file.write( message )

    # Write Total TC - & Execution start time
    message = "<tr><td width=20%><font size=""3.5 face=""Cambria color=""green><b>No. of Test Cases:</b></font></td>"" \
    ""<td width=30%><font size=""3.5 face=""Cambria color=""brown><b>" + str(config.total_testcase_count) + "</b></font></td>"" \
    ""<td width=18%><font size=""3.5 face=""Cambria color=""green><b>Execution Started At:</b></font></td>"" \
    ""<td width=32%><font size=""3.5 face=""Cambria color=""brown><b>" + str(config.first_tc_start_time) + "</b></font></td>""</tr></table>"

    html_file.write( message )

    message = "<table border=1 width=100%><tr><td width=20%><font size=" "3.5 face=""Cambria color="\
              "green><b>Remaining Execution Time: " +"Add Remain Time here"+ " </b></font></td></tr></table>"

    html_file.write( message )

    message = "<meta http-equiv=""refresh content=""150""><table border=""1"" width=100%>""<tr>" \
    "<th width=10%><font size=""2.8 face=""Cambria color=""blue" "><b> Sl No - Time </b></font></th>" \
    "<th width=15%><font size=""2.8 face=""Cambria color=""blue""><b> Test Case Id </b></font></th>" \
    "<th width=25%><font size=""2.8 face=""Cambria color=""blue""><b> Test Case Description </b></font> </th>" \
    "<th width=9%><font size=""2.8 face=""Cambria color=""blue""><b> Expected Time </b></font> </th>" \
    "<th width=9%><font size=""2.8 face=""Cambria color=""blue""><b> Actual Time in Sec </b></font></th>" \
    "<th width=32%><font size=""2.8 face=""Cambria color=""blue><b> Execution Remarks </b></font></th></tr>"

    html_file.write( message )

    html_file.close()

#########################################################################################################################################
# Fucntion to write Body of html page.
def html_body():
    f = open( config.html_report_path, "r" )
    contents = f.readlines()
    f.close()
    font_color = "Black"

    font_color = "Green" if config.tc_result == "PASS" else "Red" if config.tc_result == "FAIL" else "Grey" if config.tc_result == "ABORT" else ""
    config.tc_slno = config.tc_slno + 1
    strTemp = str(config.tc_slno) + "/" + str(config.total_testcase_count) +" - " +  str(time.strftime("%I:%M:%S" " %p"))
    html_line = "<tr><td><font size=2.8 face=Cambria color=""" + '"' + font_color +'"' + ">" + strTemp +\
                "</font></td>"+"<td><font size=2.8 face=Cambria color=""" + '"' + font_color +'"' + ">" + config.testcase_id + "</font></td>"

    # #html_line = html_line + "<td><font size=2.8 face=Cambria color="""+ '"' + font_color +'"' + ">" \
    #           + config.test_description + "</font></td><td><font size=2.8 face=Cambria color=""" '"' + font_color +'"' + ">" \
    #           + str(config.exp_execution_time) + "</font></td><td><font size=2.8 face=Cambria color=""" '"' + font_color +'"' + ">" \
    #           + str(config.tc_execution_time)  +"</font></td><td><font size=2.8 face=Cambria color=""" '"' + font_color +'"' + ">"

    html_line = html_line + "<td><font size=2.8 face=Cambria color=""" + '"' + font_color + '"' + ">" + \
        config.test_description + "</font></td><td><font size=2.8 face=Cambria color=""" '"' + font_color + '"' + ">" +\
       " " + "</font></td><td><font size=2.8 face=Cambria color=""" '"' + font_color + '"' + ">" + \
        str(config.tc_execution_time ) + "</font></td><td><font size=2.8 face=Cambria color=""" '"' + font_color + '"' + ">"

    html_line = html_line + "<p>" +config.tc_remark + "</P>"
    # if config.tc_result == "PASS":
    #     html_line = html_line + "<p>" + config.tc_remark + "</P>"
    # else:
    #     #html_line = html_line + "<p>" + ','.join(config.tc_remark) + "</P>"

    contents.insert( config.result_row_number , html_line )
    html_file = open( config.html_report_path, 'w' )
    contents = "".join( contents )
    html_file.write( contents )
    html_file.close()

    if config.tc_result == "PASS":
        config.total_pass = config.total_pass+1
    elif config.tc_result == "FAIL":
        config.total_fail = config.total_fail+1
    elif config.tc_result == "ABORT":
        config.total_abort = config.total_abort+1



##############################################################################################################################################

# Fucntion to write footer of html page.
def html_footer():
    #config.end_time = config.end_time + config.tc_execution_time
    f = open( config.html_report_path, "r" )
    contents = f.readlines()
    f.close()
    message = "</table><table border=1 width=100%><tr><td width = 20%><font size=3.5 face=Cambria>""Total No. of Test Cases Executed""</font></td>""<td width = 30%><font size=3.5 face=Cambria color=blue>" \
              + str(config.tc_slno) + "/" +str(config.total_testcase_count)+"</font></td>"
    message = message + "<td width = 18%><font size=3.5 face=Cambria>Total Execution Time</font></td><td width = 32%><font size=3.5 face=Cambria color=blue>" \
               + str(config.total_tc_execution_time) +"</font></td></tr>"
    message = message + "<tr><td width = 20%><font size=3.5 face=Cambria>Total Pass</font></td><td width = 30%><font size=3.5 face=Cambria color=blue>" \
            + str(config.total_pass)+  "</font></td><td><font size=3.5 face=Cambria>Total Fail</font></td><td width=32%><font size=3.5 face=Cambria color=blue>" \
              +str(config.total_fail) + "</font></td></tr>"
    message = message + "<tr><td width = 20%><font size=3.5 face=Cambria>Total Aborted</font></td><td width = 30%><font size=3.5 face=Cambria color=blue>" \
              +str(config.total_abort)+ "</font></td><td><font size=3.5 face=Cambria>Execution Ended At</font></td><td  width=32%><font size=3.5 face=Cambria color=blue>" \
               + str(config.last_tc_end_time) + "</font></td></tr>"

   # get_test_status()
    #print config.bln_critical_error_found
    if config.bln_critical_error_found == False:
        if config.bln_sucess == True:
            message = message + "<tr ><td colspan=4><font size=5 face=Cambria color=green><center> Execution Completed Successfully. </center></font></td></tr>"
        else:
            message = message + "<tr ><td colspan=4><font size=5 face=Cambria color=gray><center> Execution manually aborted!</center></font></td></tr>"


    else:
        message = message + "<tr ><td colspan=4><font size=5 face=Cambria color=red><center> Execution gracefully terminated. </center></font></td></tr>"
        message = message +"<tr ><td colspan=4><font size=3 face=Cambria color=red><center>" + "UNEXPECTED INTRUPTION" + "</center></font></td></tr>"

    message = message + "</table></body>"
   # print message
    contents.insert( config.result_row_number , message )
    html_file = open( config.html_report_path, 'w' )
    contents = "".join( contents )
    html_file.write( contents )
    html_file.close()

def call_full_report():
    html_header()
    html_body()
    html_footer()







