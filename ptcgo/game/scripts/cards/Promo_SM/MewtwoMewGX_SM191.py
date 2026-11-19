from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import extra_energy_beyond_cost

async def miraculous_duo(ctx):
    await ctx.deal_damage()
    if extra_energy_beyond_cost(ctx) < 1:
        return
    for pokemon in ctx.my_pokemon_in_play():
        await ctx.heal(ctx.max_hp(pokemon), pokemon)


card = PokemonCardDef(
    guid="993b69c4-fb1a-5dd7-83d7-388231994727",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MewtwoMewGX.Name",
    display_name="Mewtwo & Mew-GX",
    searchable_by=["Mewtwo & Mew-GX", "Basic", "TAG TEAM", "GX", "MewtwoMewGX"],
    subtypes=["Basic", "TAG TEAM", "GX"],
    collector_number=191,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=270,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=150,
    abilities=[
        Ability(
            title="Perfection",
            game_text="This Pok\u00e9mon can use the attacks of any Pok\u00e9mon-GX or Pok\u00e9mon-EX on your Bench or in your discard pile. (You still need the necessary Energy to use each attack.)",
            effect=unimplemented,
        ),
        Attack(
            title="Miraculous Duo-GX",
            game_text="If this Pok\u00e9mon has at least 1 extra Energy attached to it (in addition to this attack's cost), heal all damage from all of your Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=miraculous_duo,
        ),
    ],
)