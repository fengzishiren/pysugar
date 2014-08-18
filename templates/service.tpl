/**
 *
 * @author %(author)s
 * @version %(version)s
 *
 * %(date)s
 */
@Service
public class %(bean_name)sService {

    @Resource
    private %(bean_name)sDao %(var_name)sDao;

    public List<%(bean_name)sInfo> get%(bean_name)sList(Map<String, Object> params) {
    	return %(var_name)sDao.get%(bean_name)sList(params);
    }

    public int delete%(bean_name)s(Map<String, Object> params) {
        return %(var_name)sDao.delete%(bean_name)s(params);
    }

    public int update%(bean_name)s(Map<String, Object> params) {
        return %(var_name)sDao.update%(bean_name)s(params);
    }
    
    
    public int add%(bean_name)s(Map<String, Object> params) {
        return %(var_name)sDao.add%(bean_name)s(params);
    }

}
