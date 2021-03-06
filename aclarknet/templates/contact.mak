<%inherit file="root.mak"/>

<%block name="style">
    .footer {
        color: white;
    }
</%block>

<%block name="title">
    <title>ACLARK.NET, LLC &mdash; Contact</title>
</%block>

<%block name="nav">
    <li><a href="/">Home</a></li>
    <li><a href="/clients">Clients</a></li>
    <li><a href="/services">Services</a></li>
    <li><a href="/team">Team</a></li>
    <li><a href="/testimonials">Testimonials</a></li>
    <li class="active"><a href="/contact">Contact</a></li>
</%block>

<%block name="jumbotron">
    <h1>Contact</h1>
    <h2>The best way to contact us is via the email address, phone number or website form below.</h2>
    <div class="row">
        <div class="span12">
            <p class="lead"><i class="icon-envelope icon-2x pull-left"></i><i class="icon-phone icon-2x pull-left"></i>The Python programming language and open source software in general provide tremendous opportunities to businesses, but often require an expert to take advantage of. We provide services that empower individuals and organizations to benefit from such opportunities, and we would love to help you! Please contact us to schedule a time to discuss your needs. We look forward to working with you.</p>
            <p class="contact">
                ACLARK.NET, LLC <br />
                Bethesda, MD USA <br />
                Email: <a href="mailto:sales@aclark.net">sales@aclark.net</a> <br />
                Phone: 301-312-5236
            </p>
            <hr />
            <div style="text-align: center ; margin: auto; width: 740px;">
                <% error = request.session.pop_flash('errors') %>
                <% success = request.session.pop_flash() %>
                % if error:
                    <div class="alert alert-block alert-error">${error[0]}</div>
                % endif
                % if success:
                    <div class="alert alert-block alert-success">${success[0]}</div>
                % endif
                ${form|n}
            </div>
        </div>
    </div>
</%block>
