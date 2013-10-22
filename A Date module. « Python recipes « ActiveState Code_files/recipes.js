/* Copyright (c) 2009 ActiveState Software Inc.
 *
 * JS module for code.activestate.com.
 */

var Recipes = {
    /**
     * Hijaxes all components in the sidebar. Used on recipe detail page.
     */
    hijax_sidebar: function() {
        // hijax sidebar forms
        $('form.remove-from-set, form.tag-remove, form#add_tags, ' +
          'form#add_to_set, form#add_requires, form.require-remove')
            .ajaxForm({dataType: 'json', success: Recipes.process_ajax});
        // machine tag toggle button
        $('.machine_tag_toggle').click(function() {
            Recipes.toggle_machine_tags();
            return false;
        });
    },
    /**
     * Shows, hides or toggles visibility of machine tags. Used on recipe detail
     * page.
     *
     * @param show {bool} Specifies whether machine tags should be toggled (null),
     *      visible (true) or hidden (false).
     */
    toggle_machine_tags: function(show) {
        if (show == null) {
            show = !($(".machinetags").is(':visible'));
        }
        if (show) {
            $('.machinetags').show();
            $('.machine_tag_toggle > span').html('&#x25bc; Hide');
        } else {
            $('.machinetags').hide();
            $('.machine_tag_toggle > span').html('&#x25b6; Show');
        }
    },
    /**
     * Handles ajax responses from the server. Used on recipe detail page. See
     * _ajax_success and _ajax_fail on the server side.
     */
    process_ajax: function(data) {
        if(data.redirect) {
            location.href = data.redirect;
            return;
        }
        if(data.sidebar_html) {
            Recipes.loadSidebar(data.sidebar_html);
        }
        if(data.score_html) {
            $('#recipe_scorevote').replaceWith(data.score_html);
            Recipes.hijax_voting();
        }
        if(data.message) {
            Recipes.show_message(data.message,
                                 data.message_timeout,
                                 data.message_undo);
        }
    },
    /**
     * Refreshes the sidebar with new data from the server.
     * @see #process_ajax
     */
    loadSidebar: function(htmlData) {
        var sidebar = $("#as_sidebar_dynamic");
        // save state
        var showMachinetags = $(".machinetags", sidebar).is(':visible');
        // replace sidebar
        sidebar.empty().html(htmlData);
        // restore state
        Recipes.hijax_sidebar();
        // restore state
        Recipes.toggle_machine_tags(showMachinetags);
    },
    /**
     * Hijaxes the voting area on recipe detail pages.
     * @see #process_ajax
     */
    hijax_voting: function() {
        $('#recipe_scorevote form').submit(function() {
            $('button', this).addClass("waiting");
            $.post(this.action, {'in': in_param, 'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]', this).val()}, Recipes.process_ajax, 'json')
            return false;
        });
        $('#recipe_scorevote button.voted.upvote').hover(
            function () { $(this).text('\u2716'); },
            function () { $(this).text('\u25b2'); }
        );
        $('#recipe_scorevote button.voted.downvote').hover(
            function () { $(this).text('\u2716'); },
            function () { $(this).text('\u25bc'); }
        );
    },
    /**
     * ID of the message hide timer
     */
    show_message_timeout: undefined,
    /**
     * @param message {String} The message to show.
     * @param show_for_ms {Number} Optional. The number of milliseconds for
     *      for which to show the message. Default is 0, meaning the message
     *      doesn't timeout.
     * @param undo_data {object} Optional. Contains information for the undo
     *      button in the properties `url` and `fields`. */
    show_message: function(message, show_for_ms /*=0 */, undo_data) {
        if (typeof(show_for_ms) === undefined) { show_for_ms = 0; }
        var messagebar = $('#as_messagebar');
        $('.message', messagebar).text(message);
        if (undo_data == undefined) {
            $('.message-undo', messagebar).hide();
        } else {
            var undo_form = $('.message-undo', messagebar).find("form");
            undo_form.attr("action", undo_data.url);
            undo_form.remove("input[type='hidden']");
            $.each(undo_data.fields, function(k,v) {
                $("<input type='hidden'/>").attr("name", k).attr("value", v)
                                           .appendTo(undo_form);
            });
            $('.message-undo', messagebar).show();
        }
        if(typeof(this.show_message_timeout) !== undefined) {
            // clear older timeout
            window.clearTimeout(this.show_message_timeout);
            this.show_message_timeout = undefined;
        }
        messagebar.slideDown(150);
        if (show_for_ms > 0) {
            this.show_message_timeout = window.setTimeout(function() {
                $('#as_messagebar').slideUp(150);
                Recipes.show_message_timeout = undefined;
            }, show_for_ms);
        }
    },
    /**
     * Scrolls down the document to the first error.
     */
    scroll_to_errors: function() {
        var errorlists = $('ul.errorlist').get();
        if(errorlists.length>0) errorlists[0].scrollIntoView();
    },
    /**
     * Hightlights the comment just created (the last comment in fact). Used on
     * detail pages.
     */
    highlight_last_comment: function () {
        if (document.location.hash == "#clast") {
            $("#comments > div:last")
                .effect("highlight", {}, 3000)
                .get(0).scrollIntoView(false);
        }
    },
    choose_langvers: function() {
        var lang = $('select#id_lang').val();
        var oldInputs = $('input[name=langvers]');
        var oldValues = $.map(oldInputs, function(input) { return $(input).val() });
        oldInputs.remove();
        $('li#as_langvers').remove();
        
        if(!(lang in langvers))
            return;
        var versions = langvers[lang];
        var majors = [];
        for(var i in versions) {
            if($.inArray(versions[i].major, majors) == -1) {
                majors.push(versions[i].major);
            }
        }
        majors.sort();
        var htmlLi = $('<li id="as_langvers"><label>Minimum Language Version(s):</label></li>');
        for(var i in majors) {
            var htmlSelect = $('<select name="langvers"><option value="">-----</option></select>');
            for(var j in versions) {
                if(versions[j].major == majors[i]) {
                    htmlSelect.append('<option value="' + versions[j].id + '">' + versions[j].name + '</option>');
                }
            }
            htmlSelect.appendTo(htmlLi);
        }
        htmlLi.append('<div class="secondary">Select the mininum language version(s) that your recipe code works with. ' +
                      'This is optional but can help users search for recipes appropriate for the version they use.</div>');
        htmlLi.insertAfter("li:has(#id_lang)");
        if(oldValues.length)
            $("select[name=langvers]").val(oldValues);
    },
    /**
     * Sets up the auto-complete handlers for the requirements field. Used on the
     * recipe add/edit pages.
     */
    setup_requires_autocomplete: function() {
        $('input#id_requires').autocomplete([], {
            multiple: true,
            multipleSeparator: " "
        }).focus(function(){
            switch($('#id_lang option:selected').val()) {
            case 'python':
                var python_re = /^(?:\s*import\s+([\w.]+(?:\s?,\s?[\w.]+)*)|\s*from\s+([\w.]+))/gm;
                var code = $('textarea#id_code').val();
                var result = [];
                var match;
                while(match = python_re.exec(code)) {
                    if(match[1])
                        result = result.concat(match[1].split(/\s*,\s*/));
                    if(match[2])
                        result.push(match[2]);
                };
                break;
            default:
                result = [];
            }
            $('input#id_requires').setOptions({
                data: result
            });
        });
    },
    /**
     * Sets up the copy button and makes it visible. Used on recipe detail page.
     */
    setup_copy_button: function(prefix, suffix) {
        if(!FlashDetect.versionAtLeast(9))
            return;
        ZeroClipboard.setMoviePath('/static/zeroclipboard/ZeroClipboard.swf');
        var clip = new ZeroClipboard.Client();
        $("#clipboard_container").css("display", "inline-block");
        var text = prefix + $("td.code pre").text() + suffix;
        if(navigator.platform == "Win32") {
            // modify line endings for windows
            text = text.replace(/\n/g, "\r\n");
        }
        clip.setText(text);
        clip.glue("clipboard_button", "clipboard_container");
        clip.addEventListener('onComplete', function(event) {
            Recipes.show_message("Copied.", 2000);
        });
    },
    
    /** Load the given site theme.
     *
     * @param name {string} The site theme name. If null, then no theme
     *      will be loaded -- but it will still unload an existing theme.
     */
    load_site_theme: function(name) {
        // Unload any existing theme stuff, if any.
        try {
            $("#site_theme_css").remove();
        } catch(ex) {
            /* TODO: what are error conds here */
        }
        if (name) {
            // Load the new theme.
            var head = document.getElementsByTagName('head')[0];
            var css_href = "/static/themes/" + name + "/theme.css";
            $(document.createElement('link')) 
                .attr({type: 'text/css', href: css_href, rel: 'stylesheet',
                    media: 'screen', 'id': 'site_theme_css'}) 
                .appendTo(head);
        }
    },
    tagbar_data: null,
    /** Sets up the tag bar, used on recipe list pages.
     *
     */
    setup_tagbar: function(data) {
        // setup autocomplete
        $('#tagbar input').autocomplete("/recipes/autocompletetags/", {
            cacheLength: 50,
            delay: 200,
            multiple: true,
            multipleSeparator: " "
        });
        // setup validation
        this.tagbar_data = data;
        var trytags = function(new_tags) {
            var newData = $.extend({}, Recipes.tagbar_data,
                                   {tags_str: Recipes.tagbar_data.tags_str + '+' + new_tags.replace(/ /g, '+')});
            $.getJSON('/recipes/ajaxquery/', newData, function(data) {
                if(data.success) window.location.assign(data.url);
                else Recipes.show_message(data.message);
            });
        };
        $("#tagbar form").submit(function(evt) {
            trytags($("#tagbar form input").val());
            return false;
        });
    }
};
