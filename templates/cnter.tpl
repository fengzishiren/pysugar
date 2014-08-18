/**
 *
 * @author %(author)s
 * @version %(version)s
 *
 * %(date)s
 */
@Controller
public class %(bean_name)sController{
    private static Logger logger = Logger.getLogger(%(bean_name)sController.class);

    @Resource
    private %(bean_name)sService %(var_name)sService;

    @RequestMapping(value = "/get%(bean_name)sList")
    @ResponseBody
    public Object get%(bean_name)sList(HttpServletRequest req) {
        return %(var_name)sService.get%(bean_name)sList(null);
    }
    
    @RequestMapping(value = "/update%(bean_name)s")
    @ResponseBody
    public Object update%(bean_name)s(HttpServletRequest req) {
        ParamPairs pairs = Params.create();
        %(var_name)sService.update%(bean_name)s(pairs);
        return null;
    }

    @RequestMapping(value = "/del%(bean_name)s")
    @ResponseBody
    public Object delete%(bean_name)s(HttpServletRequest req) {
    	ParamPairs pairs = Params.create();
     	%(var_name)sService.delete%(bean_name)s(pairs);
        return null;
    }
    
    @RequestMapping(value = "/add%(bean_name)s")
    @ResponseBody
    public Object add%(bean_name)s(HttpServletRequest req) {
		ParamPairs pairs = Params.create();
		%(var_name)sService.add%(bean_name)s(pairs);
        return null;
    }
}
