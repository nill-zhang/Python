from nose.tools import *
from example.employee import Employee

def setup():
    
    print "Setting up...."

def test_init():
    
    sfzhang = Employee('sfzhang',29,5500,"16th floor B21",1.76,1004)
    assert_is_instance(sfzhang, Employee)
    assert_greater(sfzhang.age, 20)
    assert_equal(sfzhang.name, "sfzhang")
    assert_less_equal(sfzhang.employeeid, 2000)
    assert_is_none(sfzhang.ranking)
    assert_not_in("c++", sfzhang.skills)
    assert_regexp_matches("^[0-9]+", sfzhang.office)
    assert_true(len(sfzhang.attendance) == 0)

def test_get_ranking():
    
    # test case is independent, you have to instantiate another instance
    sfzhang = Employee('sfzhang',30,3000,"16th floor B21",1.86,1005)
    sfzhang.get_ranking()
    assert_is(sfzhang.ranking, 'intermediate')
    xlyang = Employee('xlyang', 29, 4500, "15th floor A23", 1.55, 998)
    assert_less(xlyang.height, 1.60)
    xlyang.get_ranking()
    assert_not_in('senior', xlyang.ranking)
    

def test_origin():
    
    sfzhang = Employee('sfzhang',3,1000,"1st floor B21",1.56,5)
    assert(sfzhang.origin('China') == "international")
    assert_in("citi",xlyang.origin('Canada'))

def test_add_skills():
    
    
    qshu = Employee('qshu',30,3000,"16th floor B21",1.86,1005)
    qshu.add_skills(['python','ansible','linux','network'])
    assert_list_equal(qshu.skills, ['python','ansible','linux','network'])
    assert_in('python', qshu.skills)
 
def test_add_attendance():
    
    sfzhang = Employee('shaofeng zhang',18,4030,"12nd floor B21",1.73,15)
    sfzhang.add_attendance({'Jan':28,'Feb':29})
    assert_dict_contains(sfzhang.attendance,{'Feb':29})
    xlyang = Employee('XUELIAN YANG', 28, 4100, "8th floor C3", 1.65, 3098)
    assert_dict_equal(xlyang.attendance,{})

def tear_down():
    print "Tearing down...."

