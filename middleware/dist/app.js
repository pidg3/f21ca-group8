"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
Object.defineProperty(exports, "__esModule", { value: true });
const fastify_1 = require("fastify");
const server = fastify_1.default({
    logger: true
});
const opts = {
    schema: {
        response: {
            200: {
                type: 'object',
                properties: {
                    resp: {
                        type: 'string'
                    }
                }
            }
        }
    }
};
server.get('/ping', opts, (request, reply) => __awaiter(void 0, void 0, void 0, function* () {
    return { resp: 'it worked!' };
}));
server.get('/new', opts, (request, reply) => __awaiter(void 0, void 0, void 0, function* () {
    return { resp: 'circleci working!' };
}));
server.get('/', opts, (request, reply) => __awaiter(void 0, void 0, void 0, function* () {
    return { resp: 'root!' };
}));
const start = () => __awaiter(void 0, void 0, void 0, function* () {
    try {
        yield server.listen(process.env.PORT || 3000, '127.0.0.1');
    }
    catch (err) {
        server.log.error(err);
        process.exit(1);
    }
});
start();
//# sourceMappingURL=app.js.map