package {{cookiecutter.package_prefix}};

import java.io.IOException;
import java.lang.invoke.MethodHandles;

import org.apache.solr.common.SolrInputDocument;
import org.apache.solr.common.util.NamedList;
import org.apache.solr.core.SolrCore;
import org.apache.solr.request.SolrQueryRequest;
import org.apache.solr.request.SolrRequestInfo;
import org.apache.solr.response.SolrQueryResponse;
import org.apache.solr.update.AddUpdateCommand;
import org.apache.solr.update.CommitUpdateCommand;
import org.apache.solr.update.processor.UpdateRequestProcessor;
import org.apache.solr.update.processor.UpdateRequestProcessorFactory;
import org.apache.solr.util.plugin.SolrCoreAware;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class $$URP_CLASS_NAMEFactory extends UpdateRequestProcessorFactory implements SolrCoreAware {

	private static final Logger logger = LoggerFactory.getLogger(MethodHandles.lookup().lookupClass());

	@Override
	public void init(NamedList args) {
		super.init(args);
	}

	@Override
	public void inform(SolrCore core) {

	}

	@Override
	public $$URP_CLASS_NAME getInstance(SolrQueryRequest req, SolrQueryResponse rsp,
			UpdateRequestProcessor next) {
		return new $$URP_CLASS_NAME(req, rsp, next);
	}

	class $$URP_CLASS_NAME extends UpdateRequestProcessor {
		private final SolrQueryRequest req;
		private final SolrQueryResponse rsp;
		public $$URP_CLASS_NAME(SolrQueryRequest req, SolrQueryResponse rsp,
				UpdateRequestProcessor next) {
			super(next);
			this.req = req;
			this.rsp = rsp;
		}

		@Override
		public void processAdd(AddUpdateCommand cmd) throws IOException {
			logger.info("Processing the following update: " + cmd);

			SolrInputDocument doc = cmd.getSolrInputDocument();
			doc.addField("timestamp_dt", SolrRequestInfo.getRequestInfo().getNOW());

			super.processAdd(cmd);
		}

		@Override
		public void processCommit(CommitUpdateCommand cmd) throws IOException {
			logger.info("Processing a commit command: " + cmd);
			super.processCommit(cmd);
		}

	}
}