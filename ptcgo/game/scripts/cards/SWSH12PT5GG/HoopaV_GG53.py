from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.session.passives import Passive

async def shadow_impact(ctx):
    """170. Put 3 damage counters on 1 of your Pokemon."""
    await ctx.deal_damage()
    own = ctx.my_pokemon_in_play()
    if own:
        target = await ctx.choose_pokemon(own, "Choose 1 of your Pokémon")
        if target is not None:
            await ctx.deal_damage(30, target=target, apply_modifiers=False, as_counters=True)

card = PokemonCardDef(
    guid="46f7a635-ee46-5d29-967b-c908de81c132",
    key="SWSH12PT5GG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HoopaV.Name",
    display_name="Hoopa V",
    searchable_by=["Hoopa V", "Basic", "V", "Fusion Strike", "HoopaV"],
    subtypes=["Basic", "V", "Fusion Strike"],
    collector_number=53,
    set_code="SWSH12PT5GG",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=720,
    abilities=[
        Ability(
            title="Two-Faced",
            game_text="As long as this Pok\u00e9mon is in play, it is Psychic and Darkness type.",
            effect=unimplemented,
        ),
        Attack(
            title="Shadow Impact",
            game_text="Put 3 damage counters on 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=170,
            effect=shadow_impact,
        ),
    ],
)