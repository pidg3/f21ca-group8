import express from 'express';
import cors from 'cors';

const app = express();

// Remember, this is defined manually as an env variable in EB
// (which overrides the confusing, default/hidden 8080 value, which is 
// ... reserved for web socket)
const PORT = process.env.PORT || 8090;

const start = (state:any) => {

    app.use(cors());
    app.use(express.json());
    app.get('/', (req: any, res: any) => res.send('OK!'));

    app.post('/setExternalBotUrl', (req: any, res: any) => {
        state.externalBotUrl = req.body.externalBotUrl;
        res.send('External URL updated: ' + req.body.externalBotUrl);
    });

    app.listen(PORT, () => {
        console.log(`⚡️[server]: Server is running at port ${PORT}`);
    });
};

export default start;