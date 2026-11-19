from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def flying_fury(ctx):
    """Before damage, discard any number of your Pokémon Tools; +40 damage each."""
    my_tools = [tool for tool, pokemon in ctx.tools_in_play()
                if pokemon.owning_player_id == ctx.player_id]
    picks = []
    if my_tools:
        picks = await ctx.choose_cards(
            my_tools, len(my_tools), minimum=0,
            prompt="Discard any number of Pokémon Tools from your Pokémon.",
        )
    if picks:
        await ctx.discard_cards(picks)
    await ctx.deal_damage(10 + 40 * len(picks))

card = PokemonCardDef(
    guid="2a6ef445-f960-5291-85e6-410fa9772731",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Electrode.Name",
    display_name="Electrode",
    searchable_by=["Electrode", "Stage 1", "Electrode"],
    subtypes=["Stage 1"],
    collector_number=134,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Voltorb.Name",
    family_id=100,
    abilities=[
        Attack(
            title="Bang Boom Chain",
            game_text="Before doing damage, you may discard any number of Pok\u00e9mon Tools from your Pok\u00e9mon. This attack does 40 more damage for each card you discarded in this way.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
            damage_operator="+",
            effect=flying_fury,
        ),
        Attack(
            title="Electro Ball",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)