from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.trainers import return_pokemon_to_hand


async def sky_return(ctx):
    """30 damage, then return this Pokemon and all cards attached to it to your
    hand."""
    pokemon = ctx.attacker
    await ctx.deal_damage()
    await return_pokemon_to_hand(lambda p: p is pokemon, with_attachments="same")(ctx)


card = PokemonCardDef(
    guid="b766a345-e0da-52fd-8436-79b9acf45485",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tentacool.Name",
    display_name="Tentacool",
    searchable_by=["Tentacool", "Basic", "Tentacool"],
    subtypes=["Basic"],
    collector_number=70,
    set_code="XY5",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=72,
    abilities=[
        Attack(
            title="Lost in the Waves",
            game_text="Return this Pok\u00e9mon and all cards attached to it to your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=sky_return,
        ),
    ],
)