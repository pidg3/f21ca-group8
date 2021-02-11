import Fastify, { FastifyInstance, RouteShorthandOptions } from 'fastify';

const server: FastifyInstance = Fastify({
  logger: true
});

const opts: RouteShorthandOptions = {
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

server.get('/ping', opts, async (request, reply) => {
  return { ping: 'OK!' };
});

const start = async () => {
  try {
    await server.listen(process.env.PORT || 3000, '127.0.0.1');

  } catch (err) {
    server.log.error(err);
    process.exit(1);
  }
};
start();
