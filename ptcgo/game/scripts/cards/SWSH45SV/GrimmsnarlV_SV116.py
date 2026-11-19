from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.pokemon import energy_provides_type


async def spiky_knuckle(ctx):
    """200. Put 2 Darkness Energy attached to this Pokemon into your hand."""
    await ctx.deal_damage()
    energies = [
        e for e in ctx.attached_energies(ctx.source)
        if energy_provides_type(e, PokemonTypes.DARKNESS)
    ]
    if not energies:
        return
    picks = await ctx.choose_cards(
        energies, 2,
        prompt="Choose up to 2 Darkness Energy to put into your hand.",
    )
    await ctx.put_in_hand(picks, reveal=False)


card = PokemonCardDef(
    guid="afc074ad-64ee-58b9-9a3c-11006d765596",
    key="SWSH45SV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GrimmsnarlV.Name",
    display_name="Grimmsnarl V",
    searchable_by=["Grimmsnarl V", "Basic", "V", "GrimmsnarlV"],
    subtypes=["Basic", "V"],
    collector_number=116,
    set_code="SWSH45SV",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=861,
    abilities=[
        Attack(
            title="Bite",
            cost={PokemonTypes.DARKNESS: 1},
            damage=40,
        ),
        Attack(
            title="Spiky Knuckle",
            game_text="Put 2 Darkness Energy attached to this Pok\u00e9mon into your hand.",
            cost={PokemonTypes.DARKNESS: 3},
            damage=200,
            effect=spiky_knuckle,
        ),
    ],
)