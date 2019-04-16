import eel


@eel.expose
def getdata(start_station, destination, date):
	data = Get_tickets (start_station, destination, date).tickets_info
	result = ""
	for d in data:
		html = '''<div class = "content">
        <ul class="tickets_info">
            <li class="first_li">%(train_code)s</li>
            <li>%(from_station)s</li>
            <li>%(to_station)s</li>
            <li>%(start_time)s</li>
            <li>%(arrive_time)s</li>
            <li>%(used_time)s</li>
            <li>%(business_seat)s</li>
            <li>%(first_seat)s</li>
            <li>%(second_seat)s</li>
            <li>%(gjrw)s</li>
            <li>%(dw)s</li>
            <li>%(yw)s</li>
            <li>%(rz)s</li>
            <li>%(yz)s</li>
            <li>%(wz)s</li>
            <li>%(qt)s</li>
            <li class="last_li">%(remark)s</li>
        </ul>
        <ul class="price">
                <li class="first_li"></li>
                <li></li>
                <li></li>
                <li></li>
                <li></li>
                <li></li>
                <li>%(business_price)s</li>
                <li>%(first_seat_price)s</li>
                <li>%(second_seat_price)s</li>
                <li>%(gjrw_seat_price)s</li>
                <li>%(dw_seat_price)s</li>
                <li>%(yw_seat_price)s</li>
                <li>%(rz_seat_price)s</li>
                <li>%(yz_seat_price)s</li>
                <li>%(wz_seat_price)s</li>
                <li>%(dw_seat_price)s</li>
                <li class="last_li"></li>
        </ul>
        </div>     ''' % d
		result += html
	return result

if __name__ == '__main__':
	eel.init("D:\123456")
	eel.start("12306.html")