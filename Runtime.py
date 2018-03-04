setTime = {}
setTime = wait2['setTime']
mulai = time.time() 

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d ชั่วโมง %02d นาที %02d วินาที' % (hours, mins, secs)



            elif msg.text.lower() == 'runtime':
                eltime = time.time() - mulai
                van = "ระยะเวลาการทำงานของบอท :\n"+waktu(eltime)
                cl.sendText(msg.to,van)
            
