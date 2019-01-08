/**
 * Responds to any HTTP request.
 *
 * @param {!express:Request} req HTTP request context.
 * @param {!express:Response} res HTTP response context.
 */

exports.publish_widget = (req, res) => {
  
  try {
    
    const uuid = require('uuid');
  
    // Import client library
    const PubSub = require('@google-cloud/pubsub');
  
    // obtain GCP project ID from reserved environment variable
    const projectId = process.env.GCP_PROJECT;
    
    // Create a client that uses Application Default Credentials (ADC)
    const pubsub = new PubSub({
       projectId: projectId,
    }); 
    
    // obtain topic from environment variable
    const topic = pubsub.topic(process.env.TOPIC);
  
    // obtain a publisher
    const publisher = topic.publisher();

    // const data = Buffer.from(req.body);
    const widget_content = req.body.widget_content;
    const widget_uid = uuid.v4();

    const data = Buffer.from(JSON.stringify(
                   {widget_content : widget_content, 
                    widget_uid : widget_uid })); 
  
    // publish using a Promise
    publisher.publish(data).then(function(messageId) {
        let responseMessage = { widget_uid : widget_uid, message_id : messageId }
        res.status(200).send(JSON.stringify(responseMessage));
    });
    
  }
  catch(e) {
       console.log(e.stack());
       let responseMessage = { widget_id : "", message_id : "" }
       res.status(500).send(JSON.stringify(responseMessage));
  }
  
};

