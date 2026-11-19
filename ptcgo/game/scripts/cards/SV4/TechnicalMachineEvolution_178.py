from ptcgo.game.data_utils import PokemonToolCardDef, Attack, Ability, Triggers
from ptcgo.game.attributes import Rarities, AttrID, PokemonTypes
from ptcgo.game.card_effects.trainers import discard_tool_at_end_of_turn
from ptcgo.game.content.definitions import evolves_from

async def _evolution_attack(ctx):
    bench = ctx.my_bench()
    if not bench:
        return
    targets = await ctx.choose_cards(
        bench, 2, minimum=0,
        prompt="Choose up to 2 Benched Pokémon to evolve")
    for target in targets:
        logic_name = target.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)

        def eligible(card, logic_name=logic_name):
            return bool(logic_name) and evolves_from(
                getattr(card, "archetype_id", None) or "", logic_name)

        picks = await ctx.search_deck(
            eligible, count=1, minimum=0,
            prompt="Choose an Evolution card for this Pokémon")
        if picks:
            await ctx.evolve_pokemon(target, picks[0])
    await ctx.shuffle_deck()


card = PokemonToolCardDef(
    guid="a2868773-689d-5240-8338-3ed47dee6f79",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TechnicalMachineEvolution.Name",
    display_name="Technical Machine: Evolution",
    searchable_by=["Technical Machine: Evolution", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=178,
    set_code="SV4",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Attack(
            title="Evolution",
            game_text="Choose up to 2 of your Benched Pokémon. For each of those "
                      "Pokémon, search your deck for a card that evolves from that "
                      "Pokémon and put it onto that Pokémon to evolve it. Then, "
                      "shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_evolution_attack,
        ),
        Ability(
            title="Technical Machine: Evolution",
            game_text="Discard this card at the end of your turn.",
            trigger=Triggers.END_OF_TURN,
            effect=discard_tool_at_end_of_turn(),
        ),
    ],
)
