import { Button } from '@openfun/cunningham-react';
import React, { Fragment, useState, useRef, useEffect } from 'react';
import { useTranslation } from 'react-i18next';
import { useUpdateDoc } from '../../doc-management/api/useUpdateDoc';
import { KEY_DOC, KEY_LIST_DOC } from '../../doc-management/api';
import { useToastProvider, VariantType } from '@openfun/cunningham-react';

import { Box, Card, StyledLink, Text } from '@/components';
import { useCunninghamTheme } from '@/cunningham';
import {
  Doc,
  Role,
  currentDocRole,
  useTransRole,
} from '@/features/docs/doc-management';
import { ModalVersion, Versions } from '@/features/docs/doc-versioning';
import { useDate } from '@/hook';

import { DocTagPublic } from './DocTagPublic';
import { DocToolBox } from './DocToolBox';

import styled from 'styled-components';

const EditableText = styled.div<{ $isEditing: boolean }>`
  font-size: 1.5em;
  font-weight: bold;
  cursor: pointer;
  display: inline-block;
  padding: 1px 3px;
  margin: 0 16px 0 4px;
  border: 1px solid transparent;
  border-radius: 4px;
  background-color: ${(props) => (props.$isEditing ? '#fff' : 'transparent')};

  &:hover {
    border-color: ${(props) => (props.$isEditing ? 'transparent' : '#ccc')};
    border-style: ${(props) => (props.$isEditing ? 'solid' : 'dashed')};
  }

  &:focus {
    outline: none;
    box-shadow: ${(props) =>
      props.$isEditing ? '0 0 0 2px rgba(0,123,255,.25)' : 'none'};
  }
`;

interface DocHeaderProps {
  doc: Doc;
  versionId?: Versions['version_id'];
}

export const DocHeader = ({ doc, versionId }: DocHeaderProps) => {
  const { colorsTokens } = useCunninghamTheme();
  const { t } = useTranslation();
  const { formatDate } = useDate();
  const transRole = useTransRole();
  const [isModalVersionOpen, setIsModalVersionOpen] = useState(false);
  const [isEditing, setIsEditing] = useState(false);
  const [title, setTitle] = useState(doc.title);
  const editableRef = useRef<HTMLDivElement>(null);
  const { toast } = useToastProvider();

  const { mutate: updateDoc } = useUpdateDoc({
    onSuccess: () => {
      setIsEditing(false);
      toast(t('Document title updated successfully'), VariantType.SUCCESS);
    },
    listInvalideQueries: [KEY_DOC, KEY_LIST_DOC],
  });

  const handleTitleChange = (e: React.FormEvent<HTMLDivElement>) => {
    setTitle(e.currentTarget.textContent || '');
  };

  const handleTitleSubmit = () => {
    if (title !== doc.title) {
      updateDoc({ id: doc.id, title });
    }
    setIsEditing(false);
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter') {
      e.preventDefault();
      handleTitleSubmit();
    }
  };

  useEffect(() => {
    if (isEditing && editableRef.current) {
      editableRef.current.focus();

      // Create a new range
      const range = document.createRange();
      const selection = window.getSelection();

      // Set the range to where the user clicked
      if (selection && selection.rangeCount > 0) {
        range.setStart(selection.anchorNode!, selection.anchorOffset);
        range.setEnd(selection.anchorNode!, selection.anchorOffset);
      } else {
        // If no selection, default to end of text
        range.selectNodeContents(editableRef.current);
        range.collapse(false);
      }

      // Apply the range
      selection?.removeAllRanges();
      selection?.addRange(range);
    }
  }, [isEditing]);

  return (
    <>
      <Card
        $margin="small"
        aria-label={t('It is the card information about the document.')}
      >
        <Box $padding="small" $direction="row" $align="center">
          <StyledLink href="/">
            <Text
              $isMaterialIcon
              $theme="primary"
              $size="2rem"
              $css={`&:hover {background-color: ${colorsTokens()['primary-100']}; };`}
              $hasTransition
              $radius="5px"
              $padding="tiny"
            >
              home
            </Text>
          </StyledLink>
          <Box
            $width="1px"
            $height="70%"
            $background={colorsTokens()['greyscale-100']}
            $margin={{ horizontal: 'small' }}
          />
          <Box $gap="1rem" $direction="row" $align="center">
            <EditableText
              ref={editableRef}
              $isEditing={isEditing}
              contentEditable={isEditing}
              onInput={handleTitleChange}
              onBlur={handleTitleSubmit}
              onKeyDown={handleKeyDown}
              onClick={() => !isEditing && setIsEditing(true)}
              suppressContentEditableWarning={true}
              title={isEditing ? '' : t('Edit')} // Add this line
            >
              {doc.title}
            </EditableText>
            {versionId && (
              <Button
                onClick={() => {
                  setIsModalVersionOpen(true);
                }}
                size="small"
              >
                {t('Restore this version')}
              </Button>
            )}
          </Box>
          <DocToolBox doc={doc} />
        </Box>
        <Box
          $direction="row"
          $align="center"
          $css="border-top:1px solid #eee"
          $padding={{ horizontal: 'big', vertical: 'tiny' }}
          $gap="0.5rem 2rem"
          $justify="space-between"
          $wrap="wrap"
        >
          <Box $direction="row" $align="center" $gap="0.5rem 2rem" $wrap="wrap">
            <DocTagPublic doc={doc} />
            <Text $size="s" $display="inline">
              {t('Created at')} <strong>{formatDate(doc.created_at)}</strong>
            </Text>
            <Text $size="s" $display="inline" $elipsis $maxWidth="60vw">
              {t('Owners:')}{' '}
              <strong>
                {doc.accesses
                  .filter(
                    (access) => access.role === Role.OWNER && access.user.email,
                  )
                  .map((access, index, accesses) => (
                    <Fragment key={`access-${index}`}>
                      {access.user.email}{' '}
                      {index < accesses.length - 1 ? ' / ' : ''}
                    </Fragment>
                  ))}
              </strong>
            </Text>
          </Box>
          <Text $size="s" $display="inline">
            {t('Your role:')}{' '}
            <strong>{transRole(currentDocRole(doc.abilities))}</strong>
          </Text>
        </Box>
      </Card>
      {isModalVersionOpen && versionId && (
        <ModalVersion
          onClose={() => setIsModalVersionOpen(false)}
          docId={doc.id}
          versionId={versionId}
        />
      )}
    </>
  );
};
