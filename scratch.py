import os
import threading

# def func1():
#     os.system("pytest -v -s --html=report_pnr.html -m pnr Tests/Positive_Tests/Test_Resource_Booking/test_RoomBooking.py --self-contained-html --capture=sys -rP -rF")
#     os.system("pytest -v -s Tests/test_send_email.py")
#     os.system("pytest -v -s --html=report_prs.html -m prs Tests/Positive_Tests/Test_Resource_Booking/test_RoomBooking.py --self-contained-html --capture=sys -rP -rF")
#     os.system("pytest -v -s Tests/test_send_email.py")
 
# def func2():
#     os.system("pytest -v -s --html=report_pr.html -m pr Tests/Positive_Tests/Test_Resource_Booking/test_RoomBooking.py --self-contained-html --capture=sys -rP -rF")
#     os.system("pytest -v -s Tests/test_send_email.py")
#     os.system("pytest -v -s --html=report_prw.html -m prw Tests/Positive_Tests/Test_Resource_Booking/test_RoomBooking.py --self-contained-html --capture=sys -rP -rF")
#     os.system("pytest -v -s Tests/test_send_email.py")
 
# def func3():
#     os.system("pytest -v -s --html=report_prsc.html -m prsc Tests/Positive_Tests/Test_Resource_Booking/test_RoomBooking.py --self-contained-html --capture=sys -rP -rF")
#     os.system("pytest -v -s Tests/test_send_email.py")
#     os.system("pytest -v -s --html=report_pcnclb.html -m pcnclb Tests/Positive_Tests/Test_Resource_Booking/test_RoomBooking.py --self-contained-html --capture=sys -rP -rF")
#     os.system("pytest -v -s Tests/test_send_email.py")
 
# def func4():
#     os.system("pytest -v -s --html=report_misc.html -m misc Tests/Positive_Tests/Test_Resource_Booking/test_RoomBooking.py --self-contained-html --capture=sys -rP -rF")
#     os.system("pytest -v -s Tests/test_send_email.py")
    # os.system("pytest -v -s --html=report_hostrltd.html -m hostrltd Tests/Positive_Tests/Test_Resource_Booking/test_RoomBooking.py --self-contained-html --capture=sys -rP -rF")
    # os.system("pytest -v -s Tests/test_send_email.py")

def func1():
    os.system("pytest -v -s --html=report-live-bookinglogs.html Tests/Positive_Tests/test_BookingLogs.py --self-contained-html --capture=sys -rP -rF")
    os.system("pytest -v -s --html=report-live-workStatus.html Tests/Positive_Tests/test_WorkStatus.py --self-contained-html --capture=sys -rP -rF")
    os.system("pytest -v -s --html=report-live-healthStatus.html Tests/test_HealthStatus.py --self-contained-html --capture=sys -rP -rF")
    


if __name__ == "__main__":
    t1 = threading.Thread(target=func1)
    # t2 = threading.Thread(target=func2)
    # t3 = threading.Thread(target=func3)
    # t4 = threading.Thread(target=func4)

    t1.start()
    # t2.start()
    # t3.start()
    # t4.start()


    # t1.join()
    # t2.join()
    # t3.join()
    # t4.join()
