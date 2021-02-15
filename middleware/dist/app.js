"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const express_1 = __importDefault(require("./express"));
const sockets_1 = __importDefault(require("./sockets"));
// This pattern is very nasty but will do for now...
let state = {
    externalBotUrl: ''
};
express_1.default(state);
sockets_1.default(state);
//# sourceMappingURL=app.js.map