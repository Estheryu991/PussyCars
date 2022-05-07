Last login: Sat May  7 16:12:08 on ttys008
todfuralle@MacBook-Air-von-Todfuralle ~ % ssh pi@192.168.88.225
pi@192.168.88.225's password: 
Linux vcar-x-03 5.10.103-v7+ #1529 SMP Tue Mar 8 12:21:37 GMT 2022 armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Sat May  7 14:46:04 2022 from 192.168.88.233

SSH is enabled and the default password for the 'pi' user has not been changed.
This is a security risk - please login as the 'pi' user and type 'passwd' to set a new password.

pi@vcar-x-03:~ $ ls
DeepPiCar  SunFounder_PiCar  SunFounder_PiCar-S  SunFounder_PiCar-V
pi@vcar-x-03:~ $ cd SunFounder_PiCar-S
pi@vcar-x-03:~/SunFounder_PiCar-S $ ls
docs  example  install_dependencies  LICENSE  maps  README.md  show
pi@vcar-x-03:~/SunFounder_PiCar-S $ cd example/
pi@vcar-x-03:~/SunFounder_PiCar-S/example $ ls
camera_detection.py       light_follower.py.save      line_follower.py                 test_light_module.py
camera_detection.py.save  light_follower.py.save.1    SunFounder_Light_Follower        test_line_module.py
__init__.py               light_follower.pyy          SunFounder_Line_Follower         test_ultrasonic_module.py
light_follower.py         light_with_obsavoidance.py  SunFounder_Ultrasonic_Avoidance  ultra_sonic_avoid.py
pi@vcar-x-03:~/SunFounder_PiCar-S/example $ nano light_follower.py
pi@vcar-x-03:~/SunFounder_PiCar-S/example $ pygk

-bash: k: command not found
pi@vcar-x-03:~/SunFounder_PiCar-S/example $ 
pi@vcar-x-03:~/SunFounder_PiCar-S/example $ 
pi@vcar-x-03:~/SunFounder_PiCar-S/example $ 
pi@vcar-x-03:~/SunFounder_PiCar-S/example $ nano light_follower.py


























  GNU nano 3.2                                          light_follower.py                                                    

                # Angle calculate
                if      lt_status_now == [0,1,0]:
                        step = 0
                elif lt_status_now == [1,1,0] or lt_status_now == [0,1,1]:
                        step = a_step
                elif lt_status_now == [1,0,0] or lt_status_now == [0,0,1]:
                        step = b_step
                
                # Direction calculate
                if      lt_status_now in ([0,1,0],[1,1,1]):
                        fw.turn(90)
                        bw.forward()
                        bw.speed = forward_speed
                # turn right
                elif lt_status_now in ([1,1,0],[1,0,0]):
                        fw.turn(90 - step)
                        bw.forward()
                        bw.speed = forward_speed
                # turn left
                elif lt_status_now in ([0,1,1],[0,0,1]):
                        fw.turn(90 + step)
                        bw.forward()
                        bw.speed = forward_speed
                # backward
                elif lt_status_now == [1,0,1]:
                        fw.turn(90)
                        bw.backward()
                        bw.speed = forward_speed
                # none of all above
                elif lt_status_now == [0,0,0]:
                        fw.turn(90)
                        bw.stop()

def stop():
        bw.stop()
        fw.turn_straight()

def move_straight(length):
        for i in range(length):
                fw.turn(100)
                bw.backward()

def curve(winkel, length):
        for i in range(length):
                bw.backward()
                fw.turn(winkel)

def kreis():
        for i in range(3):
                curve(80,200)
                move_straight(450)
        move_straight(150)
        curve(70,50)
        for i in range(4):
                curve(80,200)
                move_straight(450)

def stop():
        bw.stop()
        fw.turn_straight()

def move_straight(length):
        for i in range(length):
                fw.turn(100)
                bw.backward()

def curve(winkel, length):
        for i in range(length):
                bw.backward()
                fw.turn(winkel)

def kreis():
        for i in range(3):
                curve(80,200)
                move_straight(450)
        move_straight(150)
        curve(70,50)
        for i in range(4):
                curve(80,200)
                move_straight(450)

^G Get Help    ^O Write Out   ^W Where Is    ^K Cut Text    ^J Justify     ^C Cur Pos     M-U Undo       M-A Mark Text
^X Exit        ^R Read File   ^\ Replace     ^U Uncut Text  ^T To Spell    ^_ Go To Line  M-E Redo       M-6 Copy Text
