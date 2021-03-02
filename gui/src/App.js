import React from "react";
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link
} from "react-router-dom";
import UserView from './UserView';
import AdminView from './AdminView';


export default function App() {
    return (
        <Router>
            <div>
                <Switch>
                    <Route path="/admin">
                        <AdminView />
                    </Route>
                    <Route path="/">
                        <UserView />
                    </Route>
                </Switch>
            </div>
        </Router>
    );
}
