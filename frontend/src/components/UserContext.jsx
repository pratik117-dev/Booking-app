import React, { createContext, useState } from 'react';

export const UserContext = createContext();

export const UserProvider = ({ children }) => {
  const [user, setUser] = useState(null); // <-- FIX: capital U

  return (
    <UserContext.Provider value={{ user, setUser }}> {/* <-- FIX */}
      {children}
    </UserContext.Provider>
  );
};
