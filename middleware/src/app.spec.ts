import { giveMeFood } from './app';
import { expect } from 'chai';
describe('Stub function', () => {
  it('should return Gravy Peas', () => {
    const result = giveMeFood();
    expect(result).to.equal('Gravy Peas');
  });
});
