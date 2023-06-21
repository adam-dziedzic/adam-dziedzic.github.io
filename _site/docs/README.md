# Adam's comments/navigation through the data for the blog:

### General comments

This blog web page has a very unintuitive structure. The main configuration is
in: _config.yml - you can change your name, email, avatar, and other basic info.

Use command to build the website:

I also installed the wsd gem, as pointed
here: https://jekyllrb.com/docs/installation/windows/#auto-regeneration

`gem install wdm`

Build and serve the site locally:
```shell
bundle exec jekyll serve --host localhost --port 4000 --incremental --livereload --destination docs
```

Build the site for deployment:
```shell
jekyll build --destination docs
```

Ultimate command, never fails and rebuilds everything from scratch:

```shell
bundle exec jekyll serve --force_polling --livereload --trace --destination docs --incremental
```

On Windows:

```shell
bundle exec jekyll serve --force_polling --livereload --incremental --destination docs
```

Do Live reload:

```shell
bundle exec jekyll serve --port 5000 --incremental --livereload --destination docs
```

`--incremental` Incremental regeneration helps shorten build times by only
generating documents and pages that were updated since the previous build.

`--livereload` reload lively after every change

### Additional info:
1. The main style CSS sheet is: `_sass/style.scss`

### Coding, Deployment, Trouble Shooting

1. Add links to the titles of the talks.
1. If there is Uncaught ReferenceError: and something is not defined then there
   is a JavaScript library missing. Go to _sites and double click on index.html.
   Check the website locally. Open this _site/index.html in your web browser and
   inspect it. What is the error? It shows the exact line. For example, Chart
   was missing from a Chart.js JavaScript library.
2. The easiest way to deploy the webpage is to run `deploy.sh`. Deploy the
   static website to the `docs/` directory. The github pages are directed to
   serve from `docs/` folder. The commands are as follows:
   ```shell
    timestamp=$(date "+%Y-%m-%d-%H:%M:%S")
    git add *
    git commit -am "deploy at timestamp: ${timestamp}"
    git push origin source
   ``` 

3. Old version with a standard destination of building the static website to
   the `_site` folder:

   ```shell
   timestamp=`date "+%Y-%m-%d-%H:%M:%S"`
    mkdir docs
    cd docs
    cp -r ../_site/* .
    git add *
    cd ..
    git commit -am "deploy at timestamp: ${timestamp}"
    git push origin source
    rm -r docs
   ```

2. We cannot deploy this as it is directly to github pages because
   the `jekyll-scholar` is not enabled plugin officially on github. Check
   Gemfile to see the plugin and also `_plugins/ext.rb`. It has to be added to
   the `_plugins`, otherwise the `jekyll-scholar` does not work. To deploy the
   website you need to put index.html and all other files/folders from _sites in
   the main root branch. Maintain the .git folder! You have another folder
   code/adam-dziedzic.github.io-master which should contain the final deployment
   files. More
   about [deployment](https://github.com/randymorris/randymorris.github.com).
   ```shell
       git publish-website # which consists of the following steps
       git branch -D master
       git checkout -b master
       git filter-branch --subdirectory-filter _site/ -f
       git checkout source
       git push --all origin
   ```
   Other sources:
    - https://davidensinger.com/2013/04/deploying-jekyll-to-github-pages/
    - https://github.com/robwierzbowski/grunt-build-control
    - https://davidensinger.com/2013/07/automating-jekyll-deployment-to-github-pages-with-rake/
    -
3. Check if you can use /docs from git hub pages instead of copying the _sites
   folder.
4. Add the accordion from bootstrap for years of
   publications. https://getbootstrap.com/docs/4.3/components/collapse/
4. Learn the grid system in
   bootstrap: https://getbootstrap.com/docs/4.1/layout/grid/
7. Go through the tutorial on jekyll.
8. Read thoroughly the deployment for github pages.
9. Create the website for CaPC.
10. Add a section about coding with pointer to
    github: https://maruan.alshedivat.com/code/
10. Add your more personal website.
11. Add section about your past projects.
12. Add section with your best photos.
13. Buy domain for your family and create e-mail addresses for them.
14. Creating a custom 404 page for your GitHub Pages site
15. Change the colors of the buttons starting from the btn-info, which is green.
    Add blue, orange, red, etc.
16. Check Marcin Wachulski website.
17. The bacic templates for html pages are in `_layouts`.
18. `_includes` have the html pages - how to arrange stuff.
19. `_data/index` have the real data easily arranged, also `_data/landing.yml`.
20. To add blog posts, go to `_posts`.
21. CNAME file is for domain resolution between Google and GitHub.
22. `_config.yml` contains the basic and main information/data for the website.
23. Gemfile is important for plugins.
24. Update your CV. Add info about talks.
25. Change icons for projects: data loading & big dawg to more 'scientific'
    ones.
28. Add blog about PATE
29. Add blog about CaPC

### Blog

1. go to _data/blog.yml to add/drop blog categories (Blog, Html, Life, Python,
   C++, etc.)
2. Use only a single category per blog post.
3. go to blog/*.html (for example: blog/blog.html) to change how the blog posts
   are displayed.

### Stucture of the main page: Projects, About me, Contact, etc.

1. The order of the sections for the main page is in _data/landing.yml (you can
   reorder the section about procjects, for example, to be at the end of the
   main personal page).
2. To change any of the main sections (e.g. to add a project), go to the _
   data/index/projects.yml file.
3. If you want to change the html options, for example, for projects, go to: _
   includes/sections/projects.html.
4. If you add a new project, the image should be resized so that its height is
   200px.

# Other info:

## Jalpc. [![Analytics](https://ga-beacon.appspot.com/UA-73784599-1/welcome-page)](https://github.com/jarrekk/Jalpc)

[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php)
[![stable](http://badges.github.io/stability-badges/dist/stable.svg)](http://github.com/badges/stability-badges)
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badge/)

<https://jarrekk.github.io/Jalpc/>

<http://www.jarrekk.com>  -- Personal website

![Blog](https://github.com/jarrekk/Jalpc/raw/master/readme_files/Jalpc.png)

- [3 steps to setup this theme at your website!](#3-steps-to-setup-this-theme-at-your-website)
- [Features](#features)
    - [Index page](#index-page)
        - [`_data/*.yml`](#_datayml)
    - [Chart Skills](#chart-skills)
    - [Categories in blog page](#categories-in-blog-page)
    - [Pagination](#pagination)
    - [Page views counter](#page-views-counter)
    - [Multilingual Page](#multilingual-page)
    - [Web analytics](#web-analytics)
    - [Comment](#comment)
    - [Share](#share)
    - [Search engines](#search-engines)
    - [Compress CSS and JS files](#compress-css-and-js-files)
- [Put in a Jalpc Plug](#put-in-a-jalpc-plug)
- [Upgrading Jalpc](#upgrading-jalpc)
    - [Ensure there's an upstream remote](#ensure-theres-an-upstream-remote)
    - [Pull in the latest changes](#pull-in-the-latest-changes)
- [Todo](#todo)
- [Donate Jalpc](#donate-jalpc)
- [Wiki](#wiki)
- [Ad](#ad)

This is a simple, beautiful and swift theme for Jekyll. It's mobile first,
fluidly responsive, and delightfully lightweight.

If you're completely new to Jekyll, I recommend checking out the documentation
at <http://jekyllrb.com> or there's a tutorial by Smashing Magazine.

# 3 steps to setup this theme at your website!

Here is
a [document](https://jarrekk.github.io/Jalpc/html/2017/01/31/3-steps-to-setup-website-with-Jalpc.html)
of how to setup this theme with 3 steps and
a [wiki](https://github.com/jarrekk/Jalpc/wiki/How-to-add-posts) of how to add
posts. If you have any **questions** please ask me
at [GitHub Issues](https://github.com/jarrekk/Jalpc/issues).

# Features

## Index page

The index page is seprated into several sections and they are located
in `_includes/sections`,the configuration is in `_data/landing.yml` and
section's detail configuration is in `_data/*.yml`.

### `_data/*.yml`

These files are used to dynamically render pages, so you almost don't have to
edit *html files* to change your own theme, besides you can
use `jekyll serve --watch` to reload changes.

The following is mapping between *yml files* to *sections*.

* landing.yml ==> index.html
* index/language.yml ==> index.html
* index/careers.yml ==>  _includes/sections/career.html
* index/skills.yml ==>  _includes/sections/skills.html
* index/projects.yml ==>  _includes/sections/projects.html
* index/links.yml ==>  _includes/sections/links.html

This *yml file* is about blog page navbar

* blog.yml ==> _includes/header.html

The following is mapping between *yml files* to *donation*

* donation/donationlist.yml ==> blog/donate.html
* donation/alipay.yml ==>  blog/donate.html
* donation/wechat_pay.yml ==> blog/donate.yml

## Chart Skills

I use [Chart.js](http://www.chartjs.org/) to show skills, the type of skills'
chart is radar, if you want to custom, please read document of Chart.js and
edit **_includes/sections/skills.html** and **_data/index/skills.yml**.

## Categories in blog page

In blog page, we categorize posts into several categories by url, all category
pages use same template html file - `_includes/category.html`.

For example: URL is `http://127.0.0.1:4000/python/`. In `_data/blog.yml`, we
define this category named `Python`, so in `_includes/category.html` we get this
URL(/python/) and change it to my category(Python), then this page are posts
about **Python**. The following code is about how to get url and display
corresponding posts in  `_includes/category.html`.

```html

<div class="row">
    <div class="col-lg-12 text-center">
        <div class="navy-line"></div>
        {% assign category = page.url | remove:'/' | capitalize %}
        {% if category == 'Html' %}
        {% assign category = category | upcase %}
        {% endif %}
        <h1>{{ category }}</h1>
    </div>
</div>
<div class="wrapper wrapper-content  animated fadeInRight blog">
    <div class="row">
        <ul id="pag-itemContainer" style="list-style:none;">
            {% assign counter = 0 %}
            {% for post in site.categories[category] %}
            {% assign counter = counter | plus: 1 %}
            <li>
```

## Pagination

The pagination in jekyll is not very perfect,so I use front-end web method,there
is
a [blog](http://www.jarrekk.com/html/2016/06/04/jekyll-pagination-with-jpages.html)
about the method and you can refer
to [jPages](http://luis-almeida.github.io/jPages).

## Page views counter

Many third party page counter platforms are too slow,so I count my website page
view myself,the javascript file
is [static/js/count.min.js](https://github.com/jarrekk/jalpc_jekyll_theme/blob/gh-pages/static/js/count.min.js) ([static/js/count.js](https://github.com/jarrekk/jalpc_jekyll_theme/blob/gh-pages/static/js/count.js)),the
backend API is written with flask on [Vultr VPS](https://www.vultr.com/), detail
code please
see [ztool-backhend-mongo](https://github.com/Z-Tool/ztool-backhend-mongo).

## Multilingual Page

The landing page has multilingual support with the [i18next](http://i18next.com)
plugin.

Languages are configured in the `_data/index/language.yml` file.

> Not everyone needs this feature, so I make it very easy to remove it, just clear content in file `_data/language.yml` and folder `static/locales/`.

About how to custom multilingual page, please
see [wiki](https://github.com/jarrekk/Jalpc/wiki/Multilingual-Page).

## Web analytics

I use [Google analytics](https://www.google.com/analytics/)
and [GrowingIO](https://www.growingio.com/) to do web analytics, you can choose
either to realize it,just register a account and replace id in `_config.yml`.

## Comment

I use [Disqus](https://disqus.com/) to realize comment. You should set
disqus_shortname and get public key and then, in `_config.yml`, edit the disqus
value to enable Disqus.

## Share

I use [AddToAny](https://www.addtoany.com/) to share my blog on other social
network platform. You can go to this website to custom your share buttons and
paste code at `_includes/share.html`.

![share](https://github.com/jarrekk/Jalpc/raw/master/readme_files/share.png)

## Search engines

I use javascript to realize blog search,you can double click `Ctrl` or click the
icon at lower right corner of the page,the detail you can got to
this [repository](https://github.com/androiddevelop/jekyll-search). Just use it.

![search](https://github.com/jarrekk/Jalpc/raw/master/readme_files/search.gif)

## Compress CSS and JS files

All CSS and JS files are compressed at `/static/assets`.

I use [UglifyJS2](https://github.com/mishoo/UglifyJS2)
, [clean-css](https://github.com/jakubpawlowicz/clean-css) to compress CSS and
JS files, customised CSS files are at `_sass` folder which is feature
of [Jekyll](https://jekyllrb.com/docs/assets/). If you want to custom CSS and JS
files, you need to do the following:

1. Install [NPM](https://github.com/npm/npm) then install **UglifyJS2** and **
   clean-css**: `npm install -g uglifyjs; npm install -g clean-css`, then
   run `npm install` at root dir of project.
2. Compress script is **build.js**
3. If you want to add or remove CSS/JS files, just edit **build/build.js**
   and **build/files.conf.js**, then run `npm run build` at root dir of project,
   link/src files will use new files.

OR

Edit CSS files at `_sass` folder.

# Put in a Jalpc Plug

If you want to give credit to the Jalpc theme with a link to my personal
website <http://www.jarrekk.com>, that'd be awesome. No worries if you don't.

# Upgrading Jalpc

Jalpc is always being improved by its users, so sometimes one may need to
upgrade.

## Ensure there's an upstream remote

If `git remote -v` doesn't have an upstream listed, you can do the following to
add it:

```
git remote add upstream https://github.com/jarrekk/Jalpc.git
```

## Pull in the latest changes

```
git pull upstream gh-pages
```

There may be merge conflicts, so be sure to fix the files that git lists if they
occur. That's it!

# Todo

- [ ] `jekyll server --watch` mode need to use original CSS/JS files
- [ ] User can customise index page's section title.
- [x] Non-github projects also have links.
- [ ] Add some custom color themes for selection(Nav bar, background, words,
  dominant hue).

# Donate Jalpc

If this project let you enjoy your blog time, you can give me a cup of coffee :)

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://paypal.me/jarrekk)

# Wiki

* [Multilingual Page](https://github.com/jarrekk/Jalpc/wiki/Multilingual-Page)
* [How to add posts](https://github.com/jarrekk/Jalpc/wiki/How-to-add-posts)
* [Change Log](https://github.com/jarrekk/Jalpc/wiki/Change-Log)
* [Contributors](https://github.com/jarrekk/Jalpc/wiki/Contributors)
* [Thanks to the following](https://github.com/jarrekk/Jalpc/wiki/Thanks-to-the-following)

# Ad

[Jalpc-A](https://github.com/Jack614/Jalpc-A): another Jekyll theme written
by [AngularJS](https://angularjs.org/).

