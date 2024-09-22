import { Button } from '@openfun/cunningham-react';
import { useRouter } from 'next/navigation';
import React from 'react';
import { useTranslation } from 'react-i18next';

import { Box, Card } from '@/components';
import { useCreateDoc } from '@/features/docs/doc-management/';

import { DocsGrid } from './DocsGrid';

export const DocsGridContainer = () => {
  const { t } = useTranslation();
  const router = useRouter();

  const api = useCreateDoc({
    onSuccess: (doc) => {
      router.push(`/docs/${doc.id}`);
    },
  });

  const handleCreateDoc = () => {
    api.mutate({ title: t('New document') });
  };

  return (
    <Box $overflow="auto">
      <Card $margin="big" $padding="tiny">
        <Box $align="flex-end" $justify="center">
          <Button onClick={handleCreateDoc}>
            {t('Create a new document')}
          </Button>
        </Box>
      </Card>
      <DocsGrid />
    </Box>
  );
};
