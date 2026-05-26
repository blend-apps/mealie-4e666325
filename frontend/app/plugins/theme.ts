export interface ThemeConfig {
  lightPrimary: string;
  lightAccent: string;
  lightSecondary: string;
  lightSuccess: string;
  lightInfo: string;
  lightWarning: string;
  lightError: string;
  darkPrimary: string;
  darkAccent: string;
  darkSecondary: string;
  darkSuccess: string;
  darkInfo: string;
  darkWarning: string;
  darkError: string;
}

let __cachedTheme: ThemeConfig | undefined;

async function fetchTheme(): Promise<ThemeConfig | undefined> {
  const route = "/api/app/about/theme";

  try {
    const response = await fetch(route);
    const data = await response.json();
    return data as ThemeConfig;
  }
  catch {
    return undefined;
  }
}

export default defineNuxtPlugin(async (nuxtApp) => {
  nuxtApp.hook("vuetify:before-create", async ({ vuetifyOptions }) => {
    let theme = __cachedTheme;
    if (!theme) {
      theme = await fetchTheme();
      __cachedTheme = theme;
    }
    vuetifyOptions.theme = {
      defaultTheme: nuxtApp.$config.public.useDark ? "dark" : "light",
      variations: {
        colors: ["primary", "accent", "secondary", "success", "info", "warning", "error", "background"],
        lighten: 3,
        darken: 3,
      },
      themes: {
        light: {
          dark: false,
          colors: {
            primary: theme?.lightPrimary ?? "#212121",
            accent: theme?.lightAccent ?? "#424242",
            secondary: theme?.lightSecondary ?? "#616161",
            success: theme?.lightSuccess ?? "#4F4F4F",
            info: theme?.lightInfo ?? "#757575",
            warning: theme?.lightWarning ?? "#9E9E9E",
            error: theme?.lightError ?? "#000000",
          },
        },
        dark: {
          dark: true,
          colors: {
            primary: theme?.darkPrimary ?? "#FAFAFA",
            accent: theme?.darkAccent ?? "#E0E0E0",
            secondary: theme?.darkSecondary ?? "#BDBDBD",
            success: theme?.darkSuccess ?? "#9E9E9E",
            info: theme?.darkInfo ?? "#757575",
            warning: theme?.darkWarning ?? "#BDBDBD",
            error: theme?.darkError ?? "#FFFFFF",
            background: "#1E1E1E",
            surface: "#1E1E1E",
          },
        },
      },
    };
  });
});
