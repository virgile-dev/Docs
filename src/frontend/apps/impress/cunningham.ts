const config = {
  themes: {
    default: {
      theme: {
        font: {
          sizes: {
            ml: '0.938rem',
            xl: '1.50rem',
            t: '0.6875rem',
            s: '0.75rem',
            h1: '2.2rem',
            h2: '1.7rem',
            h3: '1.37rem',
            h4: '1.15rem',
            h5: '1rem',
            h6: '0.87rem',
          },
          weights: {
            thin: 100,
            extrabold: 800,
            black: 900,
          },
        },
        spacings: {
          '0': '0',
          none: '0',
        },
      },
    },
    dsfr: {
      theme: {
        colors: {
          'primary-100': '#f5f5fe',
          'primary-150': '#F4F4FD',
          'primary-200': '#ececfe',
          'primary-300': '#e3e3fd',
          'primary-400': '#cacafb',
          'primary-500': '#6a6af4',
          'primary-600': '#000091',
          'primary-700': '#272747',
          'primary-800': '#21213f',
          'primary-900': '#1c1a36',
          'secondary-100': '#fee9ea',
          'secondary-200': '#fedfdf',
          'secondary-300': '#fdbfbf',
          'secondary-400': '#e1020f',
          'secondary-500': '#c91a1f',
          'secondary-600': '#5e2b2b',
          'secondary-700': '#3b2424',
          'secondary-800': '#341f1f',
          'secondary-900': '#2b1919',
          'greyscale-000': '#ffffff',
          'greyscale-100': '#eeeeee',
          'greyscale-200': '#e5e5e5',
          'greyscale-300': '#e1e1e1',
          'greyscale-400': '#dddddd',
          'greyscale-500': '#cecece',
          'greyscale-600': '#7b7b7b',
          'greyscale-700': '#666666',
          'greyscale-800': '#2a2a2a',
          'greyscale-900': '#1e1e1e',
          'success-text': '#1f8d49',
          'success-100': '#dffee6',
          'success-200': '#b8fec9',
          'success-300': '#88fdaa',
          'success-400': '#3bea7e',
          'success-500': '#1f8d49',
          'success-600': '#18753c',
          'success-700': '#204129',
          'success-800': '#1e2e22',
          'success-900': '#19281d',
          'info-text': '#0078f3',
          'info-100': '#f4f6ff',
          'info-200': '#e8edff',
          'info-300': '#dde5ff',
          'info-400': '#bdcdff',
          'info-500': '#0078f3',
          'info-600': '#0063cb',
          'info-700': '#f4f6ff',
          'info-800': '#222a3f',
          'info-900': '#1d2437',
          'warning-text': '#d64d00',
          'warning-100': '#fff4f3',
          'warning-200': '#ffe9e6',
          'warning-300': '#ffded9',
          'warning-400': '#ffbeb4',
          'warning-500': '#d64d00',
          'warning-600': '#b34000',
          'warning-700': '#5e2c21',
          'warning-800': '#3e241e',
          'warning-900': '#361e19',
          'danger-text': '#e1000f',
          'danger-100': '#fef4f4',
          'danger-200': '#fee9e9',
          'danger-300': '#fddede',
          'danger-400': '#fcbfbf',
          'danger-500': '#e1000f',
          'danger-600': '#c9191e',
          'danger-700': '#642727',
          'danger-800': '#412121',
          'danger-900': '#3a1c1c',
        },
        font: {
          families: {
            accent: 'Marianne',
            base: 'Marianne',
          },
        },
        logo: {
          src: '/assets/logo-gouv.svg',
          widthHeader: '110px',
          widthFooter: '220px',
          alt: 'Gouvernement Logo',
        },
      },
      components: {
        alert: {
          'border-radius': '0',
          'background-color': 'var(--c--theme--colors--greyscale-000)',
        },
        button: {
          'medium-height': '48px',
          'border-radius': '0',
          primary: {
            background: {
              color: 'var(--c--theme--colors--primary-600)',
              'color-hover': '#1212ff',
              'color-active': '#2323ff',
            },
            color: '#ffffff',
            'color-hover': '#ffffff',
            'color-active': '#ffffff',
          },
          'primary-text': {
            background: {
              'color-hover': 'var(--c--theme--colors--primary-100)',
              'color-active': 'var(--c--theme--colors--primary-100)',
            },
            'color-hover': 'var(--c--theme--colors--primary-text)',
          },
          secondary: {
            background: {
              'color-hover': '#F6F6F6',
              'color-active': '#EDEDED',
            },
            border: {
              color: 'var(--c--theme--colors--primary-600)',
              'color-hover': 'var(--c--theme--colors--primary-600)',
            },
            color: 'var(--c--theme--colors--primary-600)',
          },
          'tertiary-text': {
            background: {
              'color-hover': 'var(--c--theme--colors--primary-100)',
            },
            'color-hover': 'var(--c--theme--colors--primary-text)',
          },
        },
        datagrid: {
          header: {
            color: 'var(--c--theme--colors--primary-600)',
            size: 'var(--c--theme--font--sizes--s)',
          },
          body: {
            'background-color': 'transparent',
            'background-color-hover': '#F4F4FD',
          },
          pagination: {
            'background-color': 'transparent',
            'background-color-active': 'var(--c--theme--colors--primary-300)',
          },
        },
        'forms-datepicker': {
          'border-radius': '0',
        },
        'forms-fileuploader': {
          'border-radius': '0',
        },
        'forms-input': {
          'background-color': 'var(--c--theme--colors--greyscale-100)',
          'border-radius': '0',
          'border-color': 'var(--c--theme--colors--greyscale-900)',
          'border-width': '0 0 2px 0',
          'border-color--focus': '#0974F6',
          'border-color--hover': 'var(--c--theme--colors--greyscale-900)',
          'label-color--focus':
            'var(--c--components--forms-labelledbox--label-color--small)',
        },
        'forms-textarea': {
          'background-color': 'var(--c--theme--colors--greyscale-100)',
          'border-radius': '0',
          'border-color': 'var(--c--theme--colors--greyscale-900)',
          'border-width': '0 0 2px 0',
          'border-color--focus': '#0974F6',
          'border-color--hover': 'var(--c--theme--colors--greyscale-900)',
          'label-color--focus':
            'var(--c--components--forms-labelledbox--label-color--small)',
        },
        'forms-select': {
          'background-color': 'var(--c--theme--colors--greyscale-100)',
          'border-radius': '0',
          'border-color': 'var(--c--theme--colors--greyscale-900)',
          'border-width': '0 0 2px 0',
          'border-color--focus': '#0974F6',
          'border-color--hover': 'var(--c--theme--colors--greyscale-900)',
          'label-color--focus':
            'var(--c--components--forms-labelledbox--label-color--big)',
        },
        'forms-switch': {
          'accent-color': '#2323ff',
        },
        'forms-checkbox': {
          'accent-color': '#2323ff',
        },
      },
    },
    openDesk: {
      theme: {
        colors: {
          'primary-100': '#F7F5FF',
          'primary-200': '#ECE7FE',
          'primary-300': '#DCD2FE',
          'primary-400': '#C8B9FD',
          'primary-500': '#8E75FA',
          'primary-600': '#7051FA',
          'primary-700': '#571EFA',
          'primary-800': '#4519C2',
          'primary-900': '#341291',
          'secondary-100': '#EDFDFB',
          'secondary-200': '#BFF9F2',
          'secondary-300': '#71EFE1',
          'secondary-400': '#00E6CC',
          'secondary-500': '#00A896',
          'secondary-600': '#008A7B',
          'secondary-700': '#006C60',
          'secondary-800': '#00564D',
          'secondary-900': '#004039',
        },
        font: {
          families: {
            accent: 'Open Sans',
            base: 'Marianne',
          },
        },
      },
      components: {
        button: {
          'medium-height': '48px',
          'border-radius': '8px',
          primary: {
            background: {
              color: 'var(--c--theme--colors--primary-700)',
              'color-hover': 'var(--c--theme--colors--primary-900)',
              'color-active': 'var(--c--theme--colors--primary-900)',
            },
            color: '#ffffff',
            'color-hover': '#ffffff',
            'color-active': '#ffffff',
          },
          'primary-text': {
            background: {
              'color-hover': 'var(--c--theme--colors--primary-100)',
              'color-active': 'var(--c--theme--colors--primary-100)',
            },
            'color-hover': 'var(--c--theme--colors--primary-text)',
          },
          secondary: {
            background: {
              'color-hover': '#F6F6F6',
              'color-active': '#EDEDED',
            },
            border: {
              color: 'var(--c--theme--colors--primary-600)',
              'color-hover': 'var(--c--theme--colors--primary-600)',
            },
            color: 'var(--c--theme--colors--primary-600)',
          },
          'tertiary-text': {
            background: {
              'color-hover': 'var(--c--theme--colors--primary-100)',
            },
            'color-hover': 'var(--c--theme--colors--primary-text)',
          },
        },
      },
    },
  },
};

export default config;
