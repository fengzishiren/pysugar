/**
 *
 * @author %(author)s
 * @version %(version)s
 *
 * %(date)s
 */
@Repository
public interface %(bean_name)sDao {

    public List<%(bean_name)sInfo> get%(bean_name)sList(Map<String, Object> params);

    public int delete%(bean_name)s(Map<String, Object> params);

    public int update%(bean_name)s(Map<String, Object> params);

    public int add%(bean_name)s(Map<String, Object> params);

}
