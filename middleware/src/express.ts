import express from 'express';
import cors from 'cors';
import { v4 as uuidv4 } from 'uuid';

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

    // TODO: need to actually use the new UUID, won't touch sockets.ts for now
    // to avoid a merge conflict
    app.post('/resetState', (req: any, res: any) => {
        const updatedAlanaUUID = uuidv4();
        state.alanaUUID = updatedAlanaUUID;
        state.waitingForFirstMessage = true;
        res.send(`Alana UUID set: ${updatedAlanaUUID}`);
    });



    app.listen(PORT, () => {
        console.log(`⚡️[server]: Server is running at port ${PORT}`);
    });
};

export default start;