import re

def retro_camel(ctx, cmdline):
    """'hello world' -> 'helloWorld'"""
    action = ctx.copy_last_action()
    num_words = int(cmdline)
    
    last_words = "".join(ctx.last_words(count=num_words))
    action.prev_replace = last_words

    # Split and build camelCase
    words = [w for w in re.split(r'[\s_]+', last_words) if w]
    if words:
        transformed = words[0].lower() + "".join(w.capitalize() for w in words[1:])
    else:
        transformed = last_words

    action.text = transformed
    action.word = transformed
    action.prev_attach = True
    return action

def retro_pascal(ctx, cmdline):
    """'hello world' -> 'HelloWorld'"""
    action = ctx.copy_last_action()
    num_words = int(cmdline)
    
    last_words = "".join(ctx.last_words(count=num_words))
    action.prev_replace = last_words

    # Split and build PascalCase
    words = [w for w in re.split(r'[\s_]+', last_words) if w]
    transformed = "".join(w.capitalize() for w in words) if words else last_words

    action.text = transformed
    action.word = transformed
    action.prev_attach = True
    return action

def retro_snake(ctx, cmdline):
    """'Hello World' -> 'hello_world'"""
    action = ctx.copy_last_action()
    num_words = int(cmdline)
    
    last_words = "".join(ctx.last_words(count=num_words))
    action.prev_replace = last_words

    # Split and join with underscore, then lowercase
    words = [w for w in re.split(r'[\s_]+', last_words) if w]
    transformed = "_".join(w.lower() for w in words) if words else last_words

    action.text = transformed
    action.word = transformed
    action.prev_attach = True

    return action

def retro_screaming(ctx, cmdline):
    """'hello world' -> 'HELLO_WORLD'"""
    action = ctx.copy_last_action()
    num_words = int(cmdline)
    
    last_words = "".join(ctx.last_words(count=num_words))
    action.prev_replace = last_words

    # Split and join with underscore, then uppercase
    words = [w for w in re.split(r'[\s_]+', last_words) if w]
    transformed = "_".join(w.upper() for w in words) if words else last_words

    action.text = transformed
    action.word = transformed
    action.prev_attach = True
    return action

def retro_dot(ctx, cmdline):
    """'hello world' -> 'hello.world'"""
    action = ctx.copy_last_action()
    num_words = int(cmdline)
    
    last_words = "".join(ctx.last_words(count=num_words))
    action.prev_replace = last_words

    words = [w for w in re.split(r'[\s.]+', last_words) if w]
    transformed = ".".join(words)

    action.text = transformed
    action.word = transformed
    action.prev_attach = True
    return action

def retro_dot_pascal(ctx, cmdline):
    """'hello world' -> 'Hello.World'"""
    action = ctx.copy_last_action()
    num_words = int(cmdline)
    
    last_words = "".join(ctx.last_words(count=num_words))
    action.prev_replace = last_words

    words = [w for w in re.split(r'[\s.]+', last_words) if w]
    transformed = ".".join(w.capitalize() for w in words) if words else last_words

    action.text = transformed
    action.word = transformed
    action.prev_attach = True
    return action

def retro_dot_camel(ctx, cmdline):
    """'hello world' -> 'Hello.World'"""
    action = ctx.copy_last_action()
    num_words = int(cmdline)
    
    last_words = "".join(ctx.last_words(count=num_words))
    action.prev_replace = last_words

    words = [w for w in re.split(r'[\s.]+', last_words) if w]
    transformed = ".".join(w.lower() if i == 0 else w.capitalize() for i, w in enumerate(words)) if words else last_words

    action.text = transformed
    action.word = transformed
    action.prev_attach = True
    return action

def retro_doublecolon(ctx, cmdline):
    """'hello world' -> 'hello::world'"""
    action = ctx.copy_last_action()
    num_words = int(cmdline)
    
    last_words = "".join(ctx.last_words(count=num_words))
    action.prev_replace = last_words

    words = [w for w in re.split(r'[\s:]+', last_words) if w]
    transformed = "::".join(words)

    action.text = transformed
    action.word = transformed
    action.prev_attach = True
    return action

def retro_doublecolon_pascal(ctx, cmdline):
    """'hello world' -> 'hello::world'"""
    action = ctx.copy_last_action()
    num_words = int(cmdline)
    
    last_words = "".join(ctx.last_words(count=num_words))
    action.prev_replace = last_words

    words = [w for w in re.split(r'[\s:]+', last_words) if w]
    transformed = "::".join(w.capitalize() for w in words) if words else last_words

    action.text = transformed
    action.word = transformed
    action.prev_attach = True
    return action

def retro_title(ctx, cmdline):
    action = ctx.copy_last_action()
    num_words = int(cmdline)
    last_words = "".join(ctx.last_words(count=num_words))

    transformed = last_words.title()
    
    action.prev_replace = last_words
    action.text = transformed
    action.word = transformed
    action.prev_attach = True
    return action

def retro_upper(ctx, cmdline):
    action = ctx.copy_last_action()
    num_words = int(cmdline)
    last_words = "".join(ctx.last_words(count=num_words))

    transformed = last_words.upper()
    
    action.prev_replace = last_words
    action.text = transformed
    action.word = transformed
    action.prev_attach = True
    return action

def retro_lower(ctx, cmdline):
    action = ctx.copy_last_action()
    num_words = int(cmdline)
    last_words = "".join(ctx.last_words(count=num_words))

    transformed = last_words.lower()
    
    action.prev_replace = last_words
    action.text = transformed
    action.word = transformed
    action.prev_attach = True
    return action

def retro_kebab(ctx, cmdline):
    """'Hello World' -> 'hello-world'"""
    action = ctx.copy_last_action()
    num_words = int(cmdline)
    
    last_words = "".join(ctx.last_words(count=num_words))
    action.prev_replace = last_words

    # Split by whitespace or underscores, then join with hyphens
    words = [w for w in re.split(r'[\s_]+', last_words) if w]
    transformed = "-".join(w.lower() for w in words) if words else last_words

    action.text = transformed
    action.word = transformed
    action.prev_attach = True
    return action
