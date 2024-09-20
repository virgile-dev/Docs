import { Crisp } from 'crisp-sdk-web';
import { useEffect } from 'react';

import { User } from '@/core';

const isCrispConfigured = (): boolean => {
  return typeof window !== 'undefined' && !!window.$crisp;
};

export const initializeSupportSession = (user: User) => {
  if (!isCrispConfigured()) {
    return;
  }
  Crisp.setTokenId(user.id);
  Crisp.user.setEmail(user.email);
};

export const terminateSupportSession = () => {
  if (!isCrispConfigured()) {
    return;
  }
  Crisp.session.reset();
};

/**
 * Configure Crisp chat for real-time support across all pages.
 */
export const useSupport = () => {
  useEffect(() => {
    const CRISP_WEBSITE_ID = process.env.NEXT_PUBLIC_CRISP_WEBSITE_ID;

    if (!CRISP_WEBSITE_ID) {
      console.warn('Crisp Website ID is not set');
      return;
    }
    if (isCrispConfigured()) {
      return;
    }
    Crisp.configure(CRISP_WEBSITE_ID);
  }, []);

  return null;
};
