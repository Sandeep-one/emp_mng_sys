class Employee:

    def add(self, conn, cur, l):
        for i in range(4):
            l[i] = l[i].lower()

        try:
            querry = "INSERT INTO Employee( emp_fname, emp_lname, emp_pnum, emp_des, emp_dep, emp_Sal, emp_mngr_id, emp_begin_date ) VALUES(%s,%s,%s,%s,%s,%s,%s,curdate())"
            cur.execute(querry, [l[0], l[1], l[6], l[2], l[3], l[5], l[4]])
            print('      !!! Added Successfully !!!')
            conn.commit()

            return "Record Successfully Added"

        except Exception as e:
            conn.rollback()
            print('      !!!  Rollback !!!',e)
            return str(e)

    def remove(self, conn, cur, id, fnm, lnm):
        try:
            querry = "delete from employee where emp_id = %s and emp_fname = %s and emp_lname = %s"
            cur.execute(querry, [id, fnm, lnm])
            conn.commit()
            print('deleted')
            if cur.rowcount > 0:
                return 'Record Deleted'
            else:
                return 'No Record Found, Incorrect Values '

        except Exception as e:
            conn.rollback()
            print('      !!!  Rollback !!!', e)
            return str(e)

    def display(self, cur, b):
        try:
            d = dict()
            if b == 'all':
                querry = "select * from employee"
                cur.execute(querry)
            else:
                querry = "select * from employee where emp_des = %s"
                cur.execute(querry, [b])

            for i, j in enumerate(cur.fetchall()):
                d[i] = j

            return d

        except Exception as e:
            print('      !!!  NO DATA !!!')
            return str(e)
