pysugar
=========

功能：输入数据表库中表名称自动生成基于Spring、Mybatis的增删改查的Java代码


使用教程示例：
假设已经建好数据库mysite和表auth_user:
```sql
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
```

在settings.py中配置数据库信息如：
```python
DATABASE = {'host':'127.0.0.1',
            'port': 3306,
            'username': 'root',
            'password': 'root',
            'database': 'mysite'}
```
运行命令
```sh
python pysugar.py auth_user
```
运行结果:
输出文件如下

AuthUserInfo.java
```java
/**
 *
 * @author pysugar
 * @version 0.1
 *
 * 2014-07-23
 */
public class AuthUserInfo {
	private String username;
	private String firstName;
	private String lastName;
	private int isSuperuser;
	private String dateJoined;
	private String email;
	private int isStaff;
	private String lastLogin;
	private String password;
	private long id;
	private int isActive;
    public String getUsername() {
        return username;
    }
    public void setUsername(String username) {
        this.username = username;
    }
    public String getFirstName() {
        return firstName;
    }
    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }
    public String getLastName() {
        return lastName;
    }
    public void setLastName(String lastName) {
        this.lastName = lastName;
    }
    public int getIsSuperuser() {
        return isSuperuser;
    }
    public void setIsSuperuser(int isSuperuser) {
        this.isSuperuser = isSuperuser;
    }
    public String getDateJoined() {
        return dateJoined;
    }
    public void setDateJoined(String dateJoined) {
        this.dateJoined = dateJoined;
    }
    public String getEmail() {
        return email;
    }
    public void setEmail(String email) {
        this.email = email;
    }
    public int getIsStaff() {
        return isStaff;
    }
    public void setIsStaff(int isStaff) {
        this.isStaff = isStaff;
    }
    public String getLastLogin() {
        return lastLogin;
    }
    public void setLastLogin(String lastLogin) {
        this.lastLogin = lastLogin;
    }
    public String getPassword() {
        return password;
    }
    public void setPassword(String password) {
        this.password = password;
    }
    public long getId() {
        return id;
    }
    public void setId(long id) {
        this.id = id;
    }
	public int getIsActive() {
        return isActive;
    }
    public void setIsActive(int isActive) {
        this.isActive = isActive;
    }
}
```
AuthUserController.java
```java
/**
 *
 * @author pysugar
 * @version 0.1
 *
 * 2014-07-23
 */
@Controller
public class AuthUserController{
    private static Logger logger = Logger.getLogger(AuthUserController.class);

    @Resource
    private AuthUserService authUserService;

    @Resource
    private LoginService loginService;

    @RequestMapping(value = "/getAuthUserList")
    @ResponseBody
    public Object getStatisticsList(HttpServletRequest req) {
        return AuthUserService.getAuthUserList(null);
    }
    
    @RequestMapping(value = "/updateAuthUser")
    @ResponseBody
    public Object updateAuthUser(HttpServletRequest req) {
        
        return null;
    }

    @RequestMapping(value = "/delAuthUser")
    @ResponseBody
    public Object deleteAuthUser(HttpServletRequest req) {
        return null;
    }
    
    @RequestMapping(value = "/addAuthUser")
    @ResponseBody
    public Object addAuthUser(HttpServletRequest req) {
		
        return null;
    }
}


```
AuthUserService.java
```java
/**
 *
 * @author pysugar
 * @version 0.1
 *
 * 2014-07-23
 */
@Service
public class AuthUserService {

    @Resource
    private AuthUserDao authUserDao;

    public List<AuthUserInfo> getAuthUserList(Map<String, Object> params) {
           return AuthUserDao.getAuthUserList(params);
    }

    public int deleteAuthUser(Map<String, Object> params) {
        return AuthUserDao.deleteAuthUser(params);
    }

    public int updateAuthUser(Map<String, Object> params) {
        return AuthUserDao.updateAuthUser(params);
    }
    
    
    public int addAuthUser(Map<String, Object> params) {
        return AuthUserDao.addAuthUser(params);
    }

}

```

AuthUserDao.java
```java
/**
 *
 * @author pysugar
 * @version 0.1
 *
 * 2014-07-23
 */
@Repository
public interface AuthUserDao {

    /**
     * @return
     */
    public List<AuthUserInfo> getAuthUserList(Map<String, Object> params);

    /**
     * @param params
     */
    public int deleteAuthUser(Map<String, Object> params);

    /**
     * @param params
     */
    public int updateAuthUser(Map<String, Object> params);

    /**
     * @param params
     * @return
     */
    public int addAuthUser(Map<String, Object> params);

}

```
AuthUserDaoMapper.xml
```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="yxpay.ms.dao.AuthUserDao">
    <resultMap id="authUserMap" type="yxpay.ms.bean.AuthUserInfo">
        <result property="username" column="username" />
	<result property="firstName" column="first_name" />
	<result property="lastName" column="last_name" />
	<result property="isSuperuser" column="is_superuser" />
	<result property="dateJoined" column="date_joined" />
	<result property="email" column="email" />
	<result property="isStaff" column="is_staff" />
	<result property="lastLogin" column="last_login" />
	<result property="password" column="password" />
	<result property="id" column="id" />
	<result property="isActive" column="is_active" />
    </resultMap>
    
    
    <select id="getAuthUserList" parameterType="map" resultMap="authUserMap">
        select * from auth_user
    </select>
    

    <delete id="deleteAuthUser" parameterType="map">
        delete from auth_user
    </delete>
    

    <update id="updateAuthUser" parameterType="map">
        update auth_user 
        <set>
         username = #{username},
	first_name = #{firstName},
	last_name = #{lastName},
	is_superuser = #{isSuperuser},
	date_joined = #{dateJoined},
	email = #{email},
	is_staff = #{isStaff},
	last_login = #{lastLogin},
	password = #{password},
	id = #{id},
	is_active = #{isActive} 
        </set>
    </update>
    

    <insert id="addAuthUser" parameterType="map">
        insert into auth_user (username,first_name,last_name,is_superuser,date_joined,email,is_staff,last_login,password,id,is_active) values (#{username},#{firstName},#{lastName},#{isSuperuser},#{dateJoined},#{email},#{isStaff},#{lastLogin},#{password},#{id},#{isActive})
    </insert>
    
</mapper>
```


完
