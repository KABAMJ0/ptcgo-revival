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
    guid="765536ab-044a-5409-8f5f-6e560fba7841",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Phione.Name",
    display_name="Phione",
    searchable_by=["Phione", "Basic", "Phione"],
    subtypes=["Basic"],
    collector_number=36,
    set_code="BW11",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=489,
    abilities=[
        Attack(
            title="Pull Out",
            game_text="Put a card from your discard pile on top of your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Aqua Boomerang",
            game_text="Return this Pok\u00e9mon and all cards attached to it to your hand.",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            effect=sky_return,
        ),
    ],
)