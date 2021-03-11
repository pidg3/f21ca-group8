import { ChatLogger } from '../chatLogger';
import { AppState } from '../appState';
import { expect } from 'chai';

describe('Stub function', () => {
  it('instantiates without error', () => {
    const testAppState = new AppState();
    const testChatLogger = new ChatLogger(testAppState);
  });

  it('returns previous logs', () => {
    const testAppState = new AppState();
    const testChatLogger = new ChatLogger(testAppState);
    testChatLogger.logDirect('hi');
    testChatLogger.logDirect('ey up');
    testChatLogger.logDirect('yo');
    expect(testChatLogger.getMessageHistory(3)).to.eql(['hi', 'ey up', 'yo']);
    expect(testChatLogger.getMessageHistory(2)).to.eql(['ey up', 'yo']);
    expect(testChatLogger.getMessageHistory(1)).to.eql(['yo']);
  });

  it('limits the number of previous logs stored', () => {
    const testAppState = new AppState();
    const testChatLogger = new ChatLogger(testAppState, 2);
    testChatLogger.logDirect('hi');
    testChatLogger.logDirect('ey up');
    testChatLogger.logDirect('yo');
    expect(testChatLogger.getMessageHistory(3)).to.eql(['ERROR: can only request up to 2 log messages']);
    expect(testChatLogger.getMessageHistory(2)).to.eql(['ey up', 'yo']);
    expect(testChatLogger.getMessageHistory(1)).to.eql(['yo']);
  });

});