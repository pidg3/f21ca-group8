import express from 'express';
import cors from 'cors';

// rest of the code remains same
const app = express();
const PORT = process.env.PORT || 8090;

const start = (state:any) => {

    app.use(cors());
    app.use(express.json());
    app.get('/ping', (req: any, res: any) => res.send('OK!'));

    app.post('/setExternalBotUrl', (req: any, res: any) => {
        state.externalBotUrl = req.body.externalBotUrl;
        res.send('External URL updated: ' + req.body.externalBotUrl);
    });

    app.listen(PORT, () => {
        console.log(`⚡️[server]: Server is running at https://localhost:${PORT}`);
    });
};

export default start;